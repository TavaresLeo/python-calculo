menu = """
    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Saldo
    [4] Transferir
    [5] Sair

=> """

saldo = 0
limite = 1500 
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor = ""
transferir = 300

while True:
    opcao = input(menu)

    if opcao == "0":
        valor = float(input("informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("A operação falhou! O valor informado é inválido.")

    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        execedeu_limite = valor > limite

        execedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif execedeu_limite:
            print("Operação falhou! O valor do saque execede o limite")

        elif execedeu_saques:
            print("Operação falhou! Número máximos de saques diários foi excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else: 
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("====================")

    elif opcao == "3":
        print(f"Seu saldo é: R$ {saldo:.2f}\n")
        print("====================")

    elif opcao == "4":
        transferir = float(input("informe o valor da sua transferência: "))

        if transferir > 0 and transferir <= saldo:
            saldo -= transferir
            extrato += f"Transferência: R$ {transferir:.2f}\n"
            saldo -= transferir
            print(f"\nTransferência realizada com sucesso!")
            print("====================")
        
        elif transferir <= 0:
            print("A operação falhou! O valor informado é inválido.")

        else:
            print("A operação falhou! Saldo insuficiente para realizar a transferência.")

      
    elif opcao == "5":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")