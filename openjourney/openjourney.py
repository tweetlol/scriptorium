
from diffusers import StableDiffusionPipeline
import torch

model_id = "prompthero/openjourney"
num_steps = 20
prompt_guidance = 7
dimensions = (1000, 1000)

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)

prompt = input("prompt@openjourney: ")

image = pipe(prompt=f"{prompt}, mdjrny-v4 style", num_inference_steps=num_steps, guidance_scale=prompt_guidance, height=dimensions[0], width=dimensions[1]).images[0]
image.save("./image.jpg")

