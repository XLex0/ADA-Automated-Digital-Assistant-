import json
import os

def load(ruta_json='env\params.json'):
    with open(ruta_json, 'r') as archivo_json:
        config = json.load(archivo_json)
        return config
    
if __name__ == '__main__':
    config = load()
    
    # Imprimir el tipo de objeto (será un diccionario)
    print("Tipo de objeto:", type(config))
    
    # Imprimir el diccionario completo de manera legible
    print("Contenido del diccionario:")
    print(json.dumps(config, indent=4))