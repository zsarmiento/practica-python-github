# este programa es una calculadora de gastos personales

#variables

total =0
gastos = []
variable = True

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


#logica

while True: 
    try:
        presupuestar = float(input("Ingresa el presupuesto sin comas ni puntos: "))
        break
    except:
        print("el valor ingresado debe ser un entero positivo")


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
    
    






    