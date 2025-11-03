try:
    saldo = float(input("Digite o saldo da conta: "))
    valor = float(input("Digite o valor da transferência: "))

    if valor > saldo:
        raise ValueError("Saldo insuficiente.")
    else:
        saldo -= valor
        print(f"Transferência realizada com sucesso! Saldo atual: R${saldo:.2f}")

except ValueError as erro:
    print(f"Erro: {erro}")

else:
    print("Operação concluída sem erros!")

finally:
    print("Programa encerrado.")