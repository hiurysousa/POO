from typing import List, Tuple, Dict
from pergunta import Pergunta

class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self):
        self._alternativas = []

    def validar_resposta(self, indice):
        if self._alternativas[indice]:
            return True
        return False

    @property
    def get_alternativa_correta(self):
        if self.validar_resposta:
            return self._alternativas