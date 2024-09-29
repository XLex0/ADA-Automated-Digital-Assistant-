import os


def openF(ruta,original):
    try:
        os.startfile(ruta)
    except Exception as e:
        print(f"No se pudo abrir el Archivo: {e}")
        

if __name__=='__main__':
    pass
        