#emcapsulamento

class Conta_Correntes:
    def __init__(self, numero, nome):
        self._numero = numero
        self.__saldo = 0
        self.correntista = nome
    
    #decorator
    @property
    def saldo(self): #getter
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor): #setter
        if (self.__saldo + valor) >= 0:
            self.__saldo += valor
        else:
            print(f"Saldo insuficiente")

    def __str__(self):
        return "Numero {} Saldo {}".format(self._numero, self.__saldo)

    def __eq__(self, outro):
        if type(outro) != Conta_Correntes:
            return False

        return self._numero == outro._numero and self.__saldo == outro.__saldo

    def transfere(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)


Marcos = Conta_Correntes("123-1", "Marcos")
print(Marcos.saldo) #Getter
Marcos.saldo = 10000 #Setter
Marcos.saldo = (-1000) #Setter
print(Marcos.saldo) #Getter