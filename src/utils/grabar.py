import pyaudio
import wave
import keyboard

    
def grabar():
    stop= True
    audio = pyaudio.PyAudio()
    #datos genericos (no tocar)
    stream = audio.open(channels=1, rate=44100, input=True, format=pyaudio.paInt16, frames_per_buffer=1024)
    frame= []
    try:
        while stop:
            data = stream.read(1024)
            frame.append(data)
            if not keyboard.is_pressed('space'):
                stop = False
    except  KeyboardInterrupt:
        pass
    
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    file = wave.open("./src/temp/input/record.wav",'wb')
    file.setnchannels(1)
    file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    file. setframerate(44100)
    file.writeframes(b''.join(frame))
    file.close()

if __name__ == '__main__':
    while True:
        if keyboard.is_pressed('space'):
            print("inicio")
            grabar()
            print("termino")