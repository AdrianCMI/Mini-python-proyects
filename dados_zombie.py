from random import randint, sample

# Introduccion
inicio = input("Bienvenido a Dados Zombies, un juego basado en dados que ganara el que obtenga mas puntos\nEl juego empieza con 13 dados (6 de color verde, 4 de amarillo y 3 de rojo) y va por turnos, siempre se van a tirar 3 dados a la vez y en cada dado hay:\n- Cara cerebro: +1 prunto\n- Cara pies: tiras de nuevo\n- Cara zombie: cuando tengas 3 de estos moriras\n(Presiona enter para empezar...)")


# Color de los dados
def color_random(n):
    if n <= 6:
        n = "verde"
    elif 6 < n <= 10:
        n = "amarillo"
    else:
        n = "rojo"
    print(n)


# Coger los colores
def coger_dados():
    global dado1, dado2, dado3

    dados = sample(range(1,14),3)
    
    dado1 = int(dados[0])
    dado2 = int(dados[1])
    dado3 = int(dados[2])
    
    
# Cara de los dados
def cara_random(x):
    if x == "verde":
        x = randint(1,6)
        if x <= 3:
            x = "cerebro"
        elif 3 < x <= 5:
            x = "pies"
        else:
            x = "zombie"
    elif x == "amarillo":
        if x <= 2:
            x = "cerebro"
        elif 2 < x <= 4:
            x = "pies"
        else:
            x = "zombie"
    elif x == "rojo":
        if x == 1:
            x = "cerebro"
        elif 1 < x <= 3:
            x = "pies"
        else:
            x = "zombie"
    print(x)


# Tirar para ver la cara de los dados
def tirar_dados():
    global cara1, cara2, cara3
    cara1 = dado1
    cara2 = dado2
    cara3 = dado3
    
    
    
# Juego
if inicio == "":
    inicio2 = input("Empieza el jugador 1:\nTira los dados...")
    if inicio2 == "":
        coger_dados()
        print("El color de tus dados son: ")
        color_random(dado1)
        color_random(dado2)
        color_random(dado3)
        dado1 = color_random(dado1)
        dado2 = color_random(dado2)
        dado3 = color_random(dado3)
        tirar_dados()
        print("Y su cara es: ")
        cara_random(cara1)
        cara_random(cara2)
        cara_random(cara3)