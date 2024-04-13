from pyfiglet import Figlet
import random

figlet = Figlet()
fuentes = figlet.getFonts()

opcion = input("Escoge una fuente: ")

if opcion.strip() == '':
    opcion=random.choice(fuentes)

figlet.setFont(font=opcion)
print(figlet.renderText("Hola Mundo"))