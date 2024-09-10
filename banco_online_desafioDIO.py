"""
DESAFIO DE CODIGO DIO
HELDER LOPES V2 ATUALIADO EM 10/09/2024
"""

menu = """
------------BANCO DO POVO------------      VERSAO 1.0
    Digite uma opção:

    [d] Deposito
    [s] Saque
    [e] Extrato
    [q] Sair
    => \n"""

menu2 = """
------------BANCO DO POVO------------      VERSAO 1.0
    Digite uma opção:

    [d] Deposito
    [s] Saque [excedeu limite diario]
    [e] Extrato
    [q] Sair
    => \n"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
depositos = []

while True:
    # caso o limite de saque tenaha sido alcançado ele  exibira o menu 2 informando que o saquw excedeu o limite diario
    if LIMITE_SAQUES > 0:

        opcao = input(menu)
    else:
        opcao = input(menu2)

    """funcao deposito declarada dentro do while para que o mesmo so sera usado
    em tempo de execução do laço.
    é passado o parametro saldo para que a função atribui localmente o valor
    global evitando erro de calculo com none"""

    # FUNCAO DE DEPOSITO
    def deposito(saldo, depositos):
        print(f"Saldo  atual {saldo:.2f}")
        valor_deposito = float(input("Digite o valor que deseja depositar: R$ "))

        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"\nDeposito de R$ {valor_deposito:.2f} realizado com sucesso. ")
            depositos.append(valor_deposito)

        return saldo, depositos

    # FUNCAO DE SAQUE
    def saque(saldo, limite_saques):
        while True:
            valor_saque = 0.00
            # enquanto o limite de 3 saques não forem usados ele repetira a opcao de saque

            if limite_saques <= 0:
                print(
                    f"""
                                        Voce alcançou o limite de [3] saques diários. 
                            Para novos saques, tente amanhã ou procure atendimento nos guichês"""
                )
                break

            print(f"Saldo em conta R$ {saldo:.2f}")

            try:

                valor_saque = float(
                    input("Digite o valor desejado ou [0] para retornar R$ ")
                )
                if valor_saque == 0:
                    break

                # teste para verificar se o valor a ser retirado atende o criterio de 3 saques diarios até 500,00
                if valor_saque <= 500:
                    if saldo <= 0.00:
                        print(
                            f"Saque indisponível. Desculpe, sua conta está SEM SALDO. R$ {saldo:.2f}\n"
                        )
                        break

                    # caso o saldo seja menor que o valor de saque
                    elif saldo < valor_saque:
                        print(f"Saldo insuficiente. Seu saldo é R$ {saldo:.2f}")
                    else:
                        # caso o limite de saldo seja valido ele ira retirar o valor solicitado e reduzira
                        # a quantidade de  saques diarios disponiveis
                        # if limite_saques > 0:
                        saldo -= valor_saque
                        depositos.append(-valor_saque)
                        print(f"Saque\nRetire seu dinhero. R$ {valor_saque:.2f}\n")
                        limite_saques -= 1

                else:
                    print(
                        "Valor saque maximo é R$ 500,00. Digite um valor igual ou menor."
                    )
                    continue

            except:
                print("Entrada invalida. Por favor, digite um valor numerico\n")

        return saldo, limite_saques

    # EXTRATO
    def extrato(depositos):
        sair = "s"

        if len(depositos) > 0:
            while sair == "s":

                saldo = sum(depositos)  # soma das movimentações
                print("")
                for e in depositos:
                    if e < 0:
                        print(f"-R$ {e*(-1):.2f} SAQUE")
                    else:
                        print(f" R$ {e:.2f} DEPOSITO")
                print(
                    f"""--------------------------------
                    SALDO EM CONTA: R${saldo:.2f}"""
                )
                sair = input("Deseja exibir o extrato? [s]im ou [n]ao?")
            return
        else:
            # comment:
            print("\nNão foram realizados movimentações")

    # ------------------------ INICIO ------------------------
    # MENU
    if opcao == "d" or opcao == "D":
        print("---------Depósito---------")
        # é necessario atribuir ao retorno da função as variaveis que quero armazenar. no caso o saldo e o   historico de movimentações
        saldo, depositos = deposito(saldo, depositos)

        print(f"seu saldo fora é {saldo:.2f}")

    elif opcao == "s" or opcao == "S":
        saldo, LIMITE_SAQUES = saque(saldo, LIMITE_SAQUES)
        if LIMITE_SAQUES <= 0:
            print("Não é possivel realizar saques hoje")

    elif opcao == "e" or opcao == "E":
        extrato(depositos)

    elif opcao == "q" or opcao == "Q":
        break

    else:
        print("Operação inválida, por favor digite uma opção")
