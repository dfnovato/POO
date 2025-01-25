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
        return f"Nome {self.__nome}"
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, newidade):
        self.__idade = newidade
        return f"Idade {self.__idade}"
    
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, newmatricula):
        self.__matricula = newmatricula
        return f"Matricula {self.__matricula}"
    
    def __str__(self):
        return f"Nome {self.__nome} Idade {self.__idade} Matricula {self.__matricula}"
    
Marcos = Alunos("Marcos", 27, 25)
Tyago = Alunos("Tyago", 26, 26)

print(Marcos.nome)
Marcos.nome = "Marcos Lisboa"
print(Marcos.nome)