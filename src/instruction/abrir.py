import os
import load as inst

def openF(ruta):
    try:
        os.startfile(ruta)
    except Exception as e:
        print(f"No se pudo abrir el Archivo: {e}")
        

if __name__=='__main__':
    instruction = inst.load("./env/instructions.json")
    
    try:
        openF(instruction['poder']['abrir']['wo'])
        
    except KeyError:
        print('error Key not valid')
        
else:
    pass
    