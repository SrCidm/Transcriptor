import os
import whisper
import torch
from yt_dlp import YoutubeDL

def transcribe_audio(file_path, output_txt, model_name="base"):
    try:
        # Detectar si hay GPU disponible (NVIDIA)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"🚀 Usando dispositivo: {device.upper()}")

        print(f"⏳ Cargando modelo Whisper ({model_name})...")
        model = whisper.load_model(model_name, device=device)
        
        print(f"🎙️ Transcribiendo: {file_path}...")
        # Whisper detecta el idioma automáticamente si no se especifica
        result = model.transcribe(file_path, verbose=False)
        
        print(f"✅ Idioma detectado: {result.get('language', 'desconocido')}")

        # Guardar la transcripción con formato limpio
        with open(output_txt, "w", encoding="utf-8") as f:
            for segment in result["segments"]:
                start = segment['start']
                end = segment['end']
                text = segment['text'].strip()
                f.write(f"[{start:05.2f}s -> {end:05.2f}s] {text}\n")
        
        print(f"💾 Transcripción guardada con éxito en: {output_txt}")
    
    except Exception as e:
        print(f"❌ Error al transcribir: {e}")

def download_and_transcribe_youtube(url, output_txt, model_name="base"):
    audio_file = "temp_youtube_audio.mp3"
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'temp_youtube_audio', # Nombre base sin extensión
            'quiet': True,
            'no_warnings': True,
        }
        
        print("📥 Descargando audio de YouTube...")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # El archivo real puede terminar siendo .mp3 tras el postprocesador
        if not os.path.exists(audio_file):
             audio_file = "temp_youtube_audio.mp3"

        transcribe_audio(audio_file, output_txt, model_name)
        
    except Exception as e:
        print(f"❌ Error en YouTube: {e}")
    finally:
        if os.path.exists(audio_file):
            os.remove(audio_file)
            print("🧹 Archivo temporal eliminado.")

def main():
    valid_models = ["tiny", "base", "small", "medium", "large"]
    
    while True:
        print("\n---  TRANSCRIPTOR ---")
        print("1. Transcribir audio local")
        print("2. Transcribir video de YouTube")
        print("3. Salir")
        
        choice = input("\nSelecciona opción: ")
        
        if choice == "3": break
        if choice not in ["1", "2"]: continue

        model_name = input(f"Modelo ({', '.join(valid_models)}) [default: base]: ") or "base"
        if model_name not in valid_models:
            print("Modelo no válido.")
            continue

        output_txt = input("Nombre del archivo de salida (ej: resultado.txt): ")
        if not output_txt.endswith(".txt"): output_txt += ".txt"

        if choice == "1":
            file_path = input("Ruta del archivo de audio: ").strip('"') # Limpia comillas si arrastran el archivo
            if os.path.exists(file_path):
                transcribe_audio(file_path, output_txt, model_name)
            else:
                print("El archivo no existe.")
        
        elif choice == "2":
            url = input("URL de YouTube: ")
            download_and_transcribe_youtube(url, output_txt, model_name)

if __name__ == "__main__":
    main()