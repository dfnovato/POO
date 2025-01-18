class Automoveis:
#metodo construtor
    def __init__(self, marca, cor, maximo ,):
        #atributos da classe
        self.marca = marca
        self.cor = cor
        self.velo_max = maximo
        self.ligado = False
        self.velo_atual:float = 0
    #Medoto 1
    def ligar_desligar(self):
        if not self.ligado and self.velo_atual==0:
            self.ligado = True
        elif self.ligado and self.velo_atual==0:
            self.ligado = False
    #Metodo 2
    def acelerar(self, velo):
        if (self.velo_atual + velo) <= self.velo_max:
            self.velo_atual += velo
    #Metodo 3
    def frear(self, velo):
        if (self.velo_atual - velo)>=0:
            self.velo_atual -= velo