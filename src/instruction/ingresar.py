
import os
from src.other.editarTexto import eliminar_hasta
import time

def select(url,buscar,original):

    if buscar==0:
        parametro=eliminar_hasta('bus',original)
        print(type(parametro))
        
        url = url+parametro
    time.sleep(0.1)
    os.system(f'start {url}')




