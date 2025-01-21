class forma_geometrica:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class retangulo(forma_geometrica):
    def __init__(self, base, altura):
        super().__init__(base, altura)
        
    def area(self):
        return self.base * self.altura

class triangulo(forma_geometrica):
    def __init__(self, base, altura):
        super().__init__(base, altura)
        
    def area(self):
        return (self.base * self.altura) / 2
    
class quadrado(forma_geometrica):
    def __init__(self, base, altura):
        super().__init__(base, altura)
        
    def area(self):
        return self.base * self.altura
    
class circulo(forma_geometrica):
    def __init__(self, base, altura):
        super().__init__(base, altura)
        
    def area(self):
        return 3.14 * (self.base ** 2)

ret = retangulo(10, 5)
tri = triangulo(10, 5)
qua = quadrado(10, 10)
cir = circulo(10, 10)

print(ret.area())
print(tri.area())
print(qua.area())
print(cir.area())