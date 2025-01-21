from Poo1 import (Automoveis, carro, moto, Garagem)
import time

#Objeto
civic = carro(
    marca="Honda",
    cor="branco",
    maximo=200,
    portas=4
)

opala = carro(
    marca="Chevy",
    cor="Preto",
    maximo=150,
    portas=4
)

gs310 = moto(
    marca="BMW",
    cor="Azul",
    maximo=250,
    cilindradas=310
)

#utilizando metodo
print("usando o civic")
civic.ligar_desligar()

print(civic.ligado)

for x in range(21):
    civic.acelerar(velo=10)
    time.sleep(0.1)

#testando desligar o carro correndo    
civic.ligar_desligar()
print(civic.ligado)

for y in range(11):
    civic.frear(velo=20)
    time.sleep(0.1)

#desligando o carro parado
civic.ligar_desligar()
print(civic.ligado)

print("usando a moto")
gs310.ligar_desligar()
print(gs310.ligado)
for z in range(21):
    gs310.acelerar(velo=10)
    time.sleep(0.1)
for y in range(11):
    gs310.frear(velo=20)
    time.sleep(0.1)
gs310.ligar_desligar()

print(gs310.ligado)

garagem = Garagem()
print(garagem.listar_veiculos())
print(garagem.add_automovel(civic))
print(garagem.listar_veiculos())
print(garagem.remover_automovel(civic))
civic.sair_garagem()