class Animais:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        
    def comer(self):
        print(f'{self.nome} está comendo')

    def falar(self):
        print(f'{self.nome} está falando')