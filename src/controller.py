
'''
Se busca retornar mensajes del tipo
return [cod, audio, show]

cod: es un codigo de éxito 
audio: es el mensaje que responderá la voz
show: es el contenido que devuelve la función

'''
import src.other.microFuncionalidades as other
import subprocess

def cortarComando (listaComando):
    if 'poder' in listaComando:
        index_poder = listaComando.index('poder')
        listaComando = listaComando[index_poder:]
        return listaComando
    else:
        return [-1,'No se encontro la palabra de activación\
            , intenta repetir la instrucción con la frase inicial: \
                Hola, ¿cómo estás? ¿Puedes...?', '']
        
def crearComando (query, guia):
    a=list(guia.keys())  # tomamos las claves del diccionario y lo volvemos lista
    ruta = list(a) 
    adition = guia['base'] #comando base de ese diccionario
    print (ruta)
    for x in ruta:
        for y in query:
            if other.comparaLevenshtein(x,y)<=2 and x != 'base' and x != 'error':
                if type(guia[x])==dict:                         # en caso de que la clave asociada sea otro diccionario
                    plus,success=crearComando(query,guia[x])
                    if success == -1:
                        return plus, -1                         # en caso de haber ocurrido un error
                    adition = adition+plus[1]                     
                    return [plus[0],adition], 0                 
                else:
                    return [guia[x][0],adition+guia[x][1]], 0   # [voz, base+comando], successful
    else:
        if 'default' in guia:
            return [guia['default'][0],guia['default'][1]],0    # en caso de haber un comando por default
        
        return [guia['error'],guia['error']], -1                # si no lo encuentra
            

def ejecutarComando(query, diccionario,original):
    req = cortarComando(query)
    if req[0] == -1:
        return req[1]
    
    command,sucess = crearComando(req, diccionario)
    print ("python", "-c", command[1]+",\""+original+"\")")
    if sucess == 0:
        try:
            result = subprocess.run(
        ["python", "-c", command[1]+",\""+original+"\")"],
        stdout=subprocess.PIPE,  # Captura la salida estándar
        stderr=subprocess.PIPE,   # Captura los errores estándar (opcional)
        text=True                 # Decodifica la salida a texto
    )   
            print("Salida estándar:")
            print(result.stdout)
            
            

            if result.stderr:
                print("Errores:")
                print(result.stderr)
        except Exception:
            return "Error al abrir aplicación"
    return command[0]

    
    
    
    
    
if __name__ == '__main__':
   
    lista = ['poder','abrir','word','gmail']

else:
    pass