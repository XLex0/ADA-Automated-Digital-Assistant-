import speech_recognition as sr
import io
from pydub import AudioSegment

def create_listener():
    listener = sr.Recognizer()
    return listener  

def listen(listener, ruta):
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            listener.adjust_for_ambient_noise(source)  
            audio = listener.listen(source) 

            # Convierte el audio en flujo de bytes y lo guarda como WAV
            data = io.BytesIO(audio.get_wav_data())
            clip = AudioSegment.from_file(data, format="wav")
            clip.export(ruta, format='wav') 
            print(f"Audio guardado en: {ruta}")
            return ruta

    except sr.RequestError as e:
        print(f"Error de solicitud a la API de reconocimiento: {e}")
    except sr.UnknownValueError:
        print("No entendí lo que dijiste")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None
