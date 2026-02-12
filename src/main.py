import os
import whisper
import sounddevice as sd
from openai import OpenAI
from scipy.io.wavfile import write
from gtts import gTTS
import playsound
import time

# 1. CONFIGURAÇÕES INICIAIS E AUTENTICAÇÃO
linguagem = 'pt'
CHAVE_API = "SUA_CHAVE_AQUI" # Mantenha sua chave aqui para o teste local

# Criando o cliente da OpenAI
client = OpenAI(api_key=CHAVE_API)

# Carrega o modelo do Whisper
print("Carregando modelo Whisper... (Isso pode levar alguns segundos)")
modelo_whisper = whisper.load_model("small")

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

def assistente_virtual():
    # PASSO 1: GRAVAÇÃO
    arquivo_voz = gravar_audio(5)

    # PASSO 2: TRANSCRIÇÃO (VOZ -> TEXTO)
    print("Transcrevendo com Whisper...")
    resultado = modelo_whisper.transcribe(arquivo_voz, fp16=False, language=linguagem)
    texto_usuario = resultado["text"]
    print(f"Você disse: {texto_usuario}")

    if not texto_usuario.strip():
        print("Não foi possível entender o áudio. Tente falar mais perto do microfone.")
        return

    # PASSO 3: INTELIGÊNCIA (TEXTO -> RESPOSTA)
    print("Consultando ChatGPT...")
    try:
        resposta = client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[
                {"role": "system", "content": "Você é um assistente de voz prestativo e responde de forma curta e objetiva."},
                {"role": "user", "content": texto_usuario}
            ]
        )
        texto_resposta = resposta.choices[0].message.content
        print(f"IA: {texto_resposta}")

        # PASSO 4: SÍNTESE DE VOZ (TEXTO -> VOZ)
        print("Gerando áudio de resposta...")
        nome_resposta = "response.mp3"
        
        # Remove o arquivo anterior se existir para evitar erro de permissão do playsound
        if os.path.exists(nome_resposta):
            os.remove(nome_resposta)
            
        gtts_obj = gTTS(text=texto_resposta, lang=linguagem, slow=False)
        gtts_obj.save(nome_resposta)
        
        # PASSO 5: REPRODUÇÃO
        playsound.playsound(nome_resposta)

    except Exception as e:
        print(f"Ocorreu um erro na API da OpenAI: {e}")

if __name__ == "__main__":
    assistente_virtual()
