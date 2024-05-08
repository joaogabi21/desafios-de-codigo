def criar_usuario (usuarios):
    cpf = (input("Digite seu CPF (somentes números): "))
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print("\nJá existe usuário com esse CPF")
        return
    
    nome = (input("Digite o seu nome: "))
    data_nasc = (input("Digite sua data de nascimento(dd/mm/aa): ")) 
    endereco = (input("Digite seu endereço (logradouro, nº - bairro - cidade/sigla estado): "))
    usuarios.append({"nome":nome, "data_nascimento":data_nasc, "cpf":cpf, "endereco":endereco})
    print("\nUsuário cadastrado com sucesso!")

def filtrar_usuario (cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta (agencia,num_contas,usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": num_contas, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")  

def depositar (deposito,saldo,extrato,/):
    deposito = float(input("\nDigite o valor que deseja depositar: "))
    if  deposito > 0:
        saldo += deposito
        extrato += f"Depósito: {deposito:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Não foi possível realizar o depósito.")
    return (saldo,extrato)

def sacar (*,saque,saque_diario,saldo,extrato):
    saque = float(input("\nDigite o valor que deseja sacar: "))
    saque_diario += 1
    if  saque_diario > 3:
        print("O limite de saques diários foi atingido.")
    elif saque <= saldo and saque <= 500:
        saldo -= saque
        extrato += f"Saque: {saque:.2f}\n"
        print("Saque realizado com sucesso!")
    if  saque > saldo:
        print("Não será possível realizar o saque por falta de saldo.")
    if  saque > 500:
        print("Não foi possível realizar o saque. O limite da quantia foi excedido.")
    return (saldo,extrato,saque_diario)

def consultar_extrato (saldo,/,*,extrato):
    print("\n========== EXTRATO ==========")
    if  extrato:
        print(extrato)
    else:
        print("Nenhuma movimentação foi realizada na conta.zn")
    print(f"Saldo atual da conta: R${saldo:.2f}")
    print("==============================")

menu = """
[0] - SAIR
[1] - CRIAR USUARIO
[2] - CRIAR CONTA
[3] - DEPOSITO
[4] - SAQUE  
[5] - EXTRATO
 
=> """

usuarios = []
AGENCIA = "0001"
num_contas = 1
saldo = saque_diario = 0
extrato = ""

while True:
    opcao = int(input(menu))
    
    if  opcao == 0:
        break
    
    elif opcao == 1:
        criar_usuario(usuarios)
    
    elif opcao == 2: 
        criar_conta(AGENCIA,num_contas,usuarios)
        num_contas += 1

    elif opcao == 3:
        saldo,extrato = depositar(0,saldo,extrato)   
    
    elif opcao == 4:
        saldo,extrato,saque_diario = sacar(saque = 0,saque_diario = saque_diario,saldo = saldo,extrato = extrato)

    elif opcao == 5:
        consultar_extrato(saldo,extrato = extrato)
    
    else:
        print("Opção inválida. Tente novamente.")   
