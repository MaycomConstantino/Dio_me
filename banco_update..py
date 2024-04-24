def exibir_menu():
    menu = """
    ====MENU====
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo Usuário
    [cc]\tCadastrar Conta
    [q]\tSair
    ==>
    """
    return input(menu)


def depositar( saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito:\t R${valor:.2f}\n"
            print('Depósito realizado com sucesso!')
        else:
            print('Operação falhou. Valor informado é inválido!!')

        return saldo, extrato

def sacar(*,valor, saldo, extrato, limite_saques, numero_saque, limite):
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= limite_saques
        if excedeu_saldo:
            print("Operação falhou. Saldo indispónivel!!")
        elif excedeu_limite:
            print('Operação falhou. Digite um valor menor que R$500,00.')
        elif excedeu_saques:
            print('Você excedeu o numero de saques do dia!!')
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R${valor:.2f}\n"
            numero_saque += 1
        else:
            print('Operação Falhou. Valor informado indisponível.')
        return saldo, extrato

def exibir_extrato( saldo,/,*, extrato):

        if extrato == '':
            print("==========EXTRATO==========")
            print("Não foram realizadas transações")
            print('===========================')
        else:
            print("==========EXTRATO==========")
            print(extrato)
            print(f"\nSaldo R$: {saldo:.2f}\n")
            print('===========================')
def criar_usuario(usuarios):
    cpf = int(input('CPF: '))
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print('Esse usuario já existe!!')
        return

    nome = str(input('Nome: '))
    data_nascimento = input('Data de nascimento:(dd-mm-ano): ')
    endereco = str(input('Rua - Numero -  Bairro - Cidade/Sigla: '))
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento,'cpf':cpf, 'endereco': endereco})

    print('Usuário criado com sucesso.')

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] ==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta( agencia, nro_conta, usuarios):
    cpf = int(input('Informe o seu CPF: ' ))
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
       print('Conta criada com sucesso!!')
       return {'agencia': agencia, 'nro_conta': nro_conta, 'usuario': usuario}
    else:
        print('Usuário não encontrado, operação encerrada..')

def main():
    saldo = 0
    extrato = " "
    LIMITE_SAQUE = 3
    numero_saque = 0
    limite = 500
    usuarios = []
    agencia = '0001'
    contas = []

    while True:
        opcao = exibir_menu()

        if opcao =='d':
            valor = float(input('Digite o valor do depósito:R$ '))
            saldo , extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Digite o valor do saque:R$ '))
            saldo , extrato = sacar(
                valor = valor,
                saldo = saldo,
                limite = limite,
                numero_saque = numero_saque,
                extrato = extrato,
                limite_saques = LIMITE_SAQUE,
            )

        elif opcao == 'e':
            exibir_extrato( saldo, extrato=extrato)

        elif opcao =='nu':
            criar_usuario(usuarios)

        elif opcao == "cc":
            nro_conta = len(contas)+1
            conta = criar_conta(agencia, nro_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao =='q':
            break

        else:
            print('Operação Inválida, selecione uma opção válida!!')



main()



