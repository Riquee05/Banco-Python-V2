import textwrap


def menu(): 
     
     menu ="""

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [t] Transferir
    [nu] Novo Usuario
    [nc] Criar Nova Conta Corrente
    [lc] Listar Contas
    [q] Sair

    => """
    

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"deposito: R$ {valor: .2f}n\""

    else: print ("Operação falhou, numero invalido ")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saque = numero_saques >= limite_saques
    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo

    if excedeu_saldo:
                print ("Operação invalida, Saldo insuficiente")

    elif excedeu_limite:
                print("Operação invalida, valor excede o limite da Conta ...")

    elif excedeu_saque:
                print("limite de saques diario Excedido, tente novamente mais tarde")

                extrato -= f"saque: R$ {valor: .2f}n\""

    return saldo,extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n=====Extrato=====")
    print("Não foram feitas movimentações " if not extrato else extrato)
    print(f" saldo: R$ {saldo:.2f}")
    print ("=================")

def criar_usuario(usuarios):
     
     cpf = input("Insira o Numero do CPF (Insira somente Numeros): ")
     usuario = filtrar_usuario(cpf,usuarios)

     if usuarios:
          print("Usuario ja Cadastrado")
          return
     
     nome = input("Insira seu Nome: ")
     data_nascimento = input("Insira sua Data de nascimento (Ex DD/MM/AA): ")
     endereco = input("Insira seu endereço (logradouro, nro - bairro - cidade/sigla estado):")

     usuarios.append({"nome":nome , "data_nascimento":data_nascimento, "cpf": cpf, "endereço":endereco})

     print("Usuario Criado com Sucesso")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def filtrar_usuario(cpf,usuarios):
     
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] 
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))    
      

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)


        if opcao == "s":
            valor = float(input("Insira o Valor a ser Sacado: "))

        if opcao == "nu":
            criar_usuario(usuarios) 

        elif opcao == "lc":
            listar_contas(contas)   

        elif opcao =="e":
            exibir_extrato (saldo, extrato=extrato)

        if opcao == "t":
            valor = float(input("Informe o valor a ser transferido "))

            if valor >= saldo:
                print("Valor Superior ao saldo, tente novamente")
            elif valor <= saldo:
                print("Tranferencia realizada com Sucesso")
            extrato = f"saldo: R$ {saldo:.2f}"

            
        if opcao == "q":
            break        

        else:
                print("Obrigado por ultilizar nossos serviços")

main()