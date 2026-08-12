corridas = []
equipes = []

while True:
    print("="*35)
    print("       CAMINHOS DA AVENTURA")
    print("="*35 + "\n")
    print("1 - Cadastrar corrida")
    print("2 - Listar corridas")
    print("3 - Cadastrar equipe")
    print("4 - Listar equipes")
    print("0 - Sair" "\n")
    
    opcao = input("Escolha uma opção: ")
    
    # 1. CADASTRAR CORRIDA
    if opcao == "1":
        print("\n===== CADASTRO DE CORRIDA =====\n")
        nome_corrida = input("Nome da corrida: ")
        qtd_checkpoints = int(input("Quantidade de checkpoints: "))
        
        if qtd_checkpoints <= 0:
            print("\nA quantidade de checkpoints deve ser maior que zero!")
        else:
            corridas.append([nome_corrida , qtd_checkpoints])
            print("\nCorrida cadastrada com sucesso!")
            
    # 2. LISTAR CORRIDAS
    elif opcao == "2":
        print("\n========= CORRIDAS =========\n")
        if len(corridas) == 0:
            print("Nenhuma corrida cadastrada")
        else:
            for i in range(len(corridas)):
                c = corridas[i]
                print(f"{i + 1} - {c[0]}")
                print(f"  Checkpoints: {c[1]}\n")

    # 3. CADASTRAR EQUIPE
    elif opcao == "3":
        print("\n===== CADASTRO DE EQUIPE =====\n")
        num_equipe = input("Número da equipe: ")

        existe = False
        for eq in equipes:
            if eq[0] == num_equipe:
                existe = True
                break

        if existe:
            print(
                "\nErro: Já existe uma equipe cadastrada com esse número de identificação!"
            )
        else:
            nome_equipe = input("Nome da equipe: ")
            equipes.append([num_equipe, nome_equipe])
            print("\nEquipe cadastrada com sucesso!")
            
    # 4. LISTAR EQUIPES
    elif opcao == "4":
        print("\n========= EQUIPES =========\n")
        if len(equipes) == 0:
            print("Nenhuma equipe cadastrada")
        else:
            for equipe in equipes:
                print(f"{equipe[0]} - {equipe[1]}")

    #0. SAIR
    elif opcao == "0":
        print("\nSaindo do sistema...")
        break

    else:
        print("\nOpção inválida! Tente novamente.")                                        