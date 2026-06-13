import json
from typing import Dict
from perguntadiscursiva import PerguntaDiscursiva
from llmservice import LLMService

class Correcao:

    @staticmethod
    def corrigir_discursiva(pergunta: PerguntaDiscursiva, resposta_aluno: str, service: LLMService = None) -> Dict:
        if service is None:
            service = LLMService()
            
        prompt = Correcao.criar_prompt_correcao(pergunta, resposta_aluno)
        
        try:
            resposta_texto = service.fazer_chamada_api(prompt)
            return json.loads(resposta_texto)
        # No arquivo src/correcao.py, mude temporariamente para:
        except Exception as e:
            print(f"\n🚨 ERRO REAL DA API: {e}\n") # <-- Adicione essa linha para diagnosticar
            return {
                "correta": False,
                "pontuacao": 0.0,
                "feedback": "Erro na comunicação com o serviço de correção.",
                "explicacao": "Não foi possível validar a resposta no momento."
            }

    @staticmethod
    def criar_prompt_correcao(pergunta: PerguntaDiscursiva, resposta_aluno: str) -> str:
        return (
            "Avalie a resposta do aluno com base nos critérios fornecidos.\n"
            f"Enunciado da Questão: {pergunta.texto}\n"
            f"Resposta Esperada: {pergunta.resposta_esperada}\n"
            f"Resposta enviada pelo Aluno: {resposta_aluno}\n\n"
            "Retorne obrigatoriamente um formato JSON com as chaves exatas:\n"
            '{"correta": bool, "pontuacao": float, "feedback": "str", "explicacao": "str"}'
        )