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


listar_estudiantes(estudiantes)
crear_estudiantes(estudiantes)
listar_estudiantes(estudiantes)