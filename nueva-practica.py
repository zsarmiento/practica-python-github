# for i in range (1,6):
#     print (i)



# contador =1

# while contador <=5: 
#     print(contador)
#     contador+=1


# nombres =["Juan","isidora","Maria"]

# print(nombres[0])

# for nombre in nombres:
#     print(nombre)


# #acumuladores
# numeros =[10, 20, 30, 40]


# suma =0

# for n in numeros:
#     suma +=n
#     print(f"el total de la suma es{suma}")

# notas = [3,5,7,2,9]

# contador =0

# for nota in notas:
#     if nota >=5:
#         contador+=1

# print(f"El total de chicos aprobados es {contador}")

# notas=[]

# for i in range(3):
#     nota = float(input("ingrese una nota: "))
#     notas.append(nota)

# suma =0
# for n in notas:
#     suma +=n

# def promedio ():
#     prom = suma/len(notas)
#     print(f"el promedio es {prom}")


# promedio()

# persona = []

# persona.append({"nombre": "marcela", "edad": 24})
# persona.append({"nombre": "mauricio", "edad": 45})

# for p in persona:
#     print(p["nombre"], p["edad"])





# with open("datos.txt","r") as archivo:
#     contenido = archivo.read()
#     print(contenido)





usuarios=[]

while True:
    print("\n------Menu-------")
    print("1. Registrar ususario")
    print("2. Mostrar usuario")
    print("3. Guardar en archivo")
    print("4. Salir")


    opcion = int(input("Selecicone una opcion 2:"))

    if opcion ==1:
        nombre = input("Ingrese su nombre: ")
        edad = input("Ingrese su edad: ")

        usuario = {
            "nombre": nombre, 
            "edad": edad
            }

        usuarios.append(usuario)
    elif opcion==2:
        for u in usuarios:
            print(u["nombre"], u["edad"])

    elif opcion ==3: 
        with open("usuarios.txt", "w") as archivo: 
            for u in usuarios: 
                archivo.write(u["nombre"]+","+u["edad"]+"\n")
        print("Datos Guardados")

    elif opcion ==4: 
        print("programa finalizado ")
        break

    else: 
        print("opcion invalida")