import tempfile
import os
from src.speak import speak, create_voice
from src.listen import create_listener, listen
from src.recognition import create_model, transcribe_audio

#PARAMETROS
SPEED_VOICE = 145
INDEX_VOICE = 0

MODEL = 'small'
LENGUAJE = 'spanish'


#creamos la voz 
voice = create_voice(SPEED_VOICE, INDEX_VOICE)

#creamos el listener
listener = create_listener()

#carpeta temporal
temp = tempfile.mkdtemp()
save_path = os.path.join(temp,'audio.wav')

#cargamos modelo de transcripcion
trascription_model = create_model(MODEL)