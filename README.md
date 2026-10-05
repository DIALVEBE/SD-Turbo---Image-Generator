# Generdaor de Imagenes con stabilityai/sd-turbo

Este proyecto permite generar imágenes a partir de una descripción de texto usando **Stable Diffusion Turbo** de manera local.

## Requisitos

- Python
- `uv`

## Crear el proyecto

```bash
uv init generador-imagenes
cd generador-imagenes
```

## Instalar dependencias

```bash
uv add torch diffusers transformers accelerate
```

## Código

El archivo principal puede llamarse:

```text
main.py
```

El programa:

1. Carga el modelo `stabilityai/sd-turbo`.
2. Solicita una descripción de la imagen.
3. Genera la imagen usando el procesador del computador.
4. Guarda el resultado como `imagen.png`.

## Ejecutar

```bash
uv run main.py
```

El programa solicitará un prompt:

```text
Describe la imagen que quieres crear:
```

Por ejemplo:

```text
A robot teaching artificial intelligence in a university classroom
```

Al finalizar se creará:

```text
imagen.png
```

## Parámetros principales

En la generación encontramos:

```python
imagen = modelo(
    prompt=prompt,
    num_inference_steps=1,
    guidance_scale=0.0
).images[0]
```

### `prompt`

Es la descripción de la imagen que queremos generar.

### `num_inference_steps`

Indica cuántos pasos utiliza el modelo para construir la imagen.

```python
num_inference_steps=1
```

SD-Turbo está diseñado para trabajar con pocos pasos.

### `guidance_scale`

Controla cuánto intenta seguir el modelo las instrucciones del prompt.

```python
guidance_scale=0.0
```

SD-Turbo está diseñado para funcionar con valores bajos.

## Importante

La primera vez que se ejecuta el programa, el modelo debe descargarse desde Hugging Face.

Después de la descarga, el modelo queda almacenado localmente y puede reutilizarse.

## Resultado

El flujo básico del programa es:

```text
Prompt
  ↓
Modelo SD-Turbo
  ↓
Generación de imagen
  ↓
imagen.png
```

Este ejemplo sirve como introducción al funcionamiento de los modelos generativos de texto a imagen.
