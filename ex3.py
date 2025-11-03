try:
    numero = int(input("escreve um numero ai chefia: "))
    if numero > 10:
        print("Número válido!")
    else:
        print("Número menor ou igual a 10")
except ValueError:
    print("ai n meu chapa")
else:
    print("programa executado com sucesso")
finally:
    print("programa encerrado")