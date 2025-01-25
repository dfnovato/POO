# Dicionário inicial
dados = {
    "nome": ["Marcos", "Tiago"],
    "telefone": ["71985282534", "5435345324"],
    "email": ["quinhonovato@gmail.com"]
}

# Imprimindo o dicionário completo
print(dados)

# Imprimindo apenas os nomes
print(dados["nome"])

# Obtendo e imprimindo a lista de telefones usando .get()
telefones = dados.get("telefone")
print(telefones)

# Imprimindo todas as chaves do dicionário
chaves = dados.keys()
print(chaves)

# Imprimindo todos os valores do dicionário
valores = dados.values()
print(valores)

# Substituindo o primeiro email no dicionário
dados["email"][0] = "quinho-9@hotmail.com"
print(dados["email"])

# Adicionando uma nova chave 'idade' e imprimindo o dicionário atualizado
dados["idade"] = [27, 26]  # Adiciona idades para Marcos e Tiago
print(dados)

# Removendo a chave 'telefone' e imprimindo o dicionário atualizado
dados.pop("telefone")
print(dados)

# Removendo o último item adicionado (idade) e imprimindo o dicionário atualizado
dados.popitem()
print(dados)

# Iterando sobre o dicionário e imprimindo as chaves e valores formatados
for key, value in dados.items():
    print(f"{key.capitalize()}: {value}")

# Adicionando um novo email para Tiago na lista de emails
dados["email"].append("tiagodabahia@bahia.com.br")
print(dados)

# Usando items() para iterar sobre chave e valor
for chave, valor in dados.items():
    print(f"{chave.capitalize()}: {valor}")
    
# Usando setdefault para adicionar 'idade' se não existir
dados.setdefault("idade", [18, 22])  # Adiciona idade padrão para Marcos e Tiago
print("Idade:", dados.get("idade"))

# Garantindo que a chave 'nome' existe e adicionando um novo nome
dados.setdefault("nome", []).append("patachoca")
print("nome:", dados.get("nome"))

# Utilizando copy para trabalhar sem alterar o dicionario original
dados_copia = dados.copy()

# Fazendo alterações na cópia sem afetar o original
dados_copia["nome"].append("Carlos")  # Adicionando um novo nome na cópia
dados_copia["idade"] = [18, 22, 30]   # Adicionando uma nova chave "idade" na cópia

# Imprimindo o dicionário original e a cópia para comparação
print("Dicionário Original:", dados)
print("Dicionário Cópia:", dados_copia)

#erro acima onde copy apenas utilizar deepcopy