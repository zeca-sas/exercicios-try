try:
    n1 = int(input("valor 1: "))
    n2 = int(input("valor 2: "))
    resultado = n1 / n2
except ZeroDivisionError:
    print("não é possível dividir por zero seu animal")
except ValueError:
    print("digite apenas numeros inteiros")
except Exception as erro:
    print(f"o erro encontrado foi: {erro}")
else:
    print(f"o resultado é {resultado}")
finally:
    print("operação deu")