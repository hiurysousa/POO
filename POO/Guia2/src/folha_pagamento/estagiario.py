from folha_pagamento.funcionario import Funcionario

class Estagiario(Funcionario):
    def __init__(self, nome, matricula, salario_base, curso, carga_horaria):
        super().__init__(nome, matricula, salario_base)
        self.curso = curso
        self.carga_horaria = carga_horaria

    def calcular_bonus(self) -> float:
        return (self.salario_base * 0.03)

    def calcular_descontos(self) -> float:
        return (self.salario_base * 0.02)

    def calcular_adicionais(self) -> float:
        if self.carga_horaria <= 20:
            return 150
        elif self.carga_horaria <= 30:
            return 250
        else:
            return 350