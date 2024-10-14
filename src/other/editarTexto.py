import re

def eliminar_hasta(patron, original):
    regex = rf'.*?\b({patron}\w*)'
    resultado = re.search(regex, original)
    if resultado:
            match= resultado.group(0)+" "
            modificado = original.replace(match, "").rstrip('.').replace(" ", "+")
            
            return modificado
    return original

def crearTxt(*args):
    for i in args:
        with open("./src/temp/output/output.txt", 'a') as archivo:
                archivo.write(str(i)+"\n")
                

if __name__ == '__main__':
        crearTxt(10, 'Python', [1, 2, 3], True)