class Clientes:
    def __init__(self, nome, telefone, email):
        self.Nome = nome
        self.Telefone = telefone
        self.Email = email
        self.Id:int = 0
    
    def gerar_cliente(self):
        Clientes.Id +=1
        self.id_cliente = Clientes.Id

class Quartos:
    def __init__(self, tipo, preco):
        self.Numero:int = 0
        self.Tipo = tipo
        self.Preco:float = preco
        self.Disponibilidade = True

    def gerar_quarto(self):
        Quartos.numero +=1
        self.numero_quarto = Quartos.Numero

class Reservas(Clientes, Quartos):
    def __init__(self, obj_cliente, obj_quarto ,checkin, checkout,Nome, Id, Numero, Disponibilidade):
        super().__init__(Nome, Id)
        super().__init__(Numero, Disponibilidade)
        self.quarto = obj_quarto
        self.id_cliente = obj_cliente
        self.checkin = checkin
        self.checkout = checkout

marcos = Clientes("Marcos", "71985282534", "marcos.lisboa@bradsaude.com.br")
marcos.gerar_cliente()
quarto = Quartos("Single", 1000, False)
quarto.gerar_quarto()
print(marcos.Email)
print(quarto)