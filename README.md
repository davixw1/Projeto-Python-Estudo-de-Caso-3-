# Projeto Final — Estudo de Caso: Caminhos da Aventura (Quinta Versão)

## Integrantes do Grupo
* Darlan Vasques
* Davi Sanches
* Lucas Barbosa

## Estudo de Caso
**Caminhos da Aventura** — Sistema de Gerenciamento e Acompanhamento de Corridas de Orientação.

## Breve Descrição do Sistema
O sistema gerencia corridas de aventura/orientação, permitindo o cadastro de corridas (com quantidade de checkpoints definidos) e equipes participantes. Durante o evento, realiza o registro e acompanhamento de passagens em tempo real, validando duplicações de passagem e garantindo que equipes não registrem checkpoints fora do intervalo válido.

---

## Principais Funções Criadas

### 1. Funções Auxiliares e de Busca
* `buscar_corrida_por_codigo(corridas_lista, codigo)`: Procura e retorna o dicionário da corrida correspondente.
* `buscar_equipe_por_numero(equipes_lista, numero)`: Procura e retorna o dicionário da equipe pelo número identificador.
* `verificar_passagem_duplicada(...)`: Valida se o registro de passagem já consta no histórico.
* `contar_checkpoints_equipe_corrida(...)`: Contabiliza total de passagens válidas.
* `obter_checkpoints_registrados(...)`: Retorna lista ordenada de checkpoints por equipe em determinada corrida.

### 2. Funções de Submenus e Apresentação
* `menu_principal()`, `menu_corridas()`, `menu_equipes()`, `menu_acompanhamento()`: Responsáveis por exibir opções e capturar dados do usuário.

### 3. Funções de Operações do Sistema
* `cadastrar_corrida()`, `listar_corridas()`, `consultar_corrida_por_codigo()`, `pesquisar_corrida_por_nome()`
* `cadastrar_equipe()`, `listar_equipes()`, `consultar_equipe_por_numero()`, `pesquisar_equipe_por_nome()`
* `registrar_passagem()`, `consultar_equipe_na_corrida()`

---

## Respostas às Questões de Reflexão

### 1. Qual era o maior problema de organização encontrado no código anterior?
O código anterior estava escrito em um único bloco monolithic dentro de loops aninhados `while-if-elif`. Isso gerava duplicação de lógicas (como a busca repetida por corridas e equipes) e tornava o código longo e de difícil manutenção.

### 2. Quais partes do programa foram transformadas em funções?
Todas as ações executáveis dos submenus (cadastrar, listar, consultar e pesquisar) foram transformadas em funções individuais, assim como as exibições de menus e as rotinas repetitivas de busca de dados.

### 3. Quais funções recebem parâmetros?
As funções operacionais recebem as listas do banco de dados como parâmetro (ex: `cadastrar_corrida(corridas_lista)`), e as funções auxiliares recebem os parâmetros necessários para consulta (ex: `buscar_corrida_por_codigo(corridas_lista, codigo)`).

### 4. Quais funções utilizam return?
* `menu_principal()`: Retorna a opção digitada pelo usuário.
* `buscar_corrida_por_codigo()`: Retorna o dicionário da corrida ou `None`.
* `buscar_equipe_por_numero()`: Retorna o dicionário da equipe ou `None`.
* `verificar_passagem_duplicada()`: Retorna `True` ou `False`.
* `contar_checkpoints_equipe_corrida()`: Retorna um número inteiro.
* `obter_checkpoints_registrados()`: Retorna uma lista de números.
* Funções com comandos `return` para interromper o fluxo precocemente em caso de erro de validação.

### 5. Existem funções que poderiam ser reutilizadas em mais de uma operação?
Sim. `buscar_corrida_por_codigo` e `buscar_equipe_por_numero` são reutilizadas na consulta, no registro de passagem e na consulta de acompanhamento.

### 6. Foi encontrado algum código repetido que pôde ser transformado em uma função?
Sim. O loop que procurava uma corrida pelo código e o loop que procurava uma equipe pelo número se repetiam em quase todas as opções do submenu "Acompanhamento" e "Corridas". Eles foram consolidados em funções reutilizáveis de busca.

### 7. O que acontece quando uma função tenta reatribuir uma variável global sem utilizar global?
O Python entende a instrução como a criação de uma **variável local** de mesmo nome. Caso a função tente ler a variável antes da atribuição local, ocorrerá um erro de `UnboundLocalError`.

### 8. Qual é a diferença entre `lista.append(valor)` e `lista = lista + [valor]` quando `lista` é uma variável global?
* `lista.append(valor)`: Modifica o objeto lista existente diretamente na memória (**mutação**). Não requer o uso de `global`.
* `lista = lista + [valor]`: Tenta recriar uma nova lista e reatribuir a variável (**atribuição**). Se feita dentro de uma função sem a palavra-chave `global`, gera um erro `UnboundLocalError`.
