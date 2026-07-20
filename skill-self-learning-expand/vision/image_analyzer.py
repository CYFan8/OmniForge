"""
Image Analyzer — 本地视觉分析引擎
基于 BLIP (Salesforce/blip-image-captioning-base)
使用: from image_analyzer import ImageAnalyzer
"""
import torch
from transformers import BlipForConditionalGeneration, BlipProcessor
from PIL import Image

class ImageAnalyzer:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._loaded = False
        return cls._instance
    
    def load(self):
        if self._loaded:
            return
        model_id = "Salesforce/blip-image-captioning-base"
        self.processor = BlipProcessor.from_pretrained(model_id)
        self.model = BlipForConditionalGeneration.from_pretrained(
            model_id, torch_dtype=torch.float16
        ).to("cuda")
        self._loaded = True
        print(f"[Vision] BLIP loaded on GPU ({sum(p.numel() for p in self.model.parameters())/1e6:.0f}M params)")
    
    def caption(self, image_path, prompt="a photo of", max_tokens=100):
        if not self._loaded:
            self.load()
        img = Image.open(image_path).convert("RGB")
        inputs = self.processor(img, text=prompt, return_tensors="pt").to("cuda")
        out = self.model.generate(**inputs, max_new_tokens=max_tokens)
        return self.processor.decode(out[0], skip_special_tokens=True)
    
    def analyze_blender_render(self, image_path):
        """专门分析 Blender 渲染输出"""
        base = self.caption(image_path, "a photo of", 50)
        detail = self.caption(image_path, "what is shown in this image", 100)
        return {"base": base, "detail": detail}
