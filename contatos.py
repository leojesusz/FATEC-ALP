contatos = []

while True:
    print("1 - Cadastrar novo contato")
    print("2 - Exibir contatos cadastrados")
    print("3 - Excluir contato")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = str(input("Digite o nome do contato: "))
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o e-mail do contato: ")
        novo_contato = {"nome": nome, "telefone": telefone, "email": email}
        contatos.append(novo_contato)
        print("Contato cadastrado!")

    elif opcao == "2":
        print("Lista de contatos:")
        for contato in contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")
        print()    
    elif opcao == "3":
        nome_excluir = input("Digite o nome do contato que deseja excluir: ")
        encontrado = False
        for contato in contatos:
            if contato['nome'] == nome_excluir:
                contatos.remove(contato)
                encontrado = True
                print(f"Contato {nome_excluir} removido com sucesso!")
                break
        if not encontrado:
            print(f"Contato {nome_excluir} não encontrado.")
    else:
        print("Opção inválida. Escolha uma opção válida.")