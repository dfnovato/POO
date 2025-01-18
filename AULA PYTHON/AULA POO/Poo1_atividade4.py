class Calculadora:
    
    def  somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b!=0:
            return a/b
        else:
            return "Otario"         ,;

calculadora = Calculadora()

print(calculadora.somar(5,5))
print(calculadora.subtrair(5,5))
print(calculadora.multiplicar(5,5))
print(calculadora.dividir(5,5))
print(calculadora.dividir(5,0))
        