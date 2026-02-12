import whisper
from openai import OpenAI
from config import CHAVE_API

# Inicialização dos modelos
client = OpenAI(api_key=CHAVE_API)
print("Carregando modelo Whisper...")
modelo_whisper = whisper.load_model("small")

def processar_audio_para_texto(caminho_audio, linguagem='pt'):
    """Passo 2: Transcrição (Voz -> Texto)"""
    print("Transcrevendo com Whisper...")
    resultado = modelo_whisper.transcribe(caminho_audio, fp16=False, language=linguagem)
    return resultado["text"]

def buscar_resposta_ia(texto_usuario):
    """Passo 3: Inteligência (Texto -> Resposta)"""
    print("Consultando GPT...")
    resposta = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "system", "content": "Você é um assistente de voz prestativo e responde de forma curta e objetiva."},
            {"role": "user", "content": texto_usuario}
        ]
    )
    return resposta.choices[0].message.content
