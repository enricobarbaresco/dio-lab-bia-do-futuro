import os
import sounddevice as sd
from scipy.io.wavfile import write
from gtts import gTTS
import playsound

def gravar_audio(segundos=5, nome_arquivo="request_audio.wav"):
    fs = 44100
    print(f"Ouvindo por {segundos} segundos...")
    gravacao = sd.rec(int(segundos * fs), samplerate=fs, channels=1)
    sd.wait()
    write(nome_arquivo, fs, gravacao)
    return nome_arquivo

def reproduzir_voz(texto, linguagem='pt'):
    nome_resposta = "response.mp3"
    if os.path.exists(nome_resposta):
        os.remove(nome_resposta)
    
    gtts_obj = gTTS(text=texto, lang=linguagem, slow=False)
    gtts_obj.save(nome_resposta)
    playsound.playsound(nome_resposta)
