import torch
import logging
import base64
from io import BytesIO
from diffusers import StableDiffusionPipeline
import json

HF_MODEL_ID = "OFA-Sys/small-stable-diffusion-v0"
PROMPT_SUFFIX = ", cartoon, illustration, drawing, "

class ImageModel:
    def __init__(self) -> None:
        self.model_id = HF_MODEL_ID
        self.suffix = PROMPT_SUFFIX
        self.initialize()
        self.generator = torch.Generator("cuda").manual_seed(1024)
        self.num_images = 3
    
    def initialize(self) -> None:
        self.pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16)
        self.pipe = self.pipe.to("cuda")
    
    def generate_images(self,prompt) -> list[str]:
        prompt += self.suffix
        logging.info(f"prompting Stable Diffusion model with the prompt: {prompt}")
        images  = self.pipe(
            prompt=[prompt]*self.num_images,
            generator=self.generator,
            guidance_scale=7.5,
            num_inference_steps=15,
            height=512,
            width=768).images
        
        results = []
        for i in range(self.num_images):
            buffered = BytesIO()
            images[i].save(f"output_{i}.png")
            images[i].save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
            results.append(f"data:image/png;base64,{img_str}")
        logging.info(f"images from SD: {results}")
        return results
