menu = """
[0] - SAIR
[1] - DEPOSITO
[2] - SAQUE
[3] - EXTRATO
 
=> """

saldo = saque_diario = 0
extrato = ""

while True:
    opcao = int(input(menu))
    if  opcao == 0:
        break
    
    elif opcao == 1:
        deposito = float(input("\nDigite o valor que deseja depositar: "))
        if  deposito > 0:
            saldo += deposito
            extrato += f"Depósito: {deposito:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Não foi possível realizar o depósito.")
    
    elif opcao == 2:
        saque = float(input("\nDigite o valor que deseja sacar: "))
        saque_diario += 1
        if  saque_diario > 3:
            print("O limite de saques diários foi atingido.")
            continue
        if  saque <= saldo and saque <= 500:
            saldo -= saque
            extrato += f"Saque: {saque:.2f}\n"
            print("Saque realizado com sucesso!")
        if  saque > saldo:
            print("Não será possível realizar o saque por falta de saldo.")
        if  saque > 500:
            print("Não foi possível realizar o saque. O limite da quantia foi excedido.")
    
    elif opcao == 3:
        print("\n========== EXTRATO ==========")
        if  extrato:
            print(extrato)
        else:
            print("Nenhuma movimentação foi realizada na conta.zn")
        print(f"Saldo atual da conta: R${saldo:.2f}")
        print("==============================")
    
    else:
        print("Opção inválida. Tente novamente.")   
