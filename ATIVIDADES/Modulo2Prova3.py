dict = {
}
dict["nome"] = input("Digite nome:")
dict["telefone"] = input("Digite telefone:")
dict["e-mail"] = input("Digite e-mail:")

print(dict)

print("\nInformações do contato:")
for key, value in dict.items():
    print(f"{key.capitalize()}: {value}")