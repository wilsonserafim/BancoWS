import textwrap


def menu():
    menu = """\n
    *+*+*+*+*+*+*+*+*+* BEM VINDO AO BANCO WS *+*+*+*+*+*+*+*+*+*

    \t[1] para Depositar
    \t[2] para Sacar
    \t[3] para Extrato
    \t[4] Novo Usuario
    \t[5] Nova Conta
    \t[6] Listar de contas
    \t[7] Listar de Usuarios
    \t[8] para Sair;

    *+*+*+*+*+*+*+*+*+**+*+*+*+*+*+*+*+*+**+*+*+*+*+*+*+*+*+**+*+*

    Comando => """
    return int(input(textwrap.dedent(menu)))


def deposito(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito realizado Valor : R$ {valor:.2f}\n"
        print(f" Deposito realizado com sucesso no valor de: {valor:.2f}")
        print(f" Seu saldo é de: {saldo:.2f}")
        input("\nPressione enter para voltar ao menu")
    else:
        print("Operação falhou: O valor informado é inválido")
        input("\nPressione enter para voltar ao menu")

    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("Operação falhou: Saldo insuficiente")
        print(f"Você pode sacar até: R$: {saldo:.2f}")
        print("e até R$500,00 por operação com limite de 3 vezes por dia")
        print("caso tenha Saldo")
        input("\nPressione enter para voltar ao menu")

    elif excedeu_limite:
        print("Operação falhou: O valor informado é maior que seu limite diario de saque, R$500,00")
        input("\nPressione enter para voltar ao menu")

    elif excedeu_saques:
        print("Operação falhou: você ultrapassou o limite diario de saques (3 saques por dia)")
        input("\nPressione enter para voltar ao menu")

    elif valor > 0:
        numero_saques += 1
        saldo -= valor
        extrato += f"Saque realizado Valor : -R${valor:.2f}\n"
        print("Saque realizado com sucesso!")
        print(f"Seu novo saldo é de: R${saldo:.2f}")
        input("\nPressione enter para voltar ao menu")

    else:
        print('\n Operação falhou! O valor informado é inválido.')
        input("\nPressione enter para voltar ao menu")

    return saldo, extrato


def imprimir_extrato(saldo, /, *, extrato):

    print("============================== EXTRATO ==============================")
    print("Não foram realizadas movimentações na conta." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=====================================================================")


def criar_usuario(usuarios):

    cpf = input('Informe o CPF (somente numeros): ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('Ja existe usuario com esse CPF: ')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, N - bairro - cidade/ sigla estado)')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('Usuario registrado com sucesso !')


def filtrar_usuarios(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('informe o CPF do usuario (somente numeros): ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('\n Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('\n Usuario não encontrado, fuluxo de criação de conta encerrado: ')
    return None


def listar_contas(contas):
    if contas == []:
        print("Não existe contas cadastradas volte ao menu e cadastre uma")
        input("\nPressione enter para voltar ao menu")
    else:
        for conta in contas:
            linha = f"""\
                Agencia:\t{conta['agencia']}
                C/C:\t{conta['numero_conta']}
                Tiitular:\t{conta['usuario']['nome']}
            """
            print('=' * 100)
            print(textwrap.dedent(linha))
    input("\nPressione enter para voltar ao menu")


def listar_usuarios(usuarios):
    if usuarios == []:
        print("Não existe Usuarios cadastrados volte ao menu e cadastre")
        input("\nPressione enter para voltar ao menu")
    else:
        for usuario in usuarios:
            linha = f"""\
                Nome:\t{usuario['nome']}
                Data de Nascimento:\t{usuario['data_nascimento']}
                Endereço:\t{usuario['endereco']}
            """
            print('=' * 100)
            print(textwrap.dedent(linha))
    input("\nPressione enter para voltar ao menu")


def main():

    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    
    saldo = 0
    limite = 500
    numero_saques = 0
    usuarios = []
    contas = []
    extrato = ""

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input('Informe o valor do deposito: '))
    
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == 2:

            print('Saque')
            print(f"seu saldo é de: R${saldo:.2f}")
            valor = float(input('Informe o valor a ser sacado: '))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 3:
            imprimir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 7:
            listar_usuarios(usuarios)

        elif opcao == 8:
            break

        else:
            print("Operação inválida, porfavor selecione um comando válido. ")
            input("\n\nPressione enter para continuar para voltar ao menu")


main()