menu = """
+*+*+*+* BEM VINDO AO BANCO WS +*+*+*+*

                MENU
        Pressione:
        [1] para Depositar;
        [2] para Sacar;
        [3] para Extrato;
        [4] para Sair;

+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*
"""
saldo = 100
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print('Deposito')
        valor = float(input('Informe o valor a ser depositado: '))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito realizado Valor : R$ {valor:.2f}\n"
            print(f" Deposito realizado com sucesso no valor de: {valor:.2f}")
            print(f" Seu saldo é de: {saldo:.2f}")
        else:
            print("Operação falhou: O valor informado é inválido")
            print("Escolha uma nova Opção")

    elif opcao == 2:

        if numero_saques <= LIMITE_SAQUES:
            print('Saque')
            #print(f"seu saldo é de: R${saldo:.2f}")
            valor = float(input('Informe o valor a ser sacado: '))
            if valor <= 0:
                print("Operação falhou: O valor deve ser maior que zero")
            elif valor > limite:
                print("Operação falhou: O valor informado é maior que seu limite diario de saque, R$500,00")
            elif valor > 0 and valor > saldo:
                print("Operação falhou: Saldo insuficiente")
                print(f"Você pode sacar até: R$: {saldo:.2f}")
            else:
                numero_saques += 1
                saldo -= valor
                extrato += f"Saque realizado Valor : -R${valor:.2f}\n"
                print("Saque realizado com sucesso!")
                print(f"Seu novo saldo é de: R${saldo:.2f}")
        else:
            print("Operação falhou: você ultrapassou o limite diario de saques (3 saques por dia)")

    elif opcao == 3:
        print("============================== EXTRATO ==============================")
        if extrato == "":
            print("Não foram realizadas movimentações na conta.")
        else:
            print(extrato)
        print(f"Saldo: R$ {saldo:.2f}\n")
        print("=====================================================================")

    elif opcao == 4:
        break

    else:
        print("Operação inválida, porfavor selecione um comando válido. ")
