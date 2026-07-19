#!/usr/bin/env python3
"""Stable Diffusion REST API Bridge

Connects to AUTOMATIC1111 SD WebUI or ComfyUI API for AI image generation.
Requires Stable Diffusion WebUI running with --api flag.

Dependency: pip install requests Pillow
"""

import json
import os
import sys
import base64
import time
from pathlib import Path
from datetime import datetime

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

try:
    from PIL import Image
    import io
    HAS_PIL = True
except ImportError:
    HAS_PIL = False



# Guard: block OpenAI image calls
import os as _os
_force_mcp = _os.environ.get("IMAGE_ROUTE_FORCE_MCP", "true").lower() == "true"
_allow_cloud = _os.environ.get("IMAGE_ROUTE_ALLOW_CLOUD_FALLBACK", "false").lower() == "true"
if _force_mcp and not _allow_cloud:
    _CLOUD_BLOCKED = True
else:
    _CLOUD_BLOCKED = False

class SDBridge:
    """REST API bridge for Stable Diffusion WebUI."""

    def __init__(self, api_url="http://127.0.0.1:7861"):
        self.api_url = api_url.rstrip("/").replace("/mcp", "")
        self.connected = False
        self.models = []
        self.current_model = None

    def _check_cloud_block(self):
        if _CLOUD_BLOCKED:
            return {"status": "blocked", "message": "Cloud image APIs disabled. Use local MCP only."}
        return None

    def connect(self):
        """Test connection to SD WebUI API."""
        block = self._check_cloud_block()
        if block:
            return block
        if not HAS_REQUESTS:
            return {"status": "error", "message": "requests not installed. Run: pip install requests"}

        try:
            resp = requests.get(f"{self.api_url}/mcp/sdapi/v1/sd-models", timeout=5)
            if resp.status_code == 200:
                self.connected = True
                self.models = resp.json()
                # Find current model
                for m in self.models:
                    if m.get('title') == self._get_current_model_name():
                        self.current_model = m
                        break
                return {
                    "status": "connected",
                    "api_url": self.api_url,
                    "models_available": len(self.models),
                    "current_model": self.current_model.get('model_name', 'unknown') if self.current_model else 'unknown'
                }
        except requests.exceptions.ConnectionError:
            pass
        except Exception as e:
            return {"status": "error", "message": str(e)}

        return {"status": "not_found", "message": "SD WebUI not running. Start with: python launch.py --api"}

    def _get_current_model_name(self):
        try:
            resp = requests.get(f"{self.api_url}/mcp/sdapi/v1/options", timeout=3)
            if resp.status_code == 200:
                return resp.json().get('sd_model_checkpoint', '')
        except:
            pass
        return ''

    def status(self):
        """Get detailed SD status."""
        base = self.connect()
        if not self.connected:
            return base

        try:
            options = requests.get(f"{self.api_url}/mcp/sdapi/v1/options", timeout=3).json()
            samplers = requests.get(f"{self.api_url}/mcp/sdapi/v1/samplers", timeout=3).json()

            return {
                "status": "connected",
                "api_url": self.api_url,
                "current_model": self.current_model.get('model_name', 'unknown') if self.current_model else 'unknown',
                "samplers": [s['name'] for s in samplers[:5]],
                "models_count": len(self.models)
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def txt2img(self, prompt, negative_prompt="", width=512, height=512, steps=20, cfg_scale=7, seed=-1, batch_size=1):
        """Generate image from text prompt via SD API.

        Args:
            prompt: Positive prompt text
            negative_prompt: Negative prompt text
            width: Image width (multiple of 8)
            height: Image height (multiple of 8)
            steps: Sampling steps (20-50)
            cfg_scale: CFG scale (1-30)
            seed: Random seed (-1 for random)
            batch_size: Number of images to generate (1-8)

        Returns:
            dict with status, saved image paths, and metadata
        """
        if not self.connected:
            result = self.connect()
            if not self.connected:
                return result

        payload = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "steps": steps,
            "cfg_scale": cfg_scale,
            "seed": seed,
            "batch_size": batch_size,
            "save_images": True
        }

        try:
            resp = requests.post(
                f"{self.api_url}/mcp/sdapi/v1/txt2img",
                json=payload,
                timeout=120
            )

            if resp.status_code != 200:
                return {"status": "error", "message": f"API error: {resp.status_code}", "detail": resp.text}

            result = resp.json()
            images = result.get('images', [])
            info = json.loads(result.get('info', '{}'))

            # Save images
            saved = []
            output_dir = Path.home() / "Codex" / "generated_images"
            output_dir.mkdir(parents=True, exist_ok=True)

            for i, img_b64 in enumerate(images):
                if HAS_PIL:
                    img_data = base64.b64decode(img_b64)
                    img = Image.open(io.BytesIO(img_data))
                    filename = f"sd_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{i+1}.png"
                    filepath = output_dir / filename
                    img.save(filepath)
                    saved.append(str(filepath))
                else:
                    # Fallback: save raw
                    filename = f"sd_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{i+1}.png"
                    filepath = output_dir / filename
                    filepath.write_bytes(base64.b64decode(img_b64))
                    saved.append(str(filepath))

            return {
                "status": "ok",
                "images": saved,
                "count": len(saved),
                "seed": info.get('seed', seed),
                "model": info.get('sd_model_name', 'unknown'),
                "prompt": prompt[:200],
                "steps": steps,
                "cfg_scale": cfg_scale
            }

        except requests.exceptions.Timeout:
            return {"status": "error", "message": "Request timed out. Try reducing steps or image size."}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def img2img(self, input_image_path, prompt, negative_prompt="", denoising_strength=0.75, steps=20, seed=-1):
        """Image-to-image generation (refine existing image).

        Args:
            input_image_path: Path to input image
            prompt: Positive prompt
            negative_prompt: Negative prompt
            denoising_strength: How much to change (0.0-1.0)
            steps: Sampling steps
            seed: Random seed
        """
        if not self.connected:
            result = self.connect()
            if not self.connected:
                return result

        if not os.path.exists(input_image_path):
            return {"status": "error", "message": f"Input image not found: {input_image_path}"}

        try:
            # Read and encode input image
            with open(input_image_path, 'rb') as f:
                img_b64 = base64.b64encode(f.read()).decode()

            payload = {
                "init_images": [img_b64],
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "denoising_strength": denoising_strength,
                "steps": steps,
                "seed": seed,
                "save_images": True
            }

            resp = requests.post(
                f"{self.api_url}/mcp/sdapi/v1/img2img",
                json=payload,
                timeout=120
            )

            if resp.status_code != 200:
                return {"status": "error", "message": f"API error: {resp.status_code}"}

            result = resp.json()
            images = result.get('images', [])

            # Save refined images
            saved = []
            output_dir = Path.home() / "Codex" / "generated_images"
            output_dir.mkdir(parents=True, exist_ok=True)

            for i, img_b64 in enumerate(images):
                img_data = base64.b64decode(img_b64)
                filename = f"sd_refined_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{i+1}.png"
                filepath = output_dir / filename
                filepath.write_bytes(img_data)
                saved.append(str(filepath))

            return {"status": "ok", "images": saved, "count": len(saved)}

        except Exception as e:
            return {"status": "error", "message": str(e)}

    def list_models(self):
        """List available SD models."""
        if not self.connected:
            self.connect()
        return {
            "status": "ok" if self.connected else "disconnected",
            "count": len(self.models),
            "models": [{"name": m.get('model_name', ''), "title": m.get('title', '')} for m in self.models[:10]]
        }

    def switch_model(self, model_name):
        """Switch to a different SD model."""
        if not self.connected:
            self.connect()
            if not self.connected:
                return {"status": "error", "message": "Not connected"}

        try:
            payload = {"sd_model_checkpoint": model_name}
            resp = requests.post(f"{self.api_url}/mcp/sdapi/v1/options", json=payload, timeout=10)
            if resp.status_code == 200:
                return {"status": "ok", "message": f"Switched to {model_name}. Reload may take a moment."}
            return {"status": "error", "message": f"Failed to switch model: {resp.status_code}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}


def main():
    bridge = SDBridge()
    args = sys.argv[1:] if len(sys.argv) > 1 else ["status"]

    command = args[0] if args else "status"

    if command == "status":
        result = bridge.status()
    elif command == "models":
        result = bridge.list_models()
    elif command == "generate":
        prompt = " ".join(args[1:]) if len(args) > 1 else "a beautiful landscape"
        result = bridge.txt2img(prompt)
    elif command == "refine":
        if len(args) < 3:
            result = {"status": "error", "message": "Usage: sd_bridge.py refine <input_image> <prompt>"}
        else:
            result = bridge.img2img(args[1], " ".join(args[2:]))
    elif command == "switch":
        model = " ".join(args[1:]) if len(args) > 1 else ""
        result = bridge.switch_model(model) if model else {"status": "error", "message": "No model specified"}
    else:
        result = {"status": "error", "message": f"Unknown command: {command}"}

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()