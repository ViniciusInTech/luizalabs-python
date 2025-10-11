menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar():
    global saldo, extrato
    valor_deposito = float(input("informe o valor para deposito: "))
    if valor_deposito <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return
    saldo += valor_deposito
    print("Operacao realizada com sucesso.")
    extrato += f"Deposito: R$ {valor_deposito:.2f}\n"

def saque():
    global saldo, limite, numero_saques, LIMITE_SAQUES, extrato
    valor_saque = float(input("informe o valor para saque: "))
    saldo_insuficiente = saldo < valor_saque
    saque_fora_limite = valor_saque >= limite
    tentativa_invalida = numero_saques >= LIMITE_SAQUES
    valor_invalido = valor_saque <= 0
    if saldo_insuficiente or saque_fora_limite or tentativa_invalida or valor_invalido:
        print("SAQUE NAO AUTORIZADO")
        print("limite de saldo excedido ou valor maior que o limite diario")
        return
    numero_saques += 1
    saldo -= valor_saque
    print(f"Saque de {valor_saque} realizado com sucesso")
    extrato += f"Saque: R$ {valor_saque:.2f}\n"

def exibir_extrato():
    global extrato, saldo
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:

    opcao = input(menu)

    if opcao == "d":
        depositar()
    elif opcao == "s":
        saque()
    elif opcao == "e":
        exibir_extrato()
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")