import random

jugadas_posibles = ["piedra", "papel", "tijera"]
jugadas_usuario = []
jugadas_programa = []

for _ in range(5):
    # El usuario selecciona una jugada
    jugada_usuario = input("Elige piedra, papel o tijera: ").lower()
    while jugada_usuario not in jugadas_posibles:
        print("Jugada inválida. Por favor, elige piedra, papel o tijera.")
        jugada_usuario = input("Elige piedra, papel o tijera: ").lower()
    
    # El programa genera una jugada aleatoria
    jugada_programa = random.choice(jugadas_posibles)
    
    # Se almacenan las jugadas del usuario y del programa
    jugadas_usuario.append(jugada_usuario)
    jugadas_programa.append(jugada_programa)
    
    # Se determina el resultado de la jugada
    if jugada_usuario == jugada_programa:
        print("Empate. Ambos eligieron", jugada_usuario)
    elif (jugada_usuario == "piedra" and jugada_programa == "tijera") or \
         (jugada_usuario == "papel" and jugada_programa == "piedra") or \
         (jugada_usuario == "tijera" and jugada_programa == "papel"):
        print("Has ganado. {} gana a {}".format(jugada_usuario, jugada_programa))
    else:
        print("Has perdido. {} gana a {}".format(jugada_programa, jugada_usuario))

# Se muestra el resultado final del juego
if jugadas_usuario.count("piedra") > jugadas_programa.count("piedra") or \
   jugadas_usuario.count("papel") > jugadas_programa.count("papel") or \
   jugadas_usuario.count("tijera") > jugadas_programa.count("tijera"):
    print("¡Felicidades! Has ganado el juego.")
elif jugadas_usuario.count("piedra") == jugadas_programa.count("piedra") and \
     jugadas_usuario.count("papel") == jugadas_programa.count("papel") and \
     jugadas_usuario.count("tijera") == jugadas_programa.count("tijera"):
    print("El juego ha terminado en empate.")
else:
    print("Has perdido el juego. Mejor suerte la próxima vez.")