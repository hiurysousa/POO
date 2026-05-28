from typing import List, Tuple, Dict

class Alternativa:
    def __init__(self, texto, correta, explicacao = None):
        self._texto = texto
        self._correta = correta
        self._explicacao = explicacao

    