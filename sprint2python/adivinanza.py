import random

def mostrar_adivinanza(pregunta, opciones, respuesta_correcta):
    print(pregunta)
    for opcion in opciones:
        print(opcion)
    respuesta_usuario = input("Ingresa tu respuesta (a, b o c): ").lower()
    if respuesta_usuario == respuesta_correcta:
        return 10
    else:
        return -5


def main():
    preguntas = [
        {
            'pregunta': "Blanca por dentro, verde por fuera. Si quieres que te lo diga, espera.",
            'opciones': ['a) Manzana', 'b) Sandía', 'c) Pera'],
            'respuesta_correcta': 'a'
        },
        {
            'pregunta': "Tiene ojos pero no puede ver. Tiene una pata pero no puede caminar. ¿Qué es?",
            'opciones': ['a) Pescado', 'b) Pájaro', 'c) Plátano'],
            'respuesta_correcta': 'b'
        },
        {
            'pregunta': "Aunque me aprietes y me tires al suelo, siempre vuelvo a subir al cielo. ¿Qué soy?",
            'opciones': ['a) Globo', 'b) Cometa', 'c) Avión'],
            'respuesta_correcta': 'a'
        }
    ]


    # Selecciona aleatoriamente dos adivinanzas sin repetición
    adivinanzas_seleccionadas = random.sample(preguntas, 2)

    puntuacion = 0
    for pregunta in adivinanzas_seleccionadas:
        puntuacion += mostrar_adivinanza(pregunta["pregunta"], pregunta["opciones"], pregunta["respuesta_correcta"])

    print("¡Juego terminado!")
    print(f"Tu puntuación final es: {puntuacion}")

if __name__ == "__main__":
    main()
