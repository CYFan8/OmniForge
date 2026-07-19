#!/usr/bin/env python3
"""Photoshop MCP Bridge - COM Automation on Windows

Exposes Photoshop operations via a simple JSON-RPC interface for the image-generation skill.
Supports: layer management, canvas operations, Firefly AI generation, batch export.

Dependency: pip install pywin32
"""

import json
import sys
import os
from pathlib import Path

try:
    import win32com.client
    HAS_WIN32 = True
except ImportError:
    HAS_WIN32 = False

class PhotoshopBridge:
    """COM-based Photoshop automation bridge."""

    def __init__(self):
        self.app = None
        self.connected = False

    def connect(self):
        """Attempt to connect to running Photoshop instance via COM."""
        if not HAS_WIN32:
            return {"status": "error", "message": "pywin32 not installed. Run: pip install pywin32"}

        try:
            self.app = win32com.client.Dispatch("Photoshop.Application")
            self.connected = True
            version = self.app.Version if hasattr(self.app, 'Version') else 'unknown'
            return {"status": "connected", "version": str(version)}
        except Exception as e:
            # Try alternate ProgID for older PS versions
            try:
                self.app = win32com.client.Dispatch("Photoshop.Application.2024")
                self.connected = True
                return {"status": "connected", "version": "2024+"}
            except:
                pass
            return {"status": "not_found", "message": f"Photoshop not running or not installed. Error: {e}"}

    def disconnect(self):
        """Release COM reference."""
        self.app = None
        self.connected = False
        return {"status": "disconnected"}

    def status(self):
        """Check connection status and Photoshop details."""
        if not self.connected:
            return {"status": "disconnected"}

        try:
            doc = self.app.ActiveDocument
            doc_info = None
            if doc:
                doc_info = {
                    "name": doc.Name,
                    "width": doc.Width,
                    "height": doc.Height,
                    "resolution": doc.Resolution,
                    "mode": str(doc.Mode) if doc.Mode else "unknown",
                    "layers_count": doc.Layers.Count if doc.Layers else 0
                }
            return {
                "status": "connected",
                "version": str(self.app.Version) if hasattr(self.app, 'Version') else 'unknown',
                "active_document": doc_info
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def create_canvas(self, width=1920, height=1080, resolution=300, name="AI_Generated"):
        """Create a new canvas/document."""
        if not self.connected:
            return {"status": "error", "message": "Not connected"}

        try:
            doc = self.app.Documents.Add(width, height, resolution, name)
            return {
                "status": "ok",
                "document": {
                    "name": doc.Name,
                    "width": doc.Width,
                    "height": doc.Height
                }
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def add_layer(self, name="New Layer"):
        """Add a new layer to active document."""
        if not self.connected:
            return {"status": "error", "message": "Not connected"}

        try:
            doc = self.app.ActiveDocument
            layer = doc.ArtLayers.Add()
            layer.Name = name
            return {"status": "ok", "layer_name": name}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def export_as(self, format="png", output_path=None):
        """Export active document as PNG/JPG/PSD."""
        if not self.connected:
            return {"status": "error", "message": "Not connected"}

        try:
            doc = self.app.ActiveDocument
            if not output_path:
                output_path = str(Path.home() / "Desktop" / f"{doc.Name}.{format}")

            format_map = {
                "png": 2,   # psdPNGSave
                "jpg": 1,   # psdJPEGSave
                "psd": 0,   # psdPhotoshopSave
            }

            save_format = format_map.get(format.lower(), 2)

            if format.lower() == "png":
                options = win32com.client.Dispatch("Photoshop.PNGSaveOptions")
                doc.SaveAs(output_path, options, True)
            elif format.lower() == "jpg":
                options = win32com.client.Dispatch("Photoshop.JPEGSaveOptions")
                options.Quality = 10
                doc.SaveAs(output_path, options, True)
            else:
                doc.SaveAs(output_path)

            return {"status": "ok", "output_path": output_path, "format": format}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def run_firefly(self, prompt):
        """Run Photoshop Firefly generative fill/fill using the prompt."""
        if not self.connected:
            return {"status": "error", "message": "Not connected"}

        return {
            "status": "not_implemented",
            "message": (
                "Firefly AI requires manual interaction in Photoshop. "
                "Use Edit > Generative Fill and paste this prompt manually. "
                f"Prompt: {prompt}"
            ),
            "prompt": prompt
        }


def main():
    bridge = PhotoshopBridge()
    args = sys.argv[1:] if len(sys.argv) > 1 else ["status"]

    command = args[0] if args else "status"

    if command == "connect":
        result = bridge.connect()
    elif command == "disconnect":
        result = bridge.disconnect()
    elif command == "status":
        bridge.connect()
        result = bridge.status()
    elif command == "create":
        width = int(args[1]) if len(args) > 1 else 1920
        height = int(args[2]) if len(args) > 2 else 1080
        name = args[3] if len(args) > 3 else "AI_Generated"
        result = bridge.create_canvas(width, height, 300, name)
    elif command == "layer":
        name = args[1] if len(args) > 1 else "New Layer"
        result = bridge.add_layer(name)
    elif command == "export":
        fmt = args[1] if len(args) > 1 else "png"
        path = args[2] if len(args) > 2 else None
        result = bridge.export_as(fmt, path)
    elif command == "firefly":
        prompt = " ".join(args[1:]) if len(args) > 1 else ""
        result = bridge.run_firefly(prompt)
    else:
        result = {"status": "error", "message": f"Unknown command: {command}"}

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()