print("Adivina adivinanza, Blanca por dentro, verde por fuera. Si quieres que te lo diga, espera.")
puntuacion = 0
opciones = {
'a1': "a: Manzana",
'b1': "b: Sandía",
'c1': "c: Pera",
'op1':'a',
'op2':'b',
'op3':'a',
'a2':'a: Pescado',
'b2':'b: Pájaro',
'c2':'c: Plátano',
'a3':'a: Globo',
'b3':'b: Cometa',
'c3':'c: Avión'
}

print(opciones['a1'])
print(opciones['b1'])
print(opciones['c1'])

opcionR = input()

if opcionR == opciones['op1']:
    print("Opción correcta")
    puntuacion = puntuacion + 10
else:
    print("Opción incorrecta")
    puntuacion = puntuacion + 5

print('Tiene ojos pero no puede ver. Tiene una pata pero no puede caminar. ¿Qué es?')

print(opciones['a2'])
print(opciones['b2'])
print(opciones['c2'])

opcionR = input()

if opcionR == opciones['op2']:
    print("Opción correcta")
    puntuacion = puntuacion + 10
else:
    print("Opción incorrecta")
    puntuacion = puntuacion + 5

print("Aunque me aprietes y me tires al suelo, siempre vuelvo a subir al cielo. ¿Qué soy?")

print(opciones['a3'])
print(opciones['b3'])
print(opciones['c3'])

opcionR = input()

if opcionR == opciones['op1']:
    print("Opción correcta")
    puntuacion = puntuacion + 10
else:
    print("Opción incorrecta")
    puntuacion = puntuacion + 5

print("Puntuación: ",puntuacion)