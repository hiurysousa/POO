from typing import List, Tuple, Dict
from abc import ABC, abstractmethod

class Pergunta(ABC):
    def __init__(self, texto, explicacao_geral = None):
        self._texto = texto
        self._explicacao_geral = explicacao_geral

    @abstractmethod
    def validar_resposta(resposta):
        pass

    @property
    def get_explicacao(self):
        return self._explicacao_geral
    
    @property
    def get_tipo(self):
        return self.get_tipo