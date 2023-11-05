import random

def mostrar_adivinanza(adivinanza, opciones, respuesta_correcta):
    print(adivinanza)
    for opcion in opciones:
        print(opcion)

    respuesta_usuario = input("¿Cuál es tu respuesta? (a, b o c): ")

    if respuesta_usuario.lower() == respuesta_correcta:
        print("¡Correcto! Ganaste 10 puntos.")
        return 10
    else:
        print(f"In correcto. La respuesta correcta es {respuesta_correcta.upper()}. Perdiste 5 puntos.")
        return -5

def main():
    adivinanzas = [
        {
            'adivinanza': "Blanca por dentro, verde por fuera. Si quieres que te lo diga, espera.",
            'opciones': ['a) Manzana', 'b) Sandía', 'c) Pera'],
            'respuesta_correcta': 'a'
        },
        {
            'adivinanza': "Tiene ojos pero no puede ver. Tiene una pata pero no puede caminar. ¿Qué es?",
            'opciones': ['a) Pescado', 'b) Pájaro', 'c) Plátano'],
            'respuesta_correcta': 'b'
        },
        {
            'adivinanza': "Aunque me aprietes y me tires al suelo, siempre vuelvo a subir al cielo. ¿Qué soy?",
            'opciones': ['a) Globo', 'b) Cometa', 'c) Avión'],
            'respuesta_correcta': 'a'
        }
    ]

    puntaje = 0

    for adivinanza in adivinanzas:
        puntaje += mostrar_adivinanza(adivinanza['adivinanza'], adivinanza['opciones'], adivinanza['respuesta_correcta'])

    print(f"Tu puntuación final es: {puntaje} puntos.")

if __name__ == "__main__":
    main()