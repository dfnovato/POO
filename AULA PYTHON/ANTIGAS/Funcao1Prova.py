def media(a: float, b: float, c: float) -> float:
    resultado = (a + b + c) / 3
    return resultado

print("Digite 3 números para calcular a média:")
num1 = float(input("Digite o 1° número: "))
num2 = float(input("Digite o 2° número: "))
num3 = float(input("Digite o 3° número: "))

resultado = media(num1, num2, num3)
print(f"A média dos números é: {resultado:.2f}")

"""-----------------------exemplo feito utilizando uma variavel global
numero = []
def media() -> float:
    resultado = (numero[0] + numero[1] + numero[2]) / 3
    return resultado

print("Digite 3 numeros para calcular a media")
for n in range(0,3):
    n +=1
    digitado = float(input(f"Digite o {n}°: "))
    numero.append(digitado) 

print(f"{media():.2f}")
"""