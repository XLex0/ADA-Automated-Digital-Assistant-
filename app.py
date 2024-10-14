import src.utils.transcripcion as write
import src.utils.hablar as talk
import src.utils.procesarTexto as think
import src.utils.grabar as listen
import src.controller as exec
from src.instruction.verificar import conexion
import env.load as pmts

import keyboard
import time
import os


if __name__ == "__main__":
    
    parameters = pmts.load() # cargamos los parámetros 
    instructions = pmts.load(parameters['INSTRUCTION_PATH']) # cargamos las instrucciones
    
    modelo = write.cargar_modelo(parameters['MODELO'])
    voz = talk.createVoice(parameters['RATE'], parameters['VOLUME'])
    nlp = think.crearProcessing()
    
    if(conexion()):
        pass

    while True: 
        time.sleep(0.1)
        if keyboard.is_pressed('space') and keyboard.is_pressed('m'):
            # TODO: Quitar en producción
            print("inicio a hablar")
            listen.grabar()
        else:
            
            if os.path.exists(parameters['RUTA']):
                texto_transcrito = write.transcribir_audio(modelo, parameters['RUTA'])
                print(texto_transcrito)
                
                instruccion = think.startProcess(nlp, texto_transcrito)
                print(instruccion)
                print(type(instruccion))
                
                message = exec.ejecutarComando(instruccion, instructions, texto_transcrito)
                
                talk.hablar(voz, message)
                
                os.remove(parameters['RUTA'])
                

            else:
                pass

                         
         

        
       

        
    