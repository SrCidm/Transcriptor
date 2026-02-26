import os
import re
import whisper
import torch
from yt_dlp import YoutubeDL

def detect_url_type(url):
    """Detecta si la URL es de YouTube o Instagram."""
    youtube_patterns = [
        r'(youtube\.com|youtu\.be)',
        r'youtube\.com/watch',
        r'youtube\.com/shorts',
        r'youtu\.be/'
    ]
    
    instagram_patterns = [
        r'instagram\.com/p/',
        r'instagram\.com/reel/',
        r'instagram\.com/tv/',
        r'instagr\.am/'
    ]
    
    for pattern in youtube_patterns:
        if re.search(pattern, url):
            return 'youtube'
    
    for pattern in instagram_patterns:
        if re.search(pattern, url):
            return 'instagram'
    
    return None

def transcribe_audio(file_path, output_base, model_name="base", output_format="both"):
    """
    Transcribe audio y guarda segun el formato elegido.
    output_format: 'timestamps', 'clean', 'both'
    """
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"[INFO] Usando dispositivo: {device.upper()}")

        print(f"[INFO] Cargando modelo Whisper ({model_name})...")
        model = whisper.load_model(model_name, device=device)
        
        print(f"[INFO] Transcribiendo: {file_path}...")
        result = model.transcribe(file_path, verbose=False)
        
        language = result.get('language', 'desconocido')
        print(f"[OK] Idioma detectado: {language}")

        # Preparar nombres de archivo
        base_name = output_base.replace('.txt', '')
        
        # Formato con timestamps
        if output_format in ['timestamps', 'both']:
            timestamps_file = f"{base_name}_timestamps.txt"
            with open(timestamps_file, "w", encoding="utf-8") as f:
                f.write(f"Transcripcion con marcas de tiempo\n")
                f.write(f"Idioma: {language}\n")
                f.write("=" * 50 + "\n\n")
                for segment in result["segments"]:
                    start = segment['start']
                    end = segment['end']
                    text = segment['text'].strip()
                    f.write(f"[{start:05.2f}s -> {end:05.2f}s] {text}\n")
            print(f"[GUARDADO] Con timestamps: {timestamps_file}")
        
        # Formato limpio (facil de copiar)
        if output_format in ['clean', 'both']:
            clean_file = f"{base_name}_limpio.txt"
            with open(clean_file, "w", encoding="utf-8") as f:
                full_text = result['text'].strip()
                f.write(full_text)
            print(f"[GUARDADO] Texto limpio: {clean_file}")
        
        # Formato parrafos (agrupa por pausas)
        if output_format == 'both':
            paragraphs_file = f"{base_name}_parrafos.txt"
            with open(paragraphs_file, "w", encoding="utf-8") as f:
                current_paragraph = []
                last_end = 0
                
                for segment in result["segments"]:
                    start = segment['start']
                    text = segment['text'].strip()
                    
                    # Si hay pausa mayor a 2 segundos, nuevo parrafo
                    if start - last_end > 2.0 and current_paragraph:
                        f.write(" ".join(current_paragraph) + "\n\n")
                        current_paragraph = []
                    
                    current_paragraph.append(text)
                    last_end = segment['end']
                
                # Ultimo parrafo
                if current_paragraph:
                    f.write(" ".join(current_paragraph))
            
            print(f"[GUARDADO] Con parrafos: {paragraphs_file}")
    
    except Exception as e:
        print(f"[ERROR] Al transcribir: {e}")

def select_browser_for_cookies():
    """Permite seleccionar el navegador para extraer cookies."""
    print("\n[COOKIES] Usar cookies del navegador? (util para contenido privado)")
    print("0. No usar cookies")
    print("1. Chrome")
    print("2. Firefox")
    print("3. Edge")
    print("4. Brave")
    print("5. Opera")
    print("6. Safari (macOS)")
    
    choice = input("\nSelecciona [default: 0]: ").strip() or "0"
    
    browsers = {
        "0": None,
        "1": "chrome",
        "2": "firefox",
        "3": "edge",
        "4": "brave",
        "5": "opera",
        "6": "safari"
    }
    
    return browsers.get(choice, None)

def select_output_format():
    """Permite seleccionar el formato de salida."""
    print("\n[FORMATO] Formato de salida:")
    print("1. Solo texto limpio (facil de copiar)")
    print("2. Solo con timestamps")
    print("3. Ambos formatos + parrafos (recomendado)")
    
    choice = input("\nSelecciona [default: 3]: ").strip() or "3"
    
    formats = {
        "1": "clean",
        "2": "timestamps",
        "3": "both"
    }
    
    return formats.get(choice, "both")

def download_audio_from_url(url, platform, browser_cookies=None):
    """Descarga el audio de YouTube o Instagram."""
    audio_file = "temp_audio.mp3"
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'temp_audio',
        'quiet': True,
        'no_warnings': True,
    }
    
    if browser_cookies:
        ydl_opts['cookiesfrombrowser'] = (browser_cookies,)
        print(f"[COOKIES] Usando cookies de: {browser_cookies.upper()}")
    
    if platform == 'instagram':
        print("[INFO] Descargando audio de Instagram...")
    else:
        print("[INFO] Descargando audio de YouTube...")
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        if os.path.exists(audio_file):
            return audio_file
        
        for ext in ['mp3', 'm4a', 'webm', 'wav', 'opus']:
            alt_file = f"temp_audio.{ext}"
            if os.path.exists(alt_file):
                return alt_file
        
        print("[ERROR] No se pudo encontrar el archivo de audio descargado")
        return None
        
    except Exception as e:
        print(f"[ERROR] Al descargar: {e}")
        
        if platform == 'instagram' and not browser_cookies:
            print("\n[TIP] Intenta usar cookies del navegador (opcion 3 en el menu)")
        
        return None

def download_and_transcribe_url(url, output_txt, model_name="base", browser_cookies=None, output_format="both"):
    """Descarga y transcribe audio de YouTube o Instagram."""
    
    platform = detect_url_type(url)
    
    if platform is None:
        print("[ERROR] URL no reconocida. Debe ser de YouTube o Instagram.")
        print("\nURLs validas:")
        print("   YouTube:   youtube.com/watch?v=xxx | youtu.be/xxx | youtube.com/shorts/xxx")
        print("   Instagram: instagram.com/reel/xxx | instagram.com/p/xxx")
        return
    
    print(f"[OK] Plataforma detectada: {platform.upper()}")
    
    audio_file = download_audio_from_url(url, platform, browser_cookies)
    
    if audio_file is None:
        return
    
    try:
        transcribe_audio(audio_file, output_txt, model_name, output_format)
    finally:
        if os.path.exists(audio_file):
            os.remove(audio_file)
            print("[INFO] Archivo temporal eliminado.")

def main():
    valid_models = ["tiny", "base", "small", "medium", "large"]
    browser_cookies = None
    output_format = "both"
    
    while True:
        print("\n" + "=" * 50)
        print("   TRANSCRIPTOR: Audio, YouTube & Instagram")
        print("=" * 50)
        print("1. Transcribir audio local")
        print("2. Transcribir desde URL (YouTube/Instagram)")
        print("3. Configurar cookies del navegador")
        print("4. Configurar formato de salida")
        print("5. Salir")
        
        # Mostrar configuracion actual
        config_str = f"\n   [CONFIG] Formato: {output_format.upper()}"
        if browser_cookies:
            config_str += f" | Cookies: {browser_cookies.upper()}"
        print(config_str)
        
        choice = input("\nSelecciona opcion: ").strip()
        
        if choice == "5": 
            print("\nBai bai!")
            break
        
        if choice == "3":
            browser_cookies = select_browser_for_cookies()
            if browser_cookies:
                print(f"[OK] Cookies de {browser_cookies.upper()} activadas")
            else:
                print("[OK] Cookies desactivadas")
            continue
        
        if choice == "4":
            output_format = select_output_format()
            print(f"[OK] Formato cambiado a: {output_format.upper()}")
            continue
        
        if choice not in ["1", "2"]: 
            print("[ERROR] Opcion no valida")
            continue

        # Seleccion de modelo
        print(f"\n[MODELOS] Disponibles: {', '.join(valid_models)}")
        model_name = input("Modelo [default: base]: ").strip() or "base"
        if model_name not in valid_models:
            print("[ERROR] Modelo no valido.")
            continue

        # Nombre del archivo de salida
        output_txt = input("Nombre base del archivo [default: transcripcion]: ").strip()
        if not output_txt: 
            output_txt = "transcripcion"
        output_txt = output_txt.replace('.txt', '')

        # Procesar segun la opcion
        if choice == "1":
            file_path = input("Ruta del archivo de audio: ").strip('"')
            if os.path.exists(file_path):
                transcribe_audio(file_path, output_txt, model_name, output_format)
            else:
                print("[ERROR] El archivo no existe.")
        
        elif choice == "2":
            url = input("URL (YouTube o Instagram): ").strip()
            download_and_transcribe_url(url, output_txt, model_name, browser_cookies, output_format)

if __name__ == "__main__":
    main()