x = int(input("digite o primeiro valor "))
y = int(input("digite o segundo valor "))
soma = 0
for num in range(x, y+1):
    if num %2 ==0:
        soma_pass = soma
        #variavel soma_pass não é nessaria eu poderia operar a soma apos o print e ter somado dentro do print mas so pensei depois... não sei se ficou clara a explicação
        soma += num
        print(f"foi rodado {num} + {soma_pass} = {soma}")
if soma == 0:
    print("Sem numeros pares")
else:
    print(f"O Numero Final foi: {soma}")