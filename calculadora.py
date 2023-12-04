# entrenamiento en Python ano 2023
# mi primera calculadora

#saludo
print(  "Hola, esn esta oportunidad verás una calculadora basica")

# se declran  las funciones de las tuplas
def suma(a,b):
    return  a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "Error, no es posible dividir por cero"
    return a / b

# desarrollo del menú

while True:

    print("Opciones:")
    print("Introduce 'suma' para sumar dos números")
    print("Introduce 'resta' para restar dos numreros")
    print("Introduce 'multiplicacion' para multiplicar")
    print("Introduce 'division' para dividi dos numeros")
    print("Introduce 'salir' para finalziar la ejecución del programa")

    # codigo para capturar los datos del usurio utilizando input y una variable

    user_input = input("ingrese aquí: ")
    if user_input == "salir":
        break
    elif user_input in ("suma", "resta", ",ultiplicacion", "division"):
        num1 = float(input("Introduce el primer numero: "))
        num2 = float(input("Introduce el segundo numero: "))
        
        if user_input == "suma":
            print("El resultado: ", suma(num1, num2))

        elif user_input == "resta":
                print ("El resultado: ", resta(num1, num2))
        elif user_input == "multiplicacion":
                print (" El resultado: ", multiplicacion(num1 , num2))
        elif user_input == "division":
                print ("El resutlado: ", division(num1, num2)) 

        else:
            print ("opción no valida")



