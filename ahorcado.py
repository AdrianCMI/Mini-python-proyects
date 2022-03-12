import random

#variables
list_palabras = "adrian novia sombra animal oveja aprender ejercicios caballo perro vaca computadora python abeja diente conejo mantel mesa basura escritorio ubuntu gorro parque amuleto cama cuarto descargar curso diario vaso cuadro foto revista esdrujula parlantes radio tutorial platano naranja manzana movil casco ventana silla juegos television nevera modulos cocina timbre lavadora estufa enchufe futbol pelota pizarra cargador factura papel impresora telefono remedio planta vegetal aves luna electricidad copa tiempo google lenguaje internet esposa jarra microondas manual sarten cortina musica pato esternocleidomastoirdeo".split()
palabra_random = random.choice(list_palabras)
letras = len(palabra_random)
palabra_secreta_l = list(letras * "_")
palabra_secreta = ""
posiciones = []
moñigote = 0

#moñigote
def muñeco(moñigote):
    if moñigote == 0:
        print("""
               ___
              |   |
                  |
                  |
                  |
            ______|
        """)
    if moñigote == 1:
        print("""
               ___
              |   |
              O   |
                  |
                  |
            ______|
        """)
    if moñigote == 2:
        print("""
               ___
              |   |
              O   |
              |   |
                  |
            ______|
        """)
    if moñigote == 3:
        print("""
               ___
              |   |
              O   |
              |   |
             /    |
            ______|
        """)
    if moñigote == 4:
        print("""
               ___
              |   |
              O   |
              |   |
             / \  |
            ______|
        """)
    if moñigote == 5:
        print("""
               ___
              |   |
              O   |
             \|   |
             / \  |
            ______|
        """)
    if moñigote == 6:
        print("""
               ___
              |   |
              O   |
             \|/  |
             / \  |
            ______|
        """)
    if moñigote == 7:
        print("""
               ___
              |   |
              O   |
             \|/  |
            _/ \  |
            ______|
        """)
    if moñigote == 8:
        print("""
               ___
              |   |
              O   |
             \|/  |
            _/ \_ |
            ______|
        """)

#palabra_secreta
while "_" in palabra_secreta_l and moñigote < 8:
    letra = input("")
    for pos,char in enumerate(palabra_random):
        if char == letra:
            del palabra_secreta_l[pos]
            palabra_secreta_l.insert(pos,letra)
    if not letra in palabra_random:
        moñigote  += 1
    palabra_secreta = "".join(palabra_secreta_l)
    print(palabra_secreta)
    muñeco(moñigote)
if not "_" in palabra_secreta_l:
    print("Has ganadooo!!!!")
elif moñigote >= 8:
    print(f"HA MUERTOO :C\nLa palabra era: {palabra_random}")