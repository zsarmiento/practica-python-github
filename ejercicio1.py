# try: 
#     nombre = input("ingrese un nombre: ")
#     edad = int(input("ingrese su edad: "))
#     altura = 1.69
#     activo = True 
#     print (f"hola {nombre} tu edad es {edad}")
#     if edad >18:
#         print("eres mayor de edad")
#     elif edad == 18:
#         print("tienes 18 años y eres mayor de edad")
#     else:
#         print("eres menor de edad")
# except:
#     print("Intenta nuevamente ingresando datos validos")
   

# contador = 1

# while contador <=5:
#     print (contador)
#     contador +=1


opcion = 0
while opcion != 4: 
    print ("-----Menu principal-----")
    print("1. Saludar")
    print("2. Sumar dos numeros")
    print("3. Mostrar numeros del uno al 5")
    print("4. Salir")


    try: 
        opcion = int(input("Seleccione la opcion "))
        if opcion ==1 :
            
            nombre = input("Ingrese su nombre: ")
            print(f"Hola {nombre}")
        elif opcion ==2: 
            num1= int(input("Ingrese primer numero: "))
            num2= int(input("Ingrese segundo numero: "))
            print(f"la suma de {num1} y {num2} es igual a {num1+num2}")
        elif opcion ==3: 
            conteo =1
            while conteo <=5:
                print(conteo)
                conteo +=1
        elif opcion ==4: 
            print("ha escogido salir, gracias")
        else: 
            print("no es una opcion del menu, vuelva a intentarlo seleccionando una opcion valida")
        


    except:
        print(" intente de nuevo debe ingresar un numero")