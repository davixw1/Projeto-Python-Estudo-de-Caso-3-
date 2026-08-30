corridas = []
equipes = []
passagens = []

while True:
    print("=================================")
    print("       CAMINHOS DA AVENTURA")
    print("=================================\n")
    print("1 - Corridas")
    print("2 - Equipes")
    print("3 - Acompanhamento")
    print("0 - Sair\n")
    
    opcao_principal = input("Escolha uma opção: ").strip()
    
    # SUBMENU 1: CORRIDAS

    if opcao_principal == "1":
        while True:
            print("\n=========== CORRIDAS ===========")
            print("1 - Cadastrar corrida")
            print("2 - Listar corridas")
            print("3 - Consultar corrida por código")
            print("4 - Pesquisar corrida por nome")
            print("0 - Voltar\n")
            
            opcao_corrida = input("Escolha uma opção: ").strip()
            
            if opcao_corrida == "1":
                print("\n===== CADASTRO DE CORRIDA =====\n")
                nome_corrida = input("Nome da corrida: ").strip().title()
                qtd_checkpoints = int(input("Quantidade de checkpoints: "))
                
                if qtd_checkpoints <= 0:
                    print("\nA quantidade de checkpoints deve ser maior que zero!")
                else:
                    corridas.append([nome_corrida, qtd_checkpoints])
                    print("\nCorrida cadastrada com sucesso!")
                    
            elif opcao_corrida == "2":
                if len(corridas) == 0:
                    print("\nNenhuma corrida cadastrada.")
                else:
                    print("\n========= LISTA DE CORRIDAS =========\n")
                    for i in range(len(corridas)):
                        c = corridas[i]
                        cod_corrida = i + 1
                        print(f"\nCORRIDA {cod_corrida}: {c[0]}")
                        
                        print(f"{'Equipe':<8} {'Checkpoints registrados':>23}")
                        print("-" * 32)
                        

                        teve_registro = False
                        for eq in equipes:
                            num_equipe = eq[0]
                            contador = 0
                            
                            for p in passagens:
                                if p[0] == cod_corrida and p[1] == num_equipe:
                                    contador += 1
                                    
                            if contador > 0:
                                print(f"{num_equipe:<8} {contador:>23}")
                                teve_registro = True
                                
                        if not teve_registro:
                            print("Nenhum checkpoint registrado ainda.")
                                
            elif opcao_corrida == "3":
                print("\n===== CONSULTAR CORRIDA =====\n")
                codigo_busca = input("Digite o código da corrida: ").strip()

                if codigo_busca.isdigit():
                    idx = int(codigo_busca) - 1
                    if 0 <= idx < len(corridas):
                        c = corridas[idx]
                        cod_corrida = idx + 1
                        print(f"\nCORRIDA: {c[0]}\n")
                        print(f"{'Equipe':<8} {'Checkpoints registrados':>23}")
                        print("-" * 32)
                        
                        teve_registro = False
                        for eq in equipes:
                            num_equipe = eq[0]
                            contador = 0
                            
                            for p in passagens:
                                if p[0] == cod_corrida and p[1] == num_equipe:
                                    contador += 1
                                    
                            if contador > 0:
                                print(f"{num_equipe:<8} {contador:>23}")
                                teve_registro = True
                                
                        if not teve_registro:
                            print("Nenhum checkpoint registrado ainda.")
                    else:
                        print("\nCorrida não encontrada.")
                else:
                    print("\nCódigo inválido.")
                    
            elif opcao_corrida == "4":
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
                        
            elif opcao_corrida == "0":
                break
            else:
                print("\nOpção inválida!")


    # SUBMENU 2: EQUIPES

    elif opcao_principal == "2":
        while True:
            print("\n============ EQUIPES ============")
            print("1 - Cadastrar equipe")
            print("2 - Listar equipes")
            print("3 - Consultar equipe por número")
            print("4 - Pesquisar equipe por nome")
            print("0 - Voltar\n")
            
            opcao_equipe = input("Escolha uma opção: ").strip()
            
            if opcao_equipe == "1":
                print("\n===== CADASTRO DE EQUIPE =====\n")
                num_equipe = input("Número da equipe: ").strip()

                existe = False
                for eq in equipes:
                    if eq[0] == num_equipe:
                        existe = True
                        break

                if existe:
                    print("\nErro: Já existe uma equipe cadastrada com esse número!")
                else:
                    nome_equipe = input("Nome da equipe: ").strip().title()
                    equipes.append([num_equipe, nome_equipe])
                    print("\nEquipe cadastrada com sucesso!")
                    
            elif opcao_equipe == "2":
                if len(equipes) == 0:
                    print("\nNenhuma equipe cadastrada.")
                else:
                    print("\n========================= EQUIPES ===========================\n")
                    print(f"{'Número':<8}{'Equipe':<40}")
                    print("-" * 48)
                    for eq in equipes:
                        print(f"{eq[0]:<8}{eq[1]:<40}")
                        
            elif opcao_equipe == "3":
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
                    
            elif opcao_equipe == "4":
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
                        
            elif opcao_equipe == "0":
                break
            else:
                print("\nOpção inválida!")

    # SUBMENU 3: ACOMPANHAMENTO

    elif opcao_principal == "3":
        while True:
            print("\n========= ACOMPANHAMENTO =========")
            print("1 - Registrar passagem")
            print("2 - Consultar equipe na corrida")
            print("0 - Voltar\n")
            
            opcao_acompanhamento = input("Escolha uma opção: ").strip()
            
            if opcao_acompanhamento == "1":
                print("\n===== REGISTRAR PASSAGEM =====\n")
                cod_corrida = input("Código da corrida: ").strip()
                num_equipe = input("Número da equipe: ").strip()
                checkpoint = input("Checkpoint: ").strip()
                
                if not (cod_corrida.isdigit() and checkpoint.isdigit()):
                    print("\nErro: Código da corrida e Checkpoint devem ser numéricos.")
                    continue
                
                cod_corrida = int(cod_corrida)
                checkpoint = int(checkpoint)
                
                if cod_corrida < 1 or cod_corrida > len(corridas):
                    print("\nErro: A corrida não existe.")
                    continue
                    
                equipe_existe = False
                for eq in equipes:
                    if eq[0] == num_equipe:
                        equipe_existe = True
                        break
                if not equipe_existe:
                    print("\nErro: A equipe não existe.")
                    continue
                    
                max_checkpoints = corridas[cod_corrida - 1][1]
                if checkpoint < 1 or checkpoint > max_checkpoints:
                    print(f"\nErro: Checkpoint inválido. Esta corrida tem de 1 a {max_checkpoints} checkpoints.")
                    continue
                    
                registro_duplicado = False
                for p in passagens:
                    if p[0] == cod_corrida and p[1] == num_equipe and p[2] == checkpoint:
                        registro_duplicado = True
                        break
                        
                if registro_duplicado:
                    print("\nA equipe já registrou este checkpoint nesta corrida.")
                else:
                    passagens.append([cod_corrida, num_equipe, checkpoint])
                    print("\nPassagem registrada com sucesso!")
                    
            elif opcao_acompanhamento == "2":
                print("\n===== CONSULTAR EQUIPE NA CORRIDA =====\n")
                cod_corrida = input("Código da corrida: ").strip()
                num_equipe = input("Número da equipe: ").strip()
                
                if not cod_corrida.isdigit():
                    print("\nErro: Código da corrida deve ser numérico.")
                    continue
                    
                cod_corrida = int(cod_corrida)
                
                nome_corrida = ""
                if 1 <= cod_corrida <= len(corridas):
                    nome_corrida = corridas[cod_corrida - 1][0]
                    
                nome_equipe = ""
                for eq in equipes:
                    if eq[0] == num_equipe:
                        nome_equipe = eq[1]
                        break
                        
                if not nome_corrida:
                    print("\nErro: Corrida não encontrada.")
                elif not nome_equipe:
                    print("\nErro: Equipe não encontrada.")
                else:
                    print(f"\nCorrida: {nome_corrida}")
                    print(f"Equipe: {nome_equipe}\n")
                    
                    cps_registrados = []
                    for p in passagens:
                        if p[0] == cod_corrida and p[1] == num_equipe:
                            cps_registrados.append(p[2])
                            
                    if len(cps_registrados) == 0:
                        print("A equipe ainda não registrou nenhum checkpoint nesta corrida.")
                    else:
                        print("Checkpoints registrados:\n")
                        cps_registrados.sort()
                        for cp in cps_registrados:
                            print(cp)

            elif opcao_acompanhamento == "0":
                break
            else:
                print("\nOpção inválida!")
                
    elif opcao_principal == "0":
        print("\nSaindo do sistema...")
        break
    else:
        print("\nOpção inválida! Tente novamente.")
