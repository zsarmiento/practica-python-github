estudiantes = []

def crear_estudiantes(estudiantes):
    nombre =input("Ingrese nombre del estudiante: ")
    edad = int(input("ingrese edad del estudiante: "))
    curso = input("ingrese curso del estudiante")

    estudiante = {
        "nombre" : nombre,
        "edad": edad,
        "curso": curso
    }

    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} ingresado exitosamente")




def listar_estudiantes(estudiantes):
    if len(estudiantes)==0:
        print("listado vacio, no se han creado estudiantes")
    else:
        print("-----------Listado de estudiantes----------")
        for i, estudiante in enumerate(estudiantes):
            print(f"ID:{i}")
            print(f"nombre: {estudiante["nombre"]}")
            print(f"curso: {estudiante["curso"]}")
            print("-------------------------------------")


def actualizar_estudiantes(estudiantes):
    listar_estudiantes(estudiantes)
    modificar = int(input("indique que estudiante quiere modificar: "))
    print(f"Nombre: {estudiantes[modificar]}")

    nuevo_nombre = input("ingrese el nuevo nombre: ")
    nueva_edad = int(input("ingrese nueva edad: "))
    nueva_carrera = input("ingrese nueva carrera: ")

    estudiantes[modificar]["nombre"] = nuevo_nombre
    estudiantes[modificar]["edad"] = nueva_edad
    estudiantes[modificar]["curso"] = nueva_carrera

    print(f"El estudiante {estudiantes[modificar]} ha sido modificado exitosamente")

def eliminar_estudiantes(estudiantes):
    listar_estudiantes(estudiantes)
    while True: 
        eliminar = int(input(f"ingrese id del estudiante: "))
        confirmar = input("Esta seguro que desea eliminar el estudiante? y/n: ")

        if confirmar == "y":
            estudiantes.pop(eliminar)
            print("El estudiante ha sido eliminado")
            break

        elif confirmar == "n": 
            print("intentalo de nuevo")

        else: 
            print("ingresa una opcion y/n")



listar_estudiantes(estudiantes)
crear_estudiantes(estudiantes)
actualizar_estudiantes(estudiantes)
eliminar_estudiantes(estudiantes)
listar_estudiantes(estudiantes)