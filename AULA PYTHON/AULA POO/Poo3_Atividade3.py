class Alunos:
    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula
    
    #decorador    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, newnome):
        self.__nome = newnome
        print(f"Nome {self.__nome}")
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, newidade):
        self.__idade = newidade
        print(f"Idade {self.__idade}")
    
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, newmatricula):
        self.__matricula = newmatricula
        print(f"Matricula {self.__matricula}")

Marcos = Alunos("Marcos", 27, 25)
Tyago = Alunos("Tyago", 26, 26)

print(Marcos.nome)
print(Marcos.idade)
print(Marcos.matricula)
Marcos.nome = "Marcos Lisboa"
Marcos.idade = 28
Marcos.matricula = 27
print(Marcos.nome)
print(Marcos.idade)
print(Marcos.matricula)