import socket
from src.other.editarTexto import crearTxt


def red():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return hostname, local_ip

def conexion():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False
    
def check(opcion, original):
    if opcion =="red":
        host, ip=red()
        internet=conexion()
        if (internet):       
            crearTxt(host, ip, internet)

        

