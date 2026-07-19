#!/usr/bin/env python3
"""SAI (PaintTool SAI / SAI2) Filesystem Bridge

SAI has no automation API. This bridge works via filesystem:
- Watches SAI output directories for new saved files
- Converts SAI native files (.sai/.sai2) by extracting embedded preview PNG
- Manages a work directory for SAI to read prompts and save outputs

Dependency: pip install watchdog Pillow
"""

import json
import os
import struct
import sys
from pathlib import Path
from datetime import datetime

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


class SAIBridge:
    """Filesystem-based bridge for PaintTool SAI/SAI2."""

    def __init__(self, work_dir=None):
        self.work_dir = Path(work_dir) if work_dir else Path.home() / "SAI_Work"
        self.prompts_dir = self.work_dir / "prompts"
        self.outputs_dir = self.work_dir / "outputs"
        self._ensure_dirs()

    def _ensure_dirs(self):
        self.work_dir.mkdir(parents=True, exist_ok=True)
        self.prompts_dir.mkdir(exist_ok=True)
        self.outputs_dir.mkdir(exist_ok=True)

    def status(self):
        """Report bridge status and directory structure."""
        prompt_files = list(self.prompts_dir.glob("*"))
        output_files = list(self.outputs_dir.glob("*"))
        return {
            "status": "ok",
            "work_dir": str(self.work_dir),
            "prompts_pending": len([f for f in prompt_files if f.suffix == '.txt']),
            "outputs_ready": len([f for f in output_files if f.suffix in ['.png', '.psd', '.sai', '.sai2']]),
            "note": "SAI has no API. Workflow: write prompt to prompts/, user draws in SAI, saves to outputs/."
        }

    def send_prompt(self, prompt_text, filename=None, include_settings=None):
        """Write a drawing prompt as a text file for the user to follow in SAI.

        Args:
            prompt_text: The drawing prompt/description
            filename: Optional filename (auto-generated if None)
            include_settings: Optional dict with canvas settings {width, height, dpi, brush}
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if not filename:
            filename = f"prompt_{timestamp}.txt"

        content = f"=== SAI Drawing Prompt ===\n"
        content += f"Time: {datetime.now().isoformat()}\n"
        content += f"---\n\n"
        content += prompt_text
        content += f"\n\n---\n"

        if include_settings:
            content += "Canvas Settings:\n"
            content += f"  Width: {include_settings.get('width', 1920)}px\n"
            content += f"  Height: {include_settings.get('height', 1080)}px\n"
            content += f"  DPI: {include_settings.get('dpi', 300)}\n"
            if 'brush' in include_settings:
                content += f"  Suggested Brush: {include_settings['brush']}\n"

        filepath = self.prompts_dir / filename
        filepath.write_text(content, encoding="utf-8")
        return {
            "status": "ok",
            "prompt_file": str(filepath),
            "message": f"Prompt saved. Open in SAI and save output to: {self.outputs_dir}"
        }

    def list_outputs(self, pattern="*.png"):
        """List files in outputs directory."""
        files = sorted(self.outputs_dir.glob(pattern), key=lambda f: f.stat().st_mtime, reverse=True)
        return {
            "status": "ok",
            "count": len(files),
            "files": [{"name": f.name, "size": f.stat().st_size, "modified": datetime.fromtimestamp(f.stat().st_mtime).isoformat()} for f in files[:20]]
        }

    def convert_sai_preview(self, sai_file, output_png=None):
        """Extract embedded preview PNG from SAI/SAI2 file.

        SAI2 files (.sai2) embed a preview PNG. This extracts it.
        SAI1 files (.sai) have a different format - tries best-effort extraction.
        """
        sai_path = Path(sai_file)
        if not sai_path.exists():
            return {"status": "error", "message": f"File not found: {sai_file}"}

        if not output_png:
            output_png = sai_path.with_suffix('.png')

        try:
            data = sai_path.read_bytes()

            # SAI2 format: 8-byte header + embedded PNG after
            if sai_path.suffix.lower() == '.sai2':
                # Find PNG header (89 50 4E 47)
                png_start = data.find(b'\x89PNG')
                if png_start > 0:
                    png_data = data[png_start:]
                    Path(output_png).write_bytes(png_data)
                    return {
                        "status": "ok",
                        "output": str(output_png),
                        "size": len(png_data),
                        "method": "SAI2 embedded PNG extraction"
                    }

            # SAI1 format: try to find any PNG-like data
            png_start = data.find(b'\x89PNG')
            if png_start > 0:
                png_data = data[png_start:]
                Path(output_png).write_bytes(png_data)
                return {
                    "status": "ok",
                    "output": str(output_png),
                    "size": len(png_data),
                    "method": "PNG header detection"
                }

            return {
                "status": "error",
                "message": f"No embedded PNG found in {sai_file}. Try saving as PNG from SAI manually."
            }

        except Exception as e:
            return {"status": "error", "message": str(e)}

    def clean_prompts(self):
        """Remove processed prompt files."""
        removed = 0
        for f in self.prompts_dir.glob("*.txt"):
            f.unlink()
            removed += 1
        return {"status": "ok", "removed": removed}


def main():
    bridge = SAIBridge()
    args = sys.argv[1:] if len(sys.argv) > 1 else ["status"]

    command = args[0] if args else "status"

    if command == "status":
        result = bridge.status()
    elif command == "prompt":
        prompt_text = " ".join(args[1:]) if len(args) > 1 else "Draw a character design"
        result = bridge.send_prompt(prompt_text)
    elif command == "outputs":
        pattern = args[1] if len(args) > 1 else "*.png"
        result = bridge.list_outputs(pattern)
    elif command == "convert":
        sai_file = args[1] if len(args) > 1 else None
        output = args[2] if len(args) > 2 else None
        if not sai_file:
            result = {"status": "error", "message": "Usage: sai_bridge.py convert <sai_file> [output_png]"}
        else:
            result = bridge.convert_sai_preview(sai_file, output)
    elif command == "clean":
        result = bridge.clean_prompts()
    else:
        result = {"status": "error", "message": f"Unknown command: {command}"}

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()