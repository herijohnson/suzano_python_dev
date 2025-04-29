menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso!")
    else:
        print("\n Operação falhou! O valor informado é invalido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n Operação falhou! Voçê não tem saldo suficiente.")
    elif excedeu_limite:
        print("\n Operação faalhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("\n Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso!")
    else:
        print("\n Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n Extrato")
    print("Não foram realizadas movimentaçãoes." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Depósito: "))
        saldo = 0 + valor
        extrato = (valor, saldo)
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Saque: "))

        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


main()