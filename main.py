print("hola bro soy luis")

def sumar(num1,num2):
    total=num1+num2
    print("el resultado es", total)

def restar(num1,num2):
    total=num1-num2
    print("el resultado es", total)

def multiplicar(num1,num2):
    total=num1*num2
    print("el resultado es", total)

def dividir(num1,num2):
    total=num1/num2
    print("el resultado es", total)

while True:
    print("1 sumar")
    print("2 restar")
    print("3 multiplicar")
    print("4 dividir")
    opcion = input("que quieres bro?")
    num1 = int(input("porfavor ingres numero 1:"))
    num2 = int(input("porfavor ingres numero 2:"))
    if opcion=="1":
        sumar(num1,num2)
    elif opcion=="2":
        restar(num1,num2)
    elif opcion=="3":
        multiplicar(num1,num2)
    elif opcion=="4":
        dividir(num1,num2)
    else:
        print("lo siento bro no entendi")
