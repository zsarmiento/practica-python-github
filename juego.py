from random import randint

numero1=int(input("ingresa primer numero"))
numero2=int(input("ingresa segundo numero"))

numerojugador =randint(numero1,numero2)


if numerojugador%2==0:
    print("el numero es par")
else:
    print("el numero es impar")
    numerojugador+=1
    if numerojugador>numero2:
        numerojugador-=2

print(f"numero jugador: {numerojugador} ")

print("adivina el numero que escogi")

contador =0
adivinar = False
while contador <=2 or adivinar== False:
    intento=int(input("dame el numero: "))
    if intento == numerojugador:
        print("correcto, el numero es acertado")
        adivinar = True
        contador =3
    else:
        print(f"tu intento es {intento} y el numero que juega es {numerojugador}")
        contador+=1