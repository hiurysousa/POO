from typing import List, Tuple, Dict
from resposta import Resposta

class RespostaObjetiva(Resposta):
    def __init__(self, indice_escolhido, alternativa_selecionada = None):
        self._indice_escolhido = indice_escolhido
        self._alternativa_selecionada = alternativa_selecionada
    