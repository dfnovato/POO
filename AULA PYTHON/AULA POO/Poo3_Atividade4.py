class Produto:
    def __init__(self, nome, preco, qtd):
        self.__nome = nome
        self.__preco = preco
        self.__qtd = qtd
        
    #   Nome_____________________________________________________________________
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    #   Preço____________________________________________________________________
    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, preco):
        if preco < 0:  # Deveria ser o parâmetro 'preco', não self.__preco
            print("Preço não pode ser negativo")
        else:
            self.__preco = preco
            print(f"Preço atualizado para {self.__preco}")

    #   Quantidade________________________________________________________________
    @property
    def qtd(self):
        return self.__qtd
    @qtd.setter
    def qtd(self, qtd):
        if self.__qtd + qtd >= 0:
            self.__qtd += qtd
        else:
            print("Quantidade insuficiente")


Livro = Produto("Livro", 50, 10)
print(Livro.nome)
print(Livro.preco)
print(Livro.qtd)
Livro.nome = "Livro de Python"
Livro.preco = -100
Livro.qtd = -15
print(Livro.nome)
print(Livro.preco)
print(Livro.qtd)