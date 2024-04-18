from time import sleep

menu = """
====MENU====
[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair
==>
"""
saldo = 0
extrato = " "
LIMITE_SAQUE = 3
numero_saque = 0
limite = 500

while True:
    sleep(2)
    opcao= input(menu)


    if opcao == 'd':
        valor = float(input('Digite o valor desejado para depósito:R$ '))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print('Operação falhou. Valor informado é inválido!!')

    elif opcao == 's':
        valor =float(input('Digite o valor desejado para saque:R$ '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUE
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

    elif opcao == 'e':

        if extrato =='':
            print("==========EXTRATO==========")
            print("Não foram realizadas transações")
            print('===========================')
        else:
            print("==========EXTRATO==========")
            print(extrato)
            print(f"\nSaldo R$: {saldo:.2f}\n")
            print('===========================')

    elif opcao == 'q':
        break

    else:
        print('Falhou!! Digite uma operação válida!!')

