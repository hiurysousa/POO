from typing import List, Tuple, Dict

class TentativaQuestionario:
    def __init__(self, questionario, usuario, data_inicio = None, data_fim = None):
        self._questionario = questionario
        self._usuario = usuario
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self._respostas = []

    def registrar_resposta(self, indice_pergunta, valor):
        self._respostas.append(valor)

    def finalizar(self):
        pass

    def calcular_pontuacao(self):
        pass

    def is_finalizado(self):
        pass