from folha_pagamento.funcionario import Funcionario

class Desenvolvedor(Funcionario):
    def __init__(self, nome, matricula, salario_base, linguagem, senioridade):
        super().__init__(nome, matricula, salario_base)
        self.linguagem = linguagem
        self.senioridade = senioridade

    def calcular_bonus(self):
        if self.senioridade == 'junior':
            return (self.salario_base * 0.05)
        elif self.senioridade == 'pleno':
            return (self.salario_base * 0.1)
        elif self.senioridade == 'senior':
            return (self.salario_base * 0.15)

    def calcular_descontos(self):
        return (self.salario_base * 0.08)
    
    def calcular_adicionais(self):
        if self.linguagem == 'Python':
            return 500
        elif self.linguagem == 'Java':
            return 400
        elif self.linguagem == 'JavaScript':
            return 350
        else:
            return 200