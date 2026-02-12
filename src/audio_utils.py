import os
import sounddevice as sd
from scipy.io.wavfile import write
from gtts import gTTS
import playsound

def gravar_audio(segundos=5, nome_arquivo="request_audio.wav"):
    """Captura áudio do microfone do PC"""
    fs = 44100  # Frequência de amostragem
    print(f"Ouvindo por {segundos} segundos...")
    
    # Grava os dados do microfone
    gravacao = sd.rec(int(segundos * fs), samplerate=fs, channels=1)
    sd.wait()  # Espera a gravação terminar
    
    # Salva o arquivo no disco
    write(nome_arquivo, fs, gravacao)
    return nome_arquivo

def gerar_e_reproduzir_voz(texto_resposta, linguagem='pt'):
    """Transforma texto em áudio e reproduz"""
    print("Gerando áudio de resposta...")
    nome_resposta = "response.mp3"
    
    # Remove o arquivo anterior se existir
    if os.path.exists(nome_resposta):
        os.remove(nome_resposta)
        
    gtts_obj = gTTS(text=texto_resposta, lang=linguagem, slow=False)
    gtts_obj.save(nome_resposta)
    
    # Reprodução
    playsound.playsound(nome_resposta)
