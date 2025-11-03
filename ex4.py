def verificar_senha(senha):
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
    if not any(char.isdigit() for char in senha):
        print("A senha deve conter pelo menos um número.")
    print("Senha válida!")

# Programa principal
try:
    senha = input("Digite sua senha: ")
    verificar_senha(senha)

except verificar_senha as erro:
    print(f"Erro: {erro}")

else:
    print("Verificação concluída com sucesso!")

finally:
    print("Programa encerrado.")