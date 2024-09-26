import src.utils.transcripcion as write
import src.utils.hablar as talk
import src.utils.procesarTexto as think
import src.utils.grabar as listen

import env.loadParameters as pmts

if __name__ == "__main__":
    
    parameters = pmts.load() # cargamos los parámetros 
    
    modelo = write.cargar_modelo(parameters['MODELO'])
    voz = talk.createVoice(parameters['RATE'], parameters['VOLUME'])
    
    archivo_audio = r".\src\temp\input\Grabación.wav"  # Cambia esto por tu ruta de archivo
    texto_transcrito = write.transcribir_audio(modelo, archivo_audio)
    
    # Mostrar el texto transcrito
    print("Texto transcrito:")
    print(texto_transcrito)