import whisper


def cargar_modelo(MODELO='small'):
    modelo = whisper.load_model(MODELO, )  
    return modelo

def transcribir_audio(modelo, archivo_audio,  LANGUAGE= 'Spanish', FP16=False):
    resultado = modelo.transcribe(archivo_audio, language= LANGUAGE, fp16 = FP16)
    return resultado['text']

if __name__ == "__main__":
    
    # MODELO = "seleccionar Modelo"
    modelo = cargar_modelo()
    
    # Especificar el archivo de audio a transcribir
    archivo_audio = r".\src\temp\input\record.wav"  # Cambia esto por tu ruta de archivo
    texto_transcrito = transcribir_audio(modelo, archivo_audio)
    
    # Mostrar el texto transcrito
    print("Texto transcrito:")
    print(texto_transcrito)
else:
    pass