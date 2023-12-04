# entrenamiento en Python ano 2023
# conversor de peso a dolar basico

#saludo
print(  "*** CONVERSOR DE DIVISAS ***")

# se declran las funciones de las tuplas
def peso_a_dolar(a,b):
    return  a / b
def dolar_a_peso(a,b):
    return a * b

# desarrollo del menú

while True:

    print("Opciones:")
    print("Introduce '1' para convertir de Peso a Dolar")
    print("Introduce '2' para restar Dolar a Peso")
    print("Introduce 'salir' para finalizar el programa")

 # Captura de datos

    user_input = input( 'INDICA EN NUMERO SEGUN LO QUE DESEAS CONVERTIR: ')
    if user_input == 'salir':
        break

    if user_input == '1':
        print ("Has seleccionado la opcion 1 (peso a dolar)")
        num1 = float(input("Introduce la cantidad en $ ")) 
        num2 = float(input(" Introduce el valor de conversion "))
        resultado = peso_a_dolar(num1, num2)
        print ("el Valor convertdio es de USD", resultado, "dolares")
    elif    user_input == '2':
        print ("Has seleccionado la opcion 2 (dolar a peso)")
        num1 = float(input("Introduce la cantidad en USD ")) 
        num2 = float(input(" Introduce la tasa de cambio "))
        resultado = dolar_a_peso (num1, num2)
        print ("el Valor convertdio es de $", resultado, "pesos")

    else:
        print ("el numero de menu ingresado no es correcto")

    

