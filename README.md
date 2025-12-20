# Transcriptor de Audio y Videos de YouTube con Whisper

Este proyecto permite transcribir archivos de audio locales y videos de YouTube utilizando el modelo Whisper de OpenAI.

## Requisitos

Antes de ejecutar el programa, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.8 o superior
- ffmpeg
- yt-dlp
- whisper

Puedes instalar las dependencias necesarias con el siguiente comando:

```bash
pip install yt-dlp openai-whisper ffmpeg-python
```

Además, debes asegurarte de que `ffmpeg` está instalado y accesible desde la línea de comandos. Puedes verificarlo ejecutando:

```bash
ffmpeg -version
```

## Uso

Ejecuta el script con:

```bash
python Transcriptor.py
```

### Opciones del menú

1. **Transcribir un archivo de audio local**
   - Se pedirá la ruta del archivo de audio.
   - Se debe ingresar el nombre del archivo de salida en formato `.txt`.
   - Se debe elegir un modelo de Whisper (`tiny`, `base`, `small`, `medium`, `large`).

2. **Transcribir un video de YouTube**
   - Se debe ingresar la URL del video de YouTube.
   - Se pedirá el nombre del archivo de salida en formato `.txt`.
   - Se debe elegir un modelo de Whisper (`tiny`, `base`, `small`, `medium`, `large`).

3. **Salir**
   - Finaliza la ejecución del programa.

## Funcionamiento

### Transcripción de archivos de audio locales

El programa utiliza `whisper` para transcribir archivos de audio. Además, detecta automáticamente el idioma del audio antes de la transcripción.

### Descarga y transcripción de videos de YouTube

El programa utiliza `yt-dlp` para descargar el audio del video en formato MP3 y luego lo transcribe utilizando Whisper.

## Consideraciones

- Asegúrate de que los archivos de audio sean de buena calidad para obtener una transcripción precisa.
- La transcripción puede tardar más en modelos más grandes, pero estos ofrecen mayor precisión.
- `ffmpeg` debe estar instalado correctamente para la conversión de audio.

## Autor

Este proyecto fue desarrollado para facilitar la transcripción de archivos de audio y videos de YouTube de manera sencilla y eficiente utilizando Whisper.

¡Disfruta transcribiendo tus audios y videos! 🎙️

