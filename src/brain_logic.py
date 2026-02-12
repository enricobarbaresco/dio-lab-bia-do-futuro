import whisper
from openai import OpenAI

class AssistenteCerebro:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        print("Carregando modelo Whisper...")
        self.modelo_whisper = whisper.load_model("small")

    def transcrever(self, caminho_audio, linguagem='pt'):
        resultado = self.modelo_whisper.transcribe(caminho_audio, fp16=False, language=linguagem)
        return resultado["text"]

    def pedir_resposta(self, texto_usuario):
        resposta = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um assistente de voz prestativo e responde de forma curta e objetiva."},
                {"role": "user", "content": texto_usuario}
            ]
        )
        return resposta.choices[0].message.content
