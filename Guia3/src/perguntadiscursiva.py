from typing import List, Tuple, Dict
from pergunta import Pergunta


class PerguntaDiscursiva(Pergunta):
    def __init__(self, case_sensitive:bool, resposta_esperada:str = None):
        self._case_sensitive = case_sensitive
        self._resposta_esperada = resposta_esperada

    def validar_resposta(self, texto):
        if texto in self._resposta_esperada:
            return True
        return False
