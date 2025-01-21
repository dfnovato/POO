class Calculadora:
    def __init__(self, n1, n2=0, n3=0, n4=0, n5=0):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5

    def soma(self):
        total = float(self.n1) + float(self.n2) + float(self.n3) + float(self.n4) + float(self.n5)
        return total

    def subtracao(self):
        return self.n1 - self.n2 - self.n3 - self.n4 - self.n5

    def multiplicacao(self):
        return self.n1 * self.n2 * self.n3 * self.n4 * self.n5

    def divisao(self):
        return self.n1 / self.n2 / self.n3 / self.n4 / self.n5
    
calcular = Calculadora("2"+"1")
calcular2 = Calculadora("2", "1")

print(calcular.soma())