class Automoveis:
#metodo construtor
    def __init__(self, marca, cor, maximo):
        #atributos da classe
        self.marca = marca
        self.cor = cor
        self.velo_max = maximo
        self.ligado = False
        self.velo_atual:float = 0
        self.garagem = None
        #para privar um atributo basta adicionar o __ antes do atributo
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
            print(f"acelerando {self.velo_atual}")
    #Metodo 3
    def frear(self, velo):
        if (self.velo_atual - velo)>=0:
            self.velo_atual -= velo
            print (f"freando {self.velo_atual}")
    #Metodo 4
    def estacionar(self, garagem):
        if self.garagem:
            return "O automóvel já está em uma garagem."
        self.garagem = garagem
        return garagem.add_automovel(self)
    #Metodo 5
    def sair_garagem(self):
        if self.garagem:
            resultado = self.garagem.remover_automovel(self)
            self.garagem = None
            return resultado
        return "O automóvel não está em nenhuma garagem."
                    
class carro (Automoveis):
    def __init__(self, marca, cor, maximo, portas):
        super().__init__(marca, cor, maximo)
        self.portas = portas

        
    def frear(self, velo):
        if (self.velo_atual - velo)>=0:
            self.velo_atual -= velo
        print (f"freando o carro {self.velo_atual}")
        return f"freio acionado"

class moto (Automoveis):
    def __init__(self, marca, cor, maximo, cilindradas):
        super().__init__(marca, cor, maximo)
        self.cilindradas = cilindradas

        
    def frear(self, velo):
        if (self.velo_atual - velo)>=0:
            self.velo_atual -= velo
        print (f"freando a moto {self.velo_atual}")
        return f"manete acionada"
    
    
class Garagem:
    def __init__(self):
        self.qtd_vagas = 200
        self.lista_vagas = []
        
    #Metodo 1 de garagem
    def add_automovel(self, automovel):
        if automovel not in self.lista_vagas:
            self.lista_vagas.append(automovel)
            self.qtd_vagas -=1
            return f"Temos {self.qtd_vagas} vagas disponíveis"
        return "O automóvel já está na garagem."
    
    #Metodo 2 de garagem
    def remover_automovel(self, automovel):
        if automovel in self.lista_vagas:
            self.lista_vagas.remove(automovel)
            self.qtd_vagas += 1
            return f"Temos {self.qtd_vagas} vagas disponíveis"
        return "O automóvel não está na garagem."

    #Metodo 3 de garagem
    def listar_veiculos(self):
        if not self.lista_vagas:
            return "Não há veículos na garagem."
        veiculos = "\n".join([
            f"{idx + 1}. Marca: {veiculo.marca}, Cor: {veiculo.cor}, Velocidade Máx: {veiculo.velo_max} km/h"
            for idx, veiculo in enumerate(self.lista_vagas)
        ])
        return f"Veículos na garagem:\n{veiculos}"