from random import randint

numero1=int(input("ingresa primer numero"))
numero2=int(input("ingresa segundo numero"))

numerojugador =randint(numero1,numero2)

print(f"numero jugador: {numerojugador} ")

if numerojugador%2==0:
    print("el numero es par")
else:
    print("el numero es impar")