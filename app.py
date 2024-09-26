import src.utils.transcripcion as write
import src.utils.hablar as talk
import src.utils.procesarTexto as think
import src.utils.grabar as listen

import env.loadParameters as pmts

import keyboard
import time


if __name__ == "__main__":
    
    parameters = pmts.load() # cargamos los parámetros 
    
    modelo = write.cargar_modelo(parameters['MODELO'])
    voz = talk.createVoice(parameters['RATE'], parameters['VOLUME'])
    

    while True: 
        time.sleep(0.1)
        if keyboard.is_pressed('space') and keyboard.is_pressed('m'):
            print("inicio a hablar")
            listen.grabar()
        else:
            pass               
         

        
       

        
    