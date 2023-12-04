# entrenamiento en Python ano 2023
# adivina el número 

#importa la libreria a utilizar para numeros aleatorios
import random

#saludo
print("**** ADIVINA EL NÚMERO ENTRE 0 Y 10 ****")

#instrucciones
print (" ")
print ("El siguiente programa, tiene como finalidad adivinar ")
print ("el número al azar que se econtrará contenido dentro del rango 0 - 10")
print ("A JUGAR !!")


#captura el número del usuraio para luego comprarlo con el numero aleatorio
# configura el ciclo de oportunidades para ganar
print ("tienes tres oportunidades para adivinar y ganar")
print ("***** ingresa un numero entre 0 y 10 *****")
print ("escribe 'salir' para detener el programa")
while True:
    for rep in range(3): #repite el ciclo 3 veces y se almacena en la variable rep
        # genera el nro aleatorio, dentro del for para que cada vez que se ejecute sea uno distinto
        n_aleatorio = random.randint(0, 10)
        # print (n_aleatorio) #comprobacion
        user_input = input ("ingresa un número : ")   
        if user_input == 'salir':
            break #fianliza el programa
        user_input=int(user_input) #convierte strg a int para poder comparar
            
        if user_input == n_aleatorio: #verifica el número ganador
            print("has ingresado", user_input)
            print ("Felicidades, has ingresado el númer ganador !!!") 
            break
        else: # muesta lo ingresado y el numero aleatorio utilizado
            print("has ingresado", user_input, "y el ganador es, ", n_aleatorio)     
            print("El número ingresado no es coincidente")
            print("llevas,", rep+1,"/3 intentos") #indica la cantidad de intentos
        if rep ==1:
            print ("última oportunidad")
        if rep ==2:
            print ("Lo Sentimos, esta vez no has podido ganar")
    jugar_denuevo = input ("Quieres jugar nuevamente? s/n ")
    if jugar_denuevo.lower() != 's':
        break

print ("Gracias por Jugar, espero te hayas divertido!")








