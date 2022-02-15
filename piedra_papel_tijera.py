from random import randint

j1 = input("Bienvenido al juego de piedra, papel o tijera...\n\nSelecciona una de las opciones: ")
rj1 = 0
rj2 = 0
fin ="y"
fin2 = ""
print(f"Has elegido: {j1}")

while fin == "y" or fin2 == "y":
    if j1 != "":
        if fin2 == "y":
            j1 = input("Selecciona una de las opciones: ")
        
        resultado = randint(1,3)
        
        # 1 = PIEDRA
        if resultado == 1 and j1 == "piedra":
            print("Contra: piedra")
            print("Empate... :|")
        elif resultado == 1 and j1 == "papel":
            print("Contra: piedra")
            print("Has ganado :(")
            rj1 += 1
        elif resultado == 1 and j1 == "tijera":
            print("Contra: piedra")
            print("Has perdido ;)")
            rj2 += 1
        # 2 = PAPEL
        elif resultado == 2 and j1 == "piedra":
            print("Contra: papel")
            print("Has perdido ;)")
            rj2 += 1
        elif resultado == 2 and j1 == "papel":
            print("Contra: papel")
            print("Empate... :|")
        elif resultado == 2 and j1 == "tijera":
            print("Contra: papel")
            print("Has ganado :(")
            rj1 += 1
        # 3 = TIJERA
        elif resultado == 3 and j1 == "piedra":
            print("Contra: tijera")
            print("Has ganado :(")
            rj1 += 1
        elif resultado == 3 and j1 == "papel":
            print("Contra: tijera")
            print("Has perdido ;)")
            rj2 += 1
        elif resultado == 3 and j1 == "tijera":
            print("Contra: tijera")
            print("Empate... :|")

    print(f"Vamos {rj1} - {rj2}")
    fin = ""
    fin2 = input("Otra partida?(y/n): ")

print("Gracias por jugar :3 <3")