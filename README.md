# 🎙️ Transcriptor: Audio, YouTube & Instagram

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI Whisper](https://img.shields.io/badge/OpenAI-Whisper-412991?style=for-the-badge&logo=openai&logoColor=white)
![YouTube](https://img.shields.io/badge/YouTube-Supported-FF0000?style=for-the-badge&logo=youtube&logoColor=white)
![Instagram](https://img.shields.io/badge/Instagram-Supported-E4405F?style=for-the-badge&logo=instagram&logoColor=white)

Herramienta de línea de comandos para transcribir archivos de audio locales, videos de YouTube y reels/posts de Instagram utilizando el modelo **Whisper** de OpenAI. Diseñado para ser rápido, preciso y fácil de usar.

---

## ✨ Características

- ✅ **Transcripción de Audio Local:** Soporta MP3, WAV, M4A, FLAC, OGG, OPUS, y más.
- ✅ **Soporte para YouTube:** Videos normales, Shorts y cualquier URL de YouTube.
- ✅ **Soporte para Instagram:** Reels, posts con video e IGTV.
- ✅ **Notas de Voz WhatsApp:** Compatible con archivos `.opus` y `.ogg`.
- ✅ **Detección de Idioma:** Identifica automáticamente el idioma del audio.
- ✅ **Múltiples Formatos de Salida:**
  - `_limpio.txt` - Texto corrido, fácil de copiar.
  - `_timestamps.txt` - Con marcas de tiempo detalladas.
  - `_parrafos.txt` - Texto dividido en párrafos naturales.
- ✅ **Carpeta Personalizable:** Guarda las transcripciones donde prefieras.
- ✅ **Cookies del Navegador:** Accede a contenido privado o con restricción de edad.
- ✅ **Aceleración por GPU:** Usa núcleos **CUDA** de NVIDIA si están disponibles.

---

## 🔗 URLs Soportadas

| Plataforma | Formatos de URL |
|------------|-----------------|
| **YouTube** | `youtube.com/watch?v=xxx`, `youtu.be/xxx`, `youtube.com/shorts/xxx` |
| **Instagram** | `instagram.com/reel/xxx`, `instagram.com/p/xxx`, `instagram.com/tv/xxx` |

---

## 🛠️ Requisitos

### 1. FFmpeg (Obligatorio)
Herramienta indispensable para el procesamiento de audio.

- **Windows**: Descarga desde [gyan.dev](https://www.gyan.dev/ffmpeg/builds/), extrae el archivo y añade la carpeta `bin` a las **Variables de Entorno (PATH)** del sistema.
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt update && sudo apt install ffmpeg`

### 2. Python 3.8+
Asegúrate de tener instalada una versión reciente de Python.

---

## 🚀 Instalación y Uso

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/SrCidm/Transcriptor.git
   cd Transcriptor
   ```

2. **Crea y activa un entorno virtual:**
   ```bash
   # Crear el entorno
   python -m venv .venv

   # Activar en Windows (CMD/PowerShell)
   .\.venv\Scripts\activate

   # Activar en macOS/Linux
   source .venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta el script:**
   ```bash
   python Transcriptor.py
   ```

---

## 📋 Menú Principal

```
=======================================================
      TRANSCRIPTOR: Audio, YouTube & Instagram
=======================================================
1. Transcribir audio local
2. Transcribir desde URL (YouTube/Instagram)
3. Configurar cookies del navegador
4. Configurar formato de salida
5. Configurar carpeta de destino
6. Salir

   [CONFIG]
   - Formato: BOTH
   - Carpeta: textos/
```

---

## 📄 Formatos de Salida

| Archivo | Contenido | Uso |
|---------|-----------|-----|
| `nombre_limpio.txt` | Texto corrido sin timestamps | Copiar/pegar fácilmente |
| `nombre_timestamps.txt` | `[00.00s -> 05.32s] Texto` | Referencia temporal |
| `nombre_parrafos.txt` | Texto dividido por pausas | Lectura natural |

### Ejemplo de salida

**`_limpio.txt`**
```
Hola qué tal bienvenidos a este video hoy vamos a hablar sobre inteligencia artificial es un tema muy interesante...
```

**`_parrafos.txt`**
```
Hola qué tal bienvenidos a este video hoy vamos a hablar sobre inteligencia artificial.

Es un tema muy interesante que está cambiando el mundo.

Vamos a ver los puntos más importantes...
```

**`_timestamps.txt`**
```
[00.00s -> 02.34s] Hola qué tal bienvenidos a este video
[02.34s -> 05.67s] hoy vamos a hablar sobre inteligencia artificial
[05.67s -> 08.90s] es un tema muy interesante
```

---

## 🍪 Cookies del Navegador

Las cookies permiten acceder a contenido privado o con restricciones usando tu sesión del navegador.

| Situación | ¿Necesitas cookies? |
|-----------|---------------------|
| Video público de YouTube | No |
| Reel público de Instagram | No |
| Video +18 de YouTube | Sí |
| Reel de cuenta privada (que sigues) | Sí |
| Stories de Instagram | Sí |

**Navegadores soportados:** Chrome, Firefox, Edge, Brave, Opera, Safari

---

## 📖 Modelos de Whisper

| Modelo | Parámetros | Velocidad | Precisión |
|:-------|:----------:|:---------:|:----------|
| `tiny` | 39 M | ~32x | Básica |
| `base` | 74 M | ~16x | Buena |
| `small` | 244 M | ~6x | Muy Buena |
| `medium` | 769 M | ~2x | Excelente |
| `large` | 1550 M | 1x | Máxima |

> **Nota:** La velocidad es relativa al modelo `large`. Un número mayor significa más rápido.

---

## 🎵 Formatos de Audio Soportados

Whisper (a través de FFmpeg) soporta prácticamente cualquier formato:

```
mp3, wav, m4a, flac, ogg, opus, wma, aac, webm, mp4, mkv, avi...
```

Incluyendo **notas de voz de WhatsApp** (`.opus`, `.ogg`).

---

## 📁 Estructura de Archivos

```
Transcriptor/
├── Transcriptor.py
├── requirements.txt
├── README.md
└── textos/                    # Carpeta de salida (se crea automáticamente)
    ├── video1_limpio.txt
    ├── video1_timestamps.txt
    ├── video1_parrafos.txt
    └── ...
```

---

## ⚠️ Solución de Problemas

### Error de Instagram
```
[TIP] Intenta usar cookies del navegador (opción 3 en el menú)
```
- Asegúrate de que el contenido sea **público**
- Actualiza yt-dlp: `pip install -U yt-dlp`
- Usa cookies si el contenido es privado

### Error de codificación (emojis)
Si ves errores de `UnicodeEncodeError`, ejecuta:
```bash
chcp 65001
python Transcriptor.py
```

### Modelo no descarga
Los modelos se descargan automáticamente la primera vez. Asegúrate de tener conexión a internet.

---

## 📝 Dependencias

```
openai-whisper
torch
yt-dlp
tiktoken
```

Instalar con:
```bash
pip install openai-whisper torch yt-dlp tiktoken
```

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Abre un issue o pull request en el repositorio.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.

---

<p align="center">
  Desarrollado con ❤️ por <a href="https://github.com/SrCidm">SrCidm</a>
</p>