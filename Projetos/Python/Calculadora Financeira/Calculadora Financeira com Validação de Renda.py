# Função para obter renda
def obter_renda():
    while True:
        rd = input("Escreva sua renda: R$")
        if v_renda(rd):
            return float(rd)

# Função de validar renda
def v_renda(renda):
    limite_inferior = 1320
    limite_superior = 10000

    try:
        renda = float(renda)

        if renda < limite_inferior:
            print("A renda inserida é inferior ao limite mínimo permitido (R$1320.00).")
            return False
        elif renda > limite_superior:
            print("A renda inserida é superior ao limite máximo permitido (R$10000.00).")
            return False
        else:
            print("A renda inserida está dentro dos limites permitidos.")
            return True

    except ValueError:
        print("Por favor, insira um valor númerico para a renda.")

# Função de calcular empréstimo
def calcular_emprestimo(renda):
    if renda:
        valor_emprestimo = float(input("Digite o valor do empréstimo desejado: "))
        prazo_meses = int(input("Digite o prazo em meses: "))

        taxa_juros_anual = 0.08  # 8% de taxa de juros anual

        taxa_juros_mensal = taxa_juros_anual / 12

        prestacao = (valor_emprestimo * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -prazo_meses)

        total = prazo_meses * prestacao

        print(f"O valor da prestação mensal é: R${prestacao:.2f}")
        print("Total a pagar:R$"+ f"{total:.2f}")
        return False
    else:
        print("A validação da renda falhou. Não é possível prosseguir com o empréstimo")
        return True

# Função para obter nome
def obter_nome():
    try:
        while True:
            us = input("Insira seu nome: ")
            if v_nome(us):
                return us
    except ValueError:
        print("Erro no dado inserido!!")

# Função de validar nome
def v_nome(nome):
    try:
        if nome.replace(" ", "").isalpha():
            print("Nome válido.")
            return True
        else:
            print("Nome inválido. Por favor, insira apenas letras.")
            return False
    except ValueError:
        print("Erro no dado inserido!!")

# Função impirir
def imprimir(nome, renda):
    print("Caro/Cara "+ nome +f" sua renda mensal é {renda:.2f}")


# Obtém o nome do usuário
nome_usuario = obter_nome()

# Obtém a renda do usuário
renda_usuario = obter_renda()

# Mostrar o nome e a renda
imprimir(nome_usuario, renda_usuario)

# Calcula o empréstimo com base na renda obtida
emprestimo = calcular_emprestimo(renda_usuario)




