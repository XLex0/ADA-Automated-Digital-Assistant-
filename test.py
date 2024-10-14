
import src.utils.hablar as talk
import src.utils.procesarTexto as think
import src.controller as exec
import env.load as pmts


if __name__ == "__main__":
    
    parameters = pmts.load() # cargamos los parámetros 
    instructions = pmts.load(parameters['INSTRUCTION_PATH']) # cargamos las instrucciones
    
    voz = talk.createVoice(parameters['RATE'], parameters['VOLUME'])
    nlp = think.crearProcessing()

    while True:
        texto_transcrito= input("ingresa algo: ")

        instruccion = think.startProcess(nlp, texto_transcrito)
        print(instruccion)

                    
        message = exec.ejecutarComando(instruccion, instructions, texto_transcrito)
                    
        talk.hablar(voz, message)
                

                         
         

        
       

        
    