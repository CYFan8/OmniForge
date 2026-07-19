#!/usr/bin/env python3
"""MCP Router - Unified dispatch for all drawing tool bridges.

Routes image generation requests to the appropriate bridge:
- Photoshop (COM automation) -> photoshop_bridge.py
- Stable Diffusion (REST API) -> sd_bridge.py
- SAI (filesystem bridge) -> sai_bridge.py
- Krita (Python API bridge) -> krita_bridge.py

Usage:
    python router.py <tool> <command> [args...]
    python router.py init     # Check all tools
    python router.py status   # Report all bridge statuses
"""

import json
import sys
import os
import subprocess
from pathlib import Path

MCP_DIR = Path(__file__).parent



# ---- 加载配置 ----
import json as _json
_config_path = MCP_DIR / "config.json"
_config = {}
if _config_path.exists():
    try:
        _config = _json.loads(_config_path.read_text(encoding="utf-8"))
    except:
        pass

_DISABLE_OPENAI = _config.get("defaults", {}).get("disable_openai_image_backend", True)
_DISABLE_FALLBACK = _config.get("defaults", {}).get("disable_fallback", True)
_FORCE_MCP = _config.get("image_route_rule", {}).get("force_mcp_render", True)
_ALLOW_CLOUD = _config.get("image_route_rule", {}).get("allow_cloud_image_fallback", False)
_DEFAULT_PROVIDER = _config.get("defaults", {}).get("provider", "sd_webui")
_LLM_PROVIDER = _config.get("defaults", {}).get("llm_provider", "")  # 空=不锁定，用户自由切换

class MCPRouter:
    def __init__(self):
        self.bridges = {
            "ps": {
                "name": "Photoshop",
                "script": "photoshop_bridge.py",
                "type": "COM",
                "available": None,
                "version": None
            },
            "sd": {
                "name": "Stable Diffusion",
                "script": "sd_bridge.py",
                "type": "REST API",
                "available": None,
                "version": None
            },
            "sai": {
                "name": "PaintTool SAI",
                "script": "sai_bridge.py",
                "type": "Filesystem",
                "available": None,
                "version": None
            },
            "krita": {
                "name": "Krita",
                "script": "krita_bridge.py",
                "type": "Python API",
                "available": None,
                "version": None
            }
        }

    def _run_bridge(self, bridge_key, *args):
        """Run a bridge script and return parsed JSON result."""
        script = MCP_DIR / self.bridges[bridge_key]["script"]
        if not script.exists():
            return {"status": "error", "message": f"Bridge script not found: {script}"}

        cmd = [sys.executable, str(script)] + list(args)
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30, cwd=str(MCP_DIR))
            if result.returncode == 0 and result.stdout.strip():
                return json.loads(result.stdout)
            elif result.stderr:
                return {"status": "error", "message": result.stderr.strip()[:500]}
            else:
                return {"status": "error", "message": "No output from bridge"}
        except subprocess.TimeoutExpired:
            return {"status": "error", "message": "Bridge timed out"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def init(self):
        """Initialize: check all bridges."""
        results = {}

        # Check SD first (default provider per config)
        sd_result = self._run_bridge("sd", "status")
        self.bridges["sd"]["available"] = sd_result.get("status") == "connected"
        self.bridges["sd"]["version"] = sd_result.get("current_model", "")
        results["stable_diffusion"] = sd_result

        # Check Photoshop
        ps_result = self._run_bridge("ps", "status")
        self.bridges["ps"]["available"] = ps_result.get("status") == "connected"
        self.bridges["ps"]["version"] = ps_result.get("version", "")
        results["photoshop"] = ps_result



        # Check SAI (always "available" - filesystem based)
        sai_result = self._run_bridge("sai", "status")
        self.bridges["sai"]["available"] = True  # Filesystem, always available
        results["sai"] = sai_result

        # Calculate overall status
        available_count = sum(1 for b in self.bridges.values() if b["available"])
        results["summary"] = {
            "total_tools": len(self.bridges),
            "available": available_count,
            "tools": {k: {"name": v["name"], "type": v["type"], "available": v["available"]} for k, v in self.bridges.items()}
        }

        return results

    def status(self):
        """Get status of all bridges (no re-init)."""
        return {
            "tools": {
                k: {
                    "name": v["name"],
                    "type": v["type"],
                    "available": v["available"]
                }
                for k, v in self.bridges.items()
            }
        }

    def generate(self, tool, prompt, **kwargs):
        """Generate an image using the specified tool.

        受 image_route_rule 约束：force_mcp_render=true 时所有请求强制走本地MCP，
        allow_cloud_image_fallback=false 时禁止兜底任何云端接口。

        Args:
            tool: "sd" | "ps" | "sai"
            prompt: Generation prompt text
            **kwargs: Tool-specific parameters
        """
        # 强约束：禁止云端回退
        if _FORCE_MCP and not _ALLOW_CLOUD:
            if tool not in ["sd", "ps", "sai"]:
                return {"status": "blocked", "message": "Cloud image APIs disabled. Use sd/ps/sai via MCP only."}

        if tool not in self.bridges:
            return {"status": "error", "message": f"Unknown tool: {tool}. Available: {list(self.bridges.keys())}"}

        bridge_info = self.bridges[tool]

        if tool == "ps":
            # Photoshop: create canvas, add layer, export
            width = kwargs.get("width", 1920)
            height = kwargs.get("height", 1080)
            name = kwargs.get("name", "AI_Generated")

            result = self._run_bridge("ps", "connect")
            if result.get("status") != "connected":
                return {"status": "ps_unavailable", "message": "Photoshop not available. Fallback disabled per config."}

            canvas = self._run_bridge("ps", "create", str(width), str(height), name)
            layer = self._run_bridge("ps", "layer", "AI_Layer")
            export = self._run_bridge("ps", "export", "png")

            return {
                "status": "ok",
                "tool": "photoshop",
                "canvas": canvas,
                "export": export,
                "note": "Firefly generation requires manual prompt in Photoshop"
            }

        elif tool == "sd":
            # Stable Diffusion: txt2img
            width = kwargs.get("width", 512)
            height = kwargs.get("height", 512)
            steps = kwargs.get("steps", 20)
            cfg = kwargs.get("cfg_scale", 7)
            negative = kwargs.get("negative_prompt", "")

            return self._run_bridge("sd", "generate", prompt)

        elif tool == "sai":
            # SAI: write prompt file for manual drawing
            return self._run_bridge("sai", "prompt", prompt)

        return {"status": "error", "message": f"No generation method for: {tool}"}

    def refine(self, tool, input_image, prompt, **kwargs):
        """Refine an existing image using the specified tool."""
        if tool == "sd":
            strength = kwargs.get("strength", 0.75)
            return self._run_bridge("sd", "refine", input_image, prompt)
        elif tool == "ps":
            return self._run_bridge("ps", "status")  # Open in PS for manual refinement
        return {"status": "error", "message": f"Refine not supported for: {tool}"}


def main():
    router = MCPRouter()
    args = sys.argv[1:] if len(sys.argv) > 1 else ["status"]

    command = args[0] if args else "status"

    if command == "init":
        result = router.init()
    elif command == "status":
        router.init()  # Quick check first
        result = router.status()
    elif command == "generate":
        if len(args) < 3:
            result = {"status": "error", "message": "Usage: router.py generate <tool> <prompt>"}
        else:
            tool = args[1]
            prompt = " ".join(args[2:])
            result = router.generate(tool, prompt)
    elif command == "refine":
        if len(args) < 4:
            result = {"status": "error", "message": "Usage: router.py refine <tool> <image> <prompt>"}
        else:
            result = router.refine(args[1], args[2], " ".join(args[3:]))
    else:
        result = {"status": "error", "message": f"Unknown command: {command}"}

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()