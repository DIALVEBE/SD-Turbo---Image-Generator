import torch
from diffusers import AutoPipelineForText2Image

print("Cargando modelo...")

modelo = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/sd-turbo",
    torch_dtype=torch.float32
)

modelo = modelo.to("cpu")

prompt = input("Escribe el prompt de la imagen que quieres crear: ")
# negative_prompt="blurry, low quality, distorted, extra fingers, bad anatomy, cropped, deformed"

print("Generando imagen...")

imagen = modelo(
    prompt=prompt,
    # negative_prompt=negative_prompt,
    num_inference_steps=1, # Cambiar a 10
    guidance_scale=0.0, # Cambiar a 1.0
    # height=1024, 
    # width=1024
).images[0]

imagen.save("imagen.png")

print("Imagen guardada como imagen.png")
