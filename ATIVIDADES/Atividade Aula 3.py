import random
tentativa=3 
numero_aleatorio = random.randint(1, 10)
print("Acerte o Numero Aleatorio 3 tentatvias")
while  tentativa > 0:
    num = int(input(f"Digite um número (resta {tentativa}): "))
    tentativa -= 1
    if num != numero_aleatorio:
        print("Voce errou.")
    else:
        print("Parabens voce acertou.")
        break
else:
    print(f"Chances esgotadas o resultado era: {numero_aleatorio}.")