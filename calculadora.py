# este programa es una calculadora de gastos personales
try:
    presupuestar = int(input("Ingresa el presupuesto sin comas ni puntos: "))
except:
    print("el valor ingresado debe ser un entero positivo")
total =0
gastos = []

def analizar_gasto(pres,gas,cat):
    calculo = (gas/pres)
    if calculo >= 0.5:
        print(f"el gasto en la categoria {cat} esta por encima del 50%")
    elif 0.2>=calculo < 0.5:
        print(f"el gasto en la categoria {cat} es moderado")
    else:
        print(f"el gasto en categoria {cat} es saludable")


while True: 

    categoria = input("Ingrese la categoria: ")
    gasto = int(input("Ingrese el monto del gasto: "))
    gastos_nuevos = {
        "categoria": categoria, 
        "gasto": gasto
    }
    gastos.append(gastos_nuevos)
    total+=gasto
    analizar_gasto(presupuestar,gasto,categoria)
    continuar = input("desea continuar ingresando gastos? y/n: ").lower()
    if continuar =="n":
        for item in gastos:
            print(f"{item["categoria"]}-{item["gasto"]}")
        print(f"total gastos es igual a {total}")
        break






    