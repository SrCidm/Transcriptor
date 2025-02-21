import os
import whisper
from yt_dlp import YoutubeDL

def transcribe_audio(file_path, output_txt, model_name="base"):
    try:
        # Cargar el modelo de Whisper según la elección del usuario
        model = whisper.load_model(model_name)
        
        # Cargar el audio y detectar el idioma
        audio = whisper.load_audio(file_path)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        
        # Detectar el idioma
        _, probs = model.detect_language(mel)
        detected_language = max(probs, key=probs.get)
        print(f"Idioma detectado: {detected_language}")
        
        # Transcribir el archivo de audio en el idioma detectado
        result = model.transcribe(file_path, language=detected_language)
        
        # Guardar la transcripción en un archivo txt con formato
        with open(output_txt, "w", encoding="utf-8") as f:
            for segment in result["segments"]:
                f.write(f"[{segment['start']:.2f}s -> {segment['end']:.2f}s] {segment['text']}\n\n")
        
        print(f"Transcripción guardada en {output_txt}")
    
    except Exception as e:
        print(f"Error al transcribir el archivo: {e}")

def download_and_transcribe_youtube(url, output_txt, model_name="base"):
    try:
        # Configurar yt_dlp para extraer solo el audio
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'temp_audio',  # Nombre temporal del archivo de audio
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # El archivo descargado tendrá la extensión .mp3
        audio_file = "temp_audio.mp3"
        
        # Transcribir el archivo de audio
        transcribe_audio(audio_file, output_txt, model_name)
        
        # Eliminar el archivo temporal
        os.remove(audio_file)
        print(f"Archivo temporal {audio_file} eliminado.")
    
    except Exception as e:
        print(f"Error al descargar o transcribir el video de YouTube: {e}")

def main():
    valid_models = ["tiny", "base", "small", "medium", "large"]
    
    while True:
        print("Menú:")
        print("1. Transcribir un archivo de audio local")
        print("2. Transcribir un video de YouTube")
        print("3. Salir")
        
        choice = input("Selecciona una opción (1/2/3): ")
        
        if choice == "1":
            file_path = input("Introduce la ruta del archivo de audio: ")
            if not os.path.exists(file_path):
                print("Error: El archivo no existe.")
                continue
            
            output_txt = input("Introduce el nombre del archivo de salida (txt): ")
            model_name = input("Introduce el modelo de Whisper que deseas usar (tiny, base, small, medium, large): ")
            
            if model_name not in valid_models:
                print(f"Error: Modelo no válido. Debe ser uno de: {', '.join(valid_models)}")
                continue
            
            transcribe_audio(file_path, output_txt, model_name)
        
        elif choice == "2":
            url = input("Introduce el enlace del video de YouTube: ")
            output_txt = input("Introduce el nombre del archivo de salida (con .txt): ")
            model_name = input("Introduce el modelo de Whisper que deseas usar (tiny, base, small, medium, large): ")
            
            if model_name not in valid_models:
                print(f"Error: Modelo no válido. Debe ser uno de: {', '.join(valid_models)}")
                continue
            
            download_and_transcribe_youtube(url, output_txt, model_name)
        
        elif choice == "3":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

if __name__ == "__main__":
    main()