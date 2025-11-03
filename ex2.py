cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': (0, 0, 255)}

try:
    cor = str(input("escolha uma cor do RGB: ")).lower()
    if cor in cores:
        print(cor["cor"])
except cor in cores:
    print("viaja n")