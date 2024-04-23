contatos = []
i = 1
while True:
    print("1 - Cadastrar novo contato\n2 - Exibir contatos cadastrados\n3 - Excluir contato")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        cpf = input("Digite o CPF do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o e-mail do contato: ")
        novo_contato = {"nome": nome, "cpf": cpf, "telefone": telefone, "email": email}
        contatos.append(novo_contato)
        print("Contato cadastrado!")

    elif opcao == "2":
        print("Lista de contatos:")
        for contato in contatos:
            print(f"Nome: {contato['nome']}, CPF: {contato['cpf']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")
        print()    
    elif opcao == "3":
        cpf_excluir = input("Digite o CPF do contato que deseja excluir: ")
        encontrado = False
        for contato in contatos:
            if contato['cpf'] == cpf_excluir:
                contatos.remove(contato)
                encontrado = True
                print(f"Contato {i}, com CPF: {cpf_excluir} removido com sucesso!")
                i+=1
                break
        if not encontrado:
            print(f"Contato com CPF: {cpf_excluir} não encontrado.")
    else:
        print("Opção inválida. Escolha uma opção válida.")