# =========================================================
# BASE DE DADOS EM MEMÓRIA
# =========================================================
corridas = []
equipes = []
passagens = []

# =========================================================
# FUNÇÕES DE BUSCA E AUXILIARES (REUTILIZÁVEIS E COM RETURN)
# =========================================================

def buscar_corrida_por_codigo(corridas_lista, codigo):
    """Busca e retorna o dicionário da corrida pelo código. Retorna None se não encontrar."""
    for c in corridas_lista:
        if c.get("codigo") == codigo:
            return c
    return None

def buscar_equipe_por_numero(equipes_lista, numero):
    """Busca e retorna o dicionário da equipe pelo número. Retorna None se não encontrar."""
    for eq in equipes_lista:
        if eq.get("numero") == numero:
            return eq
    return None

def verificar_passagem_duplicada(passagens_lista, cod_corrida, num_equipe, checkpoint):
    """Verifica se um determinado checkpoint já foi registrado para a equipe na corrida."""
    for p in passagens_lista:
        if p.get("cod_corrida") == cod_corrida and p.get("num_equipe") == num_equipe and p.get("checkpoint") == checkpoint:
            return True
    return False

def contar_checkpoints_equipe_corrida(passagens_lista, cod_corrida, num_equipe):
    """Conta quantos checkpoints uma equipe registrou em uma determinada corrida."""
    contador = 0
    for p in passagens_lista:
        if p.get("cod_corrida") == cod_corrida and p.get("num_equipe") == num_equipe:
            contador += 1
    return contador

def obter_checkpoints_registrados(passagens_lista, cod_corrida, num_equipe):
    """Retorna uma lista ordenada com os números dos checkpoints registrados por uma equipe."""
    cps = []
    for p in passagens_lista:
        if p.get("cod_corrida") == cod_corrida and p.get("num_equipe") == num_equipe:
            cps.append(p.get("checkpoint"))
    cps.sort()
    return cps

# =========================================================
# OPERAÇÕES DO SUBMENU CORRIDAS
# =========================================================

def cadastrar_corrida(corridas_lista):
    print("\n===== CADASTRO DE CORRIDA =====\n")
    nome_corrida = input("Nome da corrida: ").strip().title()
    qtd_checkpoints = int(input("Quantidade de checkpoints: "))
    
    if qtd_checkpoints <= 0:
        print("\nA quantidade de checkpoints deve ser maior que zero!")
    else:
        novo_codigo = len(corridas_lista) + 1
        corrida = {
            "codigo": novo_codigo,
            "nome": nome_corrida,
            "checkpoints": qtd_checkpoints
        }
        corridas_lista.append(corrida)
        print("\nCorrida cadastrada com sucesso!")

def listar_corridas(corridas_lista, equipes_lista, passagens_lista):
    if len(corridas_lista) == 0:
        print("\nNenhuma corrida cadastrada.")
        return

    print("\n========= LISTA DE CORRIDAS =========\n")
    for c in corridas_lista:
        cod_corrida = c.get("codigo")
        print(f"\nCORRIDA {cod_corrida}: {c.get('nome')}")
        
        print(f"{'Equipe':<8} {'Checkpoints registrados':>23}")
        print("-" * 32)
        
        teve_registro = False
        for eq in equipes_lista:
            num_equipe = eq.get("numero")
            contador = contar_checkpoints_equipe_corrida(passagens_lista, cod_corrida, num_equipe)
                
            if contador > 0:
                print(f"{num_equipe:<8} {contador:>23}")
                teve_registro = True
                
        if not teve_registro:
            print("Nenhum checkpoint registrado ainda.")

def consultar_corrida_por_codigo(corridas_lista, equipes_lista, passagens_lista):
    print("\n===== CONSULTAR CORRIDA =====\n")
    codigo_busca = input("Digite o código da corrida: ").strip()

    if not codigo_busca.isdigit():
        print("\nCódigo inválido.")
        return

    cod_busca_num = int(codigo_busca)
    corrida_encontrada = buscar_corrida_por_codigo(corridas_lista, cod_busca_num)

    if corrida_encontrada:
        cod_corrida = corrida_encontrada.get("codigo")
        print(f"\nCORRIDA: {corrida_encontrada.get('nome')}\n")
        print(f"{'Equipe':<8} {'Checkpoints registrados':>23}")
        print("-" * 32)
        
        teve_registro = False
        for eq in equipes_lista:
            num_equipe = eq.get("numero")
            contador = contar_checkpoints_equipe_corrida(passagens_lista, cod_corrida, num_equipe)
                
            if contador > 0:
                print(f"{num_equipe:<8} {contador:>23}")
                teve_registro = True
                
        if not teve_registro:
            print("Nenhum checkpoint registrado ainda.")
    else:
        print("\nCorrida não encontrada.")

def pesquisar_corrida_por_nome(corridas_lista):
    print("\n===== PESQUISAR CORRIDA =====\n")
    termo = input("Digite o nome ou parte do nome: ").strip().lower()

    encontradas = []
    for c in corridas_lista:
        if termo in c.get("nome").lower():
            encontradas.append(c)

    if len(encontradas) == 0:
        print("\nNenhuma corrida encontrada.")
    else:
        print("\nCorridas encontradas:\n")
        print(f"{'Código':<8}{'Corrida':<37}{'Checkpoints':>11}")
        print("-" * 56)
        for item in encontradas:
            print(f"{str(item.get('codigo')):<8}{item.get('nome'):<37}{str(item.get('checkpoints')):>11}")

def menu_corridas():
    while True:
        print("\n=========== CORRIDAS ===========")
        print("1 - Cadastrar corrida")
        print("2 - Listar corridas")
        print("3 - Consultar corrida por código")
        print("4 - Pesquisar corrida por nome")
        print("0 - Voltar\n")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_corrida(corridas)
        elif opcao == "2":
            listar_corridas(corridas, equipes, passagens)
        elif opcao == "3":
            consultar_corrida_por_codigo(corridas, equipes, passagens)
        elif opcao == "4":
            pesquisar_corrida_por_nome(corridas)
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida!")

# =========================================================
# OPERAÇÕES DO SUBMENU EQUIPES
# =========================================================

def cadastrar_equipe(equipes_lista):
    print("\n===== CADASTRO DE EQUIPE =====\n")
    num_equipe = input("Número da equipe: ").strip()

    if buscar_equipe_por_numero(equipes_lista, num_equipe):
        print("\nErro: Já existe uma equipe cadastrada com esse número!")
    else:
        nome_equipe = input("Nome da equipe: ").strip().title()
        equipes_lista.append({
            "numero": num_equipe,
            "nome": nome_equipe
        })
        print("\nEquipe cadastrada com sucesso!")

def listar_equipes(equipes_lista):
    if len(equipes_lista) == 0:
        print("\nNenhuma equipe cadastrada.")
    else:
        print("\n========================= EQUIPES ===========================\n")
        print(f"{'Número':<8}{'Equipe':<40}")
        print("-" * 48)
        for eq in equipes_lista:
            print(f"{eq.get('numero'):<8}{eq.get('nome'):<40}")

def consultar_equipe_por_numero(equipes_lista):
    print("\n===== CONSULTAR EQUIPE =====\n")
    num_busca = input("Digite o número da equipe: ").strip()
    equipe_encontrada = buscar_equipe_por_numero(equipes_lista, num_busca)

    if equipe_encontrada:
        print("\nEquipe encontrada:\n")
        print(f"{'Número':<8}{'Equipe':<40}")
        print("-" * 48)
        print(f"{equipe_encontrada.get('numero'):<8}{equipe_encontrada.get('nome'):<40}")
    else:
        print("\nEquipe não encontrada.")

def pesquisar_equipe_por_nome(equipes_lista):
    print("\n===== PESQUISAR EQUIPE =====\n")
    termo = input("Digite o nome ou parte do nome: ").strip().lower()

    encontradas = []
    for eq in equipes_lista:
        if termo in eq.get("nome").lower():
            encontradas.append(eq)

    if len(encontradas) == 0:
        print("\nNenhuma equipe encontrada.")
    else:
        print("\nEquipes encontradas:\n")
        print(f"{'Número':<8}{'Equipe':<40}")
        print("-" * 48)
        for eq in encontradas:
            print(f"{eq.get('numero'):<8}{eq.get('nome'):<40}")

def menu_equipes():
    while True:
        print("\n============ EQUIPES ============")
        print("1 - Cadastrar equipe")
        print("2 - Listar equipes")
        print("3 - Consultar equipe por número")
        print("4 - Pesquisar equipe por nome")
        print("0 - Voltar\n")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_equipe(equipes)
        elif opcao == "2":
            listar_equipes(equipes)
        elif opcao == "3":
            consultar_equipe_por_numero(equipes)
        elif opcao == "4":
            pesquisar_equipe_por_nome(equipes)
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida!")

# =========================================================
# OPERAÇÕES DO SUBMENU ACOMPANHAMENTO
# =========================================================

def registrar_passagem(corridas_lista, equipes_lista, passagens_lista):
    print("\n===== REGISTRAR PASSAGEM =====\n")
    cod_corrida = input("Código da corrida: ").strip()
    num_equipe = input("Número da equipe: ").strip()
    checkpoint = input("Checkpoint: ").strip()
    
    if not (cod_corrida.isdigit() and checkpoint.isdigit()):
        print("\nErro: Código da corrida e Checkpoint devem ser numéricos.")
        return
    
    cod_corrida = int(cod_corrida)
    checkpoint = int(checkpoint)
    
    corrida_selecionada = buscar_corrida_por_codigo(corridas_lista, cod_corrida)
    if not corrida_selecionada:
        print("\nErro: A corrida não existe.")
        return
        
    equipe_selecionada = buscar_equipe_por_numero(equipes_lista, num_equipe)
    if not equipe_selecionada:
        print("\nErro: A equipe não existe.")
        return
        
    max_checkpoints = corrida_selecionada.get("checkpoints")
    if checkpoint < 1 or checkpoint > max_checkpoints:
        print(f"\nErro: Checkpoint inválido. Esta corrida tem de 1 a {max_checkpoints} checkpoints.")
        return
        
    if verificar_passagem_duplicada(passagens_lista, cod_corrida, num_equipe, checkpoint):
        print("\nA equipe já registrou este checkpoint nesta corrida.")
    else:
        passagens_lista.append({
            "cod_corrida": cod_corrida,
            "num_equipe": num_equipe,
            "checkpoint": checkpoint
        })
        print("\nPassagem registrada com sucesso!")

def consultar_equipe_na_corrida(corridas_lista, equipes_lista, passagens_lista):
    print("\n===== CONSULTAR EQUIPE NA CORRIDA =====\n")
    cod_corrida = input("Código da corrida: ").strip()
    num_equipe = input("Número da equipe: ").strip()
    
    if not cod_corrida.isdigit():
        print("\nErro: Código da corrida deve ser numérico.")
        return
        
    cod_corrida = int(cod_corrida)
    
    corrida_encontrada = buscar_corrida_por_codigo(corridas_lista, cod_corrida)
    equipe_encontrada = buscar_equipe_por_numero(equipes_lista, num_equipe)
        
    if not corrida_encontrada:
        print("\nErro: Corrida não encontrada.")
    elif not equipe_encontrada:
        print("\nErro: Equipe não encontrada.")
    else:
        print(f"\nCorrida: {corrida_encontrada.get('nome')}")
        print(f"Equipe: {equipe_encontrada.get('nome')}\n")
        
        cps_registrados = obter_checkpoints_registrados(passagens_lista, cod_corrida, num_equipe)
                
        if len(cps_registrados) == 0:
            print("A equipe ainda não registrou nenhum checkpoint nesta corrida.")
        else:
            print("Checkpoints registrados:\n")
            for cp in cps_registrados:
                print(cp)

def menu_acompanhamento():
    while True:
        print("\n========= ACOMPANHAMENTO =========")
        print("1 - Registrar passagem")
        print("2 - Consultar equipe na corrida")
        print("0 - Voltar\n")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            registrar_passagem(corridas, equipes, passagens)
        elif opcao == "2":
            consultar_equipe_na_corrida(corridas, equipes, passagens)
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida!")

# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

def menu_principal():
    print("=================================")
    print("        CAMINHOS DA AVENTURA")
    print("=================================\n")
    print("1 - Corridas")
    print("2 - Equipes")
    print("3 - Acompanhamento")
    print("0 - Sair\n")
    return input("Escolha uma opção: ").strip()

def main():
    while True:
        opcao = menu_principal()
        
        if opcao == "1":
            menu_corridas()
        elif opcao == "2":
            menu_equipes()
        elif opcao == "3":
            menu_acompanhamento()
        elif opcao == "0":
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
