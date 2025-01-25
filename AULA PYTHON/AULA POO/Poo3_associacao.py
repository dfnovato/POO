class Clientes:
    def __init__(self, nome):
        self.nome = nome
        self.pedido = []
        
    def inserir_pedido(self, obj_pedido):
        self.pedido.append(obj_pedido)
        
class Pedido:
    def __init__(self, produto, qtd, valor):
        self.produto = produto
        self.qtd = qtd
        self.valor = valor
        
#criando objetos
Marcos = Clientes("Marcos")
pedido1 = Pedido("Notebook", 1, 2000.00)
pedido2 = Pedido("Mouse", 2, 49.99)
pedido3 = Pedido("Teclado", 1, 150.00)

#associando os pedidos ao cliente
Marcos.inserir_pedido(pedido1)
Marcos.inserir_pedido(pedido2)
Marcos.inserir_pedido(pedido3)

#imprimindo os pedidos
for pedido in Marcos.pedido:
    print(f"Produto: {pedido.produto}, Quantidade: {pedido.qtd}, Valor: {pedido.valor:.2f}")
    total = pedido.qtd * pedido.valor
print(f"Total: {total:.2f}\n")