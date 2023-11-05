import random

def mostrar_adivinanza():
    adivinanza = "Blanca por dentro, verde por fuera. Si quieres que te lo diga, espera."
    opciones = ['a) Manzana', 'b) Sandía', 'c) Pera']
    print(adivinanza)
    for opcion in opciones:
        print(opcion)

    respuesta_correcta = 'a'

    respuesta_usuario = input("¿Cuál es tu respuesta? (a, b o c): ")

    if respuesta_usuario.lower() == respuesta_correcta:
        print("¡Correcto! La respuesta es Manzana.")
    else:
        print("Incorrecto. La respuesta correcta es Manzana.")

if __name__ == "__main__":
    mostrar_adivinanza()