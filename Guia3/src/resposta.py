from typing import List, Tuple, Dict
from abc import ABC, abstractmethod

class Resposta(ABC):
    def __init__(self, pergunta, esta_correta, pontuacao_obtida):
        self._pergunta = pergunta 
        self._esta_correta = esta_correta
        self._pontuacao_obtida = pontuacao_obtida

    @abstractmethod
    def calcular_pontuacao(self):
        return self._pontuacao_obtida