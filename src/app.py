import os
import sounddevice as sd
from scipy.io.wavfile import write
from gtts import gTTS
import playsound
from config import LINGUAGEM
from agente import processar_audio_para_texto, buscar_resposta_ia

def gravar_audio(segundos=5, nome_arquivo="request_audio.wav"):
    """Passo 1: Captura áudio do microfone"""
    fs = 44100
    print(f"Ouvindo por {segundos} segundos...")
    gravacao = sd.rec(int(segundos * fs), samplerate=fs, channels=1)
    sd.wait()
    write(nome_arquivo, fs, gravacao)
    return nome_arquivo

def falar(texto):
    """Passo 4 e 5: Síntese e Reprodução"""
    nome_resposta = "response.mp3"
    if os.path.exists(nome_resposta):
        os.remove(nome_resposta)
    
    gtts_obj = gTTS(text=texto, lang=LINGUAGEM, slow=False)
    gtts_obj.save(nome_resposta)
    playsound.playsound(nome_resposta)

def executar_assistente():
    try:
        # Execução do fluxo
        arquivo_voz = gravar_audio(5)
        
        texto_usuario = processar_audio_para_texto(arquivo_voz, LINGUAGEM)
        print(f"Você disse: {texto_usuario}")

        if texto_usuario.strip():
            texto_ia = buscar_resposta_ia(texto_usuario)
            print(f"IA: {texto_ia}")
            falar(texto_ia)
        else:
            print("Áudio não compreendido.")

    except Exception as e:
        print(f"Erro no sistema: {e}")

if __name__ == "__main__":
    executar_assistente()
