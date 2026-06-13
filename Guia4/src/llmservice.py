import os
import json
from typing import Dict
from groq import Groq
from perguntadiscursiva import PerguntaDiscursiva

class LLMService:
    def __init__(self, api_key: str = None, model: str = "llama-3.3-70b-versatile", groq_obj: Groq = None):
        self.api_key = api_key or os.environ.get("GROQ_API_KEY")
        self.model = model
        self.groq_obj = groq_obj or (Groq(api_key=self.api_key) if self.api_key else None)

    def fazer_chamada_api(self, prompt: str) -> str:
        if not isinstance(prompt, str):
            raise TypeError("Erro na entrada de dados. O prompt deve ser uma string.")
        
        if not self.groq_obj:
            raise ValueError("Cliente Groq não foi inicializado. Verifique a API Key.")

        response = self.groq_obj.chat.completions.create(
            model=self.model,
            temperature=0.0,  
            messages=[
                {"role": "system", "content": "Você é um professor avaliador. Responda APENAS com um JSON estruturado."},
                {"role": "user", "content": prompt},
            ]
        )
        return response.choices[0].message.content

    