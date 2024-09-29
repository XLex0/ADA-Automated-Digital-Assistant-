import re

def eliminar_hasta(patron, original):
    regex = rf'.*?\b({patron}\w*)'
    resultado = re.search(regex, original)
    if resultado:
            match= resultado.group(0)+" "
            modificado = original.replace(match, "").rstrip('.').replace(" ", "+")
            
            return modificado
    return original

if __name__ == '__main__':
        pass