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
    print("5 - Consultar corrida por código")
    print("6 - Pesquisar corrida por nome")
    print("7 - Consultar equipe por número")
    print("8 - Pesquisar equipe por nome")
    print("0 - Sair" "\n")
    
    opcao = input("Escolha uma opção: ").strip()
    
    # 1. CADASTRAR CORRIDA
    if opcao == "1":
        print("\n===== CADASTRO DE CORRIDA =====\n")
        nome_corrida = input("Nome da corrida: ").strip().title()
        qtd_checkpoints = int(input("Quantidade de checkpoints: "))
        
        if qtd_checkpoints <= 0:
            print("\nA quantidade de checkpoints deve ser maior que zero!")
        else:
            corridas.append([nome_corrida , qtd_checkpoints])
            print("\nCorrida cadastrada com sucesso!")
            
    # 2. LISTAR CORRIDAS
    elif opcao == "2":
        if len(corridas) == 0:
            print("Nenhuma corrida cadastrada.")
        else:
            print("\n========= CORRIDAS =========\n")
            print(f"{'Código':<8}{'Corrida':<37}{'Checkpoints':11}")
            print("-"*56)
            for i in range(len(corridas)):
                c = corridas[i]
                codigo = str(i+1)
                nome = c[0]
                cps = str(c[1])
                print(f"{codigo:<8}{nome:<37}{cps:>11}")

    # 3. CADASTRAR EQUIPE
    elif opcao == "3":
        print("\n===== CADASTRO DE EQUIPE =====\n")
        num_equipe = input("Número da equipe: ").strip()

        existe = False
        for eq in equipes:
            if eq[0] == num_equipe:
                existe = True
                break

        if existe:
            print("\nErro: Já existe uma equipe cadastrada com esse número de identificação!")
        else:
            nome_equipe = input("Nome da equipe: ").strip().title()
            equipes.append([num_equipe, nome_equipe])
            print("\nEquipe cadastrada com sucesso!")
            
    # 4. LISTAR EQUIPES
    elif opcao == "4":
        if len(equipes) == 0:
            print("\nNenhuma equipe cadastrada.")
        else:
            print("\n========================= EQUIPES ===========================\n")
            print(f"{'Número':<8}{'Equipe':<40}")
            print("-" * 48)
            for eq in equipes:
                print(f"{eq[0]:<8}{eq[1]:<40}")

    # 5. CONSULTAR CORRIDA POR CÓDIGO
    elif opcao == "5":
        print("\n===== CONSULTAR CORRIDA =====\n")
        codigo_busca = input("Digite o código da corrida: ").strip()

        if codigo_busca.isdigit():
            idx = int(codigo_busca) - 1
            if 0 <= idx < len(corridas):
                c = corridas[idx]
                print("\nCorrida encontrada:\n")
                print(f"{'Código':<8}{'Corrida':<37}{'Checkpoints':>11}")
                print("-" * 56)
                print(f"{str(idx + 1):<8}{c[0]:<37}{str(c[1]):>11}")
            else:
                print("\nCorrida não encontrada.")
        else:
            print("\nCódigo inválido.")

    # 6. PESQUISAR CORRIDA POR NOME
    elif opcao == "6":
        print("\n===== PESQUISAR CORRIDA =====\n")
        termo = input("Digite o nome ou parte do nome: ").strip().lower()

        encontradas = []
        for i in range(len(corridas)):
            c = corridas[i]
            if termo in c[0].lower():
                encontradas.append([i + 1, c[0], c[1]])

        if len(encontradas) == 0:
            print("\nNenhuma corrida encontrada.")
        else:
            print("\nCorridas encontradas:\n")
            print(f"{'Código':<8}{'Corrida':<37}{'Checkpoints':>11}")
            print("-" * 56)
            for item in encontradas:
                print(f"{str(item[0]):<8}{item[1]:<37}{str(item[2]):>11}")

    # 7. CONSULTAR EQUIPE POR NÚMERO
    elif opcao == "7":
        print("\n===== CONSULTAR EQUIPE =====\n")
        num_busca = input("Digite o número da equipe: ").strip()

        equipe_encontrada = None
        for eq in equipes:
            if eq[0] == num_busca:
                equipe_encontrada = eq
                break

        if equipe_encontrada:
            print("\nEquipe encontrada:\n")
            print(f"{'Número':<8}{'Equipe':<40}")
            print("-" * 48)
            print(f"{equipe_encontrada[0]:<8}{equipe_encontrada[1]:<40}")
        else:
            print("\nEquipe não encontrada.")

    # 8. PESQUISAR EQUIPE POR NOME
    elif opcao == "8":
        print("\n===== PESQUISAR EQUIPE =====\n")
        termo = input("Digite o nome ou parte do nome: ").strip().lower()

        encontradas = []
        for eq in equipes:
            if termo in eq[1].lower():
                encontradas.append(eq)

        if len(encontradas) == 0:
            print("\nNenhuma equipe encontrada.")
        else:
            print("\nEquipes encontradas:\n")
            print(f"{'Número':<8}{'Equipe':<40}")
            print("-" * 48)
            for eq in encontradas:
                print(f"{eq[0]:<8}{eq[1]:<40}")

    # 0. SAIR
    elif opcao == "0":
        print("\nSaindo do sistema...")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
