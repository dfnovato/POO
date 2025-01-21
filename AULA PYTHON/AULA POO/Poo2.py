class Animais:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        
    def comer(self):
        print(f'{self.nome} está comendo')

    def falar(self):
        print(f'{self.nome} está falando')
        
class Cachorro(Animais):
    def __init__(self, nome, idade, raca, cor):
        super().__init__(nome, idade, raca)
        self.cor = cor
        
    def latir(self):
        print(f'{self.nome} está latindo')
        
class Gato(Animais):
    def __init__(self, nome, idade, raca, cor):
        super().__init__(nome, idade, raca)
        self.cor = cor
        
    def miar(self):
        print(f'{self.nome} está miando')
        
#objeto
rex = Cachorro(nome='Rex', idade=3, raca='Pastor Alemão', cor='Marrom')
rex.comer()
rex.latir()