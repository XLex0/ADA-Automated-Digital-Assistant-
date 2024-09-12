import whisper

def create_model(modelo):
    try:
        audio_recognizer = whisper.load_model(modelo)
        return audio_recognizer
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        return None

def transcribe_audio(audio_recognizer, ruta, lengua, fp=False):
    try:
        transcripcion = audio_recognizer.transcribe(ruta, language=lengua, fp16=fp)
        return transcripcion['text']
    except FileNotFoundError:
        print(f"El archivo de audio '{ruta}' no se encuentra.")
    except Exception as e:
        print(f"Error durante la transcripción: {e}")
    return None
