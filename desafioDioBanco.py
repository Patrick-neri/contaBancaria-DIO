deposito = 0
saque = 0
saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


bancoContinuar = True



while bancoContinuar:
    opcao = int(input("\n============MENU=================="
        "\n  Bem vindo ao banco digital!" 
        "\n"
        "\nEscolha uma das opções abaixo: " 
        "\n[1] Depositar" 
        "\n[2] Sacar" 
        "\n[3] Extrato" 
        "\n[0] Sair"
        "\n"
        "\n Digite a opção desejada: " 
        ))
    print("\n ==============================\n")
    
    if opcao == 1:
        deposito = float(input("Digite o valor que deseja depositar: "))
        if deposito >= 0:
            saldo += deposito
            
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Você depositou R${deposito: .2f}")
        else:
           print("Não é possível depositar valor menor que 0")

    elif opcao == 2:
        numero_saques += 1

        if numero_saques <= LIMITE_SAQUES:
            saque = float(input("Digite o valor que deseja sacar: "))
            if saldo > 0:
                if saque <= 500:
                    
                    extrato += f"Saque: R$ {saque:.2f}\n"
                    saldo -= saque
                    print("Sacando...")
                else:
                    print("Valor limite de saque é de R$ 500,00. \n Por favor, digite um valor menor que R$ 500,00")
            else:
                print("Saldo insuficiente para saque")
        else:
            print("Limite diário de saque foi atingido")



    elif opcao == 3:
        print("\n============ EXTRATO =================")
        print(extrato)
        saldo
        print(f"Saldo: R${saldo: .2f}")
        print("\n=====================================")

    elif opcao == 0:
        print("Saindo")    
        break
    else:
        print("Digite uma opção válida")

        