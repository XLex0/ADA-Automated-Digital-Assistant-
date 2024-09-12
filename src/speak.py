import pyttsx3

def create_voice(velocidad, voz):
    voice = pyttsx3.init()
    list_voice = voice.getProperty('voices')
    
    voice.setProperty('rate', velocidad)
    voice.setProperty('voice', list_voice[voz].id)
    
    return voice

def speak(text, voice):
    voice.say(text)
    voice.runAndWait()

