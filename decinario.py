decimal = input("Ingrese un numero decimal: ")
binario = ""
cociente = int(decimal)


while cociente != 1.0:
    residuo = cociente % 2
    cociente = cociente // 2
    binario = binario + str(residuo)
    
binario = binario + str(residuo)
rev = binario[::-1]
print (rev)