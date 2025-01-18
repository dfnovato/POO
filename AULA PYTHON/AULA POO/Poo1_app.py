from Poo1 import (Automoveis)
import time

#Objeto
civic = Automoveis(
    marca="Honda",
    cor="branco",
    maximo=200
)

opala = Automoveis(
    marca="Chevy",
    cor="Preto",
    maximo=150
)

#utilizando metodo
civic.ligar_desligar()

print(civic.ligado)

for x in range(21):
    civic.acelerar(velo=10)
    print(civic.velo_atual)
    time.sleep(0.25)

#testando desligar o carro correndo    
civic.ligar_desligar()
print(civic.ligado)

for y in range(11):
    civic.frear(velo=20)
    print(civic.velo_atual)
    time.sleep(0.25)

#desligando o carro parado
civic.ligar_desligar()
print(civic.ligado)