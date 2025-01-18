class Funcionario:

    dolar:float=6.15

    @classmethod
    def converter(cls, salario):
        return salario / Funcionario.dolar
    
    def __init__(self, nome, cargo, sal, valordesconto): #metodo construtor
        #atributos da classe
        self.nome = nome
        self.cargo = cargo
        self.salario = sal
        self.valordesconto = valordesconto

    def desconto(self):
        if (self.salario - self.valordesconto) >=0:
            self.salario -= self.valordesconto
        else:
           print(f"Desconto não pode ser aplicado para o funcionario {self.nome}")
            
    
    def __str__(self):
        return f"Nome:{self.nome}, cargo:{self.cargo}, salario: R${self.salario:.2f} Dolar: U${Funcionario.converter(self.salario):.2f}\n"
    
class  Empresa:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, nome, cargo, sal, valordesconto):
        novo_funcionario = Funcionario(nome, cargo, sal, valordesconto)

        self.funcionarios.append(novo_funcionario)

        print(f"Funcionario {nome} adicionado com sucesso.")

    def remover_funcionario(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                self.funcionarios.remove(funcionario)
                print(f"Funcionário {nome} removido com sucesso.")
                return
        print(f"Funcionário {nome} não encontrado.")
        
    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            print("Lista de funcionários:")
            for funcionario in self.funcionarios:
                print(funcionario)
    
    def aplicar_desconto(self):
        for funcionario in self.funcionarios:
            funcionario.desconto()

marcos = Funcionario("Marcos", "Dev", 2000, 10000)
pedro = Funcionario("Pedro", "Designer", 4000, 200)

empresa = Empresa()
empresa.adicionar_funcionario(marcos.nome, marcos.cargo, marcos.salario, marcos.valordesconto)
empresa.adicionar_funcionario(pedro.nome, pedro.cargo, pedro.salario, marcos.valordesconto)
empresa.listar_funcionarios()
empresa.remover_funcionario(pedro.nome)
empresa.aplicar_desconto()
empresa.listar_funcionarios()