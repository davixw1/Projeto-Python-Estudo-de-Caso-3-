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
            print("Nenhuma corrida cadastrada")
        else:
            print("\n========= CORRIDAS =========\n")
            print(f"{'Código':<8}{'Corrida':<37}{'Checkpoints':11}")
            print("-"*56)
            for i in range(len(corridas)):
                c = corridas[i]
                codigo = i+1
                nome = c[0]
                cps = c[1]
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
            print(
                "\nErro: Já existe uma equipe cadastrada com esse número de identificação!"
            )
        else:
            nome_equipe = input("Nome da equipe: ").strip().title()
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
    
    # 5. CONSULTAR CORRIDA POR CÓDIGO
    elif opcao == "5":
        print("\n===== CONSULTAR CORRIDA =====\n")
        codigo_busca = int(input("Digite o código da corrida: ")).strip()
        if codigo_busca.isdigit():
            idx = int(codigo_busca) - 1
            if 0 <= idx < len(corridas):
                c = corridas[idx]
                print("\nCorrida encontrada:\n")
                print(f"{'Código':<8}{'Corrida':<37}{'Checkpoints':>11}")
                print("-" * 56)
                print(f"{str(idx + 1):<8}{c[0]:<37}{str(c[1]):>11}")
            else:
                ("\nCorrida não encontrada.")
        else:
            ("\nCódigo inválido.")

    # 7. CONSULTAR EQUIPE POR NÚMERO
    el
= oacpo f

    # 0. SAIR
    elif opcao == "0":
        print("\nSaindo do sistema...")
        break

    else:
        print("\nOpção inválida! Tente novamente.") 

    # 6. PESQUISAR CORRIDA POR NOME 
    elif opcao == "6":
        print("\n========= PESQUISAR CORRIDA =========\n")
        if len(corridas) == 0:
            print("Nenhuma corrida cadastrada")
        else:
            termo = input("Digite o nome da corrida: ").strip().lower()
            
            encontradas = []
            for i in range(len(corridas)):
                c = corridas[1]
                if termo inn  c[0].lower()
        

        
        
    print