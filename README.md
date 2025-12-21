# 🎙️ Transcriptor: Audio & YouTube

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI Whisper](https://img.shields.io/badge/OpenAI-Whisper-412991?style=for-the-badge&logo=openai&logoColor=white)

Herramienta de línea de comandos para transcribir archivos de audio locales y videos de YouTube utilizando el modelo **Whisper** de OpenAI. Diseñado para ser rápido, preciso y fácil de usar.

---

## ✨ Características

- ✅ **Transcripción de Audio Local:** Soporta formatos comunes como MP3, WAV, M4A, FLAC, entre otros.
- ✅ **Soporte para YouTube:** Descarga automáticamente el audio de cualquier video de YouTube a partir de su URL.
- ✅ **Detección de Idioma:** Identifica automáticamente el idioma del audio.
- ✅ **Marcas de Tiempo:** Genera un archivo `.txt` con la transcripción y marcas de tiempo detalladas por segmento: `[00.00s -> 05.32s] Texto transcrito.`.
- ✅ **Aceleración por GPU:** Utiliza automáticamente núcleos **CUDA** de NVIDIA si están disponibles para acelerar la transcripción significativamente.

---

## 🛠️ Requisitos

### 1. FFmpeg (Obligatorio)
Herramienta indispensable para el procesamiento de audio.

- **Windows**: Descarga desde gyan.dev, extrae el archivo y añade la carpeta `bin` a las **Variables de Entorno (PATH)** del sistema.
- **macOS**: Instalar con Homebrew: `brew install ffmpeg`
- **Linux**: Instalar con el gestor de paquetes: `sudo apt update && sudo apt install ffmpeg`

### 2. Python 3.8+
Asegúrate de tener instalada una versión reciente de Python.

---

## 🚀 Instalación y Uso

1.  **Clona el repositorio:**
   ```bash
   git clone https://github.com/SrCidm/Transcriptor.git
   cd Transcriptor
   ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # Crear el entorno
    python -m venv .venv

    # Activar en Windows (CMD/PowerShell)
    .\.venv\Scripts\activate

    # Activar en macOS/Linux
    source .venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta el script:**
    ```bash
    python Transcriptor.py
    ```
    Sigue las instrucciones en la consola para elegir una opción, seleccionar un modelo y transcribir tu audio.

---

## 📖 Tabla de Modelos de Whisper

Puedes elegir diferentes modelos de Whisper, cada uno con un balance distinto entre velocidad y precisión.

| Modelo  | Parámetros | Velocidad Relativa | Precisión |
| :------ | :--------: | :----------------: | :-------- |
| `tiny`  |   39 M     |        ~32x        | Básica    |
| `base`  |   74 M     |        ~16x        | Buena     |
| `small` |   244 M    |        ~6x         | Muy Buena |
| `medium`|   769 M    |        ~2x         | Excelente |
| `large` |   1550 M   |         1x         | Máxima    |

**Nota:** La velocidad es relativa al modelo `large`. Un número mayor (ej. `32x`) significa que es más rápido.