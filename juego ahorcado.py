#importa la librería random
import random

#listado de palabras para adivinar
palabras = ["cassa", "abuelo", "comida", "futbol", "voleyball"]

# funcion para seleccionar una palabra al azar 
def seleccionar_palabra():
    return random.choice(palabras)

#funcion para mostrar la palabra oculta con letras adivinadas
def mostrar_palabra(palabra, letras_avidinadas):
    palabra_mostrada =""
    for letra in palabra:
        if letra in letras_avidinadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += "_"
    return palabra_mostrada


    