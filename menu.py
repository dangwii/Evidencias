def opcion1():
    print("Has seleccionado la opción 1.")
    decimal = int(input("Ingrese un numero decimal: "))  
    binario = ""
    cociente = decimal

    while cociente != 0:  
        residuo = cociente % 2
        cociente = cociente // 2
        binario = str(residuo) + binario 

    print("Binario:", binario)

def opcion2():
    print("Has seleccionado la opción 2.")
    binario = input("Ingrese un numero binario: ")
    decimal = 0
    base = 1

    for bit in binario[::-1]:
        if bit == '1':
            decimal += base
        base *= 2

    print("Decimal:", decimal)

def opcion3():
    print("Has seleccionado la opción 3.")
    num1 = int(input("Ingrese un numero: ")) 
    num2 = int(input("Ingrese otro numero: "))  
    suma = num1 + num2
    print("Suma:", suma)

    resta = num1 - num2
    print("Resta:", resta)

    multiplicacion = num1 * num2
    print("Multiplicación:", multiplicacion)

    division = num1 / num2
    print("División:", division)

    resto = num1 % num2
    print("Resto:", resto)

while True:
    print("Menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        opcion3()
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

