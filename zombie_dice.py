from random import randint, sample


# Introduccion
inicio = input("Bienvenido a Zombie Dice, un juego basado en dados que ganara el que obtenga mas puntos\nEl juego empieza con 13 dados (6 de color verde, 4 de amarillo y 3 de rojo) y va por turnos, siempre se van a tirar 3 dados a la vez y en cada dado hay:\n- Cara cerebro: +1 prunto\n- Cara pie: tiras de nuevo\n- Cara zombie: cuando tengas 3 de estos moriras\n(Presiona enter para empezar...)")


# Variables
dados_total = 13
jp1 = 0
jp2 = 0
jz1 = 0
jz2 = 0

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
def cara_random(x): # las variables p y z no funcionan
    if x <= 6:
        x = "verde"
    elif 6 < x <= 10:
        x = "amarillo"
    else:
        x = "rojo"
    
    if x == "verde":
        x = randint(1,6)
        if x <= 3:
            x = "cerebro"
        elif 3 < x <= 5:
            x = "pie"
        else:
            x = "zombie"
    elif x == "amarillo":
        x = randint(1,6)
        if x <= 2:
            x = "cerebro"
        elif 2 < x <= 4:
            x = "pie"
        else:
            x = "zombie"
    elif x == "rojo":
        x = randint(1,16)
        if x == 1:
            x = "cerebro"
        elif 1 < x <= 3:
            x = "pie"
        else:
            x = "zombie"
    print(x)


# Recuento de dados, puntos, zombies
def calcular(dado,a,b,c):
    global tirar_pie
    
    if dado == "cerebro":
        a -= 1
        b += 1
    elif dado == "zombie":
        a -= 1
        c += 1
    elif dado == "pie":
        tirar_pie = "y"
        


# Juego
while dados_total >= 0 and jz1 or jz2 <= 3:
    inicioj1 = input("\n\nLe toca al jugador 1:\nTira los dados...")
    
    coger_dados()
    print("\nEl color de tus dados son: ")
    color_random(dado1)
    color_random(dado2)
    color_random(dado3)
    cara = input("Siguiente...")
    print("\nY su cara es: ")
    cara_random(dado1)
    cara_random(dado2)
    cara_random(dado3)
    calcular(dado1,dados_total,jp1,jz1)
    calcular(dado2,dados_total,jp1,jz1)
    calcular(dado3,dados_total,jp1,jz1)
    print(f"Ahora quedan {dados_total} dados")
    print(f"Tienes {jp1} puntos")
    if jz1 != 0:
        print(f"Aunque tienes {jz1} zombies")
    elif jz1 == 0:
        print("No tienes ningun zombie :)")
    while dado1 == "pie" or dado2 =="pie" or dado3 == "pie" and tirar_pie == "y":
        
        tirar_pie = input("\n\n¿Quieres tirar otra vez?(y/n): ")
        
        if tirar_pie == "y":
            
            coger_dados()
            print("\nEl color de tus dados son: ")
            color_random(dado1)
            color_random(dado2)
            color_random(dado3)
            cara = input("Siguiente...")
            print("\nY su cara es: ")
            cara_random(dado1)
            cara_random(dado2)
            cara_random(dado3)
            calcular(dado1,dados_total,jp1,jz1)
            calcular(dado2,dados_total,jp1,jz1)
            calcular(dado3,dados_total,jp1,jz1)
            print(f"Ahora quedan {dados_total} dados")
            print(f"Tienes {jp1} puntos")
            if jz1 != 0:
                print(f"Aunque tienes {jz1} zombies")
            elif jz1 == 0:
                print("No tienes ningun zombie :)")
        elif tirar_pie == "n":
            break
            
    inicioj2 = input("\n\nAhora le toca al jugador 2:\nTira los dados...")
    coger_dados()
    print("\nEl color de tus dados son: ")
    color_random(dado1)
    color_random(dado2)
    color_random(dado3)
    cara = input("Siguiente...")
    print("\nY su cara es: ")
    cara_random(dado1)
    cara_random(dado2)
    cara_random(dado3)
    calcular(dado1,dados_total,jp2,jz2)
    calcular(dado2,dados_total,jp2,jz2)
    calcular(dado3,dados_total,jp2,jz2)
    print(f"Ahora quedan {dados_total} dados")
    print(f"Tienes {jp2} puntos")
    if jz2 != 0:
        print(f"Aunque tienes {jz2} zombies")
    elif jz2 == 0:
        print("No tienes ningun zombie :)")
    while dado1 == "pie" or dado2 == "pie" or dado3 == "pie" and tirar_pie == "y":
        
        tirar_pie = input("\n\n¿Quieres tirar otra vez?(y/n): ")

        if tirar_pie == "y":
            coger_dados()
            print("\nEl color de tus dados son: ")
            color_random(dado1)
            color_random(dado2)
            color_random(dado3)
            cara = input("Siguiente...")
            print("\nY su cara es: ")
            cara_random(dado1)
            cara_random(dado2)
            cara_random(dado3)
            calcular(dado1,dados_total,jp2,jz2)
            calcular(dado2,dados_total,jp2,jz2)
            calcular(dado3,dados_total,jp2,jz2)
            print(f"Ahora quedan {dados_total} dados")
            print(f"Tienes {jp2} puntos")
            if jz2 != 0:
                print(f"Aunque tienes {jz2} zombies")
            elif jz2 == 0:
                print("No tienes ningun zombie :)")
        elif tirar_pie == "n":
            break

print("\nHa acabado el juego")
