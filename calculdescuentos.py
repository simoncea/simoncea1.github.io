#CALCULADORA DE DESCUENTOS
#formula:
#Precio Final = Precio Original - (
# Precio Original * Porcentaje de Descuento / 100)

while True:

    print("*** Calculadora de descuentos ***")
    try:
        #caputrar los datos necesarios
        precio_original =int(input("ingrese el precio original: "))
        if precio_original <= 0:
            raise ValueError ("Error, el nro. no debe ser negativo")
        
        porcentaje_descuento =int(input("ingrese el '%' de descuento: "))
        if porcentaje_descuento <= 0:
            raise 
        #declarar funcion
        precio_final = precio_original - (precio_original * porcentaje_descuento /100)

        #muestra resultados
        print("")
        print("Al valor del prodcuto señalado, con el ", porcentaje_descuento,"'%' de descuento aplicado" )
        print("se obtiene el valor final de: $",precio_final,"pesos.")
        print("")
        #termina el programa
        print("Escribe 'salir' para finalizar el programa.")
        print("Para continuar, presiona 'enter'")
        salir = input()
        if salir == "salir":
            print("El programa se detendrá, hasta pronto")
            break


    except ValueError as error:
        print("Error:", error)
        print("Por favor, ingrese valores válidos.")
