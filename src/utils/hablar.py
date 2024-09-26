import pyttsx3

def createVoice(rate=130, volume=1 ):
    voz = pyttsx3.init()
    voz.setProperty('rate', rate)  
    voz.setProperty('volume', volume)  
    return voz

def hablar(voz, texto="hola, soy ADA"):
    voz.say(texto)
    voz.runAndWait() 

if __name__ == "__main__":
    voz = createVoice()
    hablar(voz)
else:
    pass