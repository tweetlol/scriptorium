# openjourney with pytorch

## openjourney.py

- prompts openjourney text2img model, saves generated image as image.jpg
- [huggingface model card](https://huggingface.co/prompthero/openjourney/)

### prequisites

```sh
pip install transformers torch diffusers accelerate safetensors bitsandbytes
```

### parameters

```py
model_id = "prompthero/openjourney"
num_steps = 20
prompt_guidance = 7
dimensions = (1000, 1000)
```

- model_id chooses a model to prompt
- num_steps chooses number of iterations of diffusion loop
- prompt_guidance how guided the model is by the prompt prompted (range 0-50?)
- dimensions (tuple) determines how big the image should be

### the action

```py
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)

prompt = input("prompt@openjourney: ")

image = pipe(prompt=prompt, num_inference_steps=num_steps, guidance_scale=prompt_guidance, height=dimensions[0], width=dimensions[1]).images[0]
image.save("./image.jpg")
```
