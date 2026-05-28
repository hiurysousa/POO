from typing import List, Tuple, Dict
from resposta import Resposta

class RespostaDiscursiva(Resposta):
    def __init__(self, texto_resposta):
        self._texto_resposta = texto_resposta