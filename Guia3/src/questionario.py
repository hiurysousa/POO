from typing import List, Tuple, Dict
from tentativaquestionario import TentativaQuestionario 

class Questionario:
    def __init__(self, titulo):
        self._titulo = titulo
        self._perguntas = []

    def adicionar_pergunta(self, pergunta):
        self._perguntas.append(pergunta)

    def criar_attempt(self, usuario):
        return TentativaQuestionario(usuario)