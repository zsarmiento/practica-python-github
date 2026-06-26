# este programa es una calculadora de gastos personales

#variables

total =0
gastos = []
variable = True
seleccion = 0
buscar_categoria =""

#funciones


def analizar_gasto(pres,gas,cat):
    calculo = (gas/pres)
    if calculo > 0.5:
        print(f"el gasto en la categoria {cat} esta por encima del 50%")
    elif calculo >= 0.2:
        print(f"el gasto en la categoria {cat} es moderado")
    else: 
        print(f"el gasto en categoria {cat} es saludable")

def mostrar_resumen(gastw, tot):
    print("----Resumen------")
    for item in gastw:
       print(f"{item["cat"]}-{item["mont"]}")
    print(f"el total es: {tot}")    
        
def agregar_gastos(mont,cat):
    agregar = {
        "mont": mont,
        "cat": cat
    }
    gastos.append(agregar)

def filtrar_categoria(lista,categoria):
    filtrados = []
    total_filtrados = 0
    for item in lista:
        if item["cat"]==categoria:
            filtrados.append(item)
            total_filtrados += item["mont"]
        
        
    if total_filtrados == 0:
        print(f"la categoria {categoria} buscada no existe")
    print(filtrados)
    print(f"el total de la categoria {categoria} es {total_filtrados} ")

def imprimir_menu():
    print("-----Menu------")
    print("1. Agregar nuevo gasto \n 2. Consultar gastos por categoria \n 3. Ver resumen toal \n 4. Salir")
    while True: 
        try: 
            select = int(input("Ingrese opcion del menu: "))
            return select
        except:
            print("ingrese un valor entre 1 y 4")
#logica


while True:

    seleccion = imprimir_menu()


    if seleccion == 1: 
        if 'presupuestar' not in locals(): # Esto verifica si la variable existe
            while True:
                try:
                    presupuestar = float(input("Ingresa el presupuesto: "))
                    break
                except:
                    print("Error: debe ser un número")
        
        # 2. Resetear la variable de control antes de entrar al bucle
        variable = True



        while variable ==True: 

            categoria = input("Ingrese la categoria: ")
            while True: 
                try: 
                    gasto = float(input("Ingrese el monto del gasto: "))
                    break
                except:
                    print("el gasto a ingresar debe ser un numero entero positivo")
            agregar_gastos(gasto,categoria)
            total+=gasto
            analizar_gasto(presupuestar,gasto,categoria)
            
            while True: 
                continuar = input("desea continuar ingresando gastos? y/n: ").lower()
                if continuar =="n":
                    mostrar_resumen(gastos,total)
                    variable = False
                    break
                elif continuar == "y":
                    break
                else:
                    print("ingrese un dato valido y/n: ")

    elif seleccion ==2: 
        buscar_categoria = input("Escribe la categoria a buscar")
        filtrar_categoria(gastos,buscar_categoria)
    elif seleccion ==3: 
        print(gastos)
    else: 
        print("ha seleccionado salir")
        break

        
        






        