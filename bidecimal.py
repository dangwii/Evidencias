binario = input("Ingrese un numero binario: ")
decimal = 0
base = 1

for bit in binario[::-1]:
    if bit == '1':
        decimal += base
    base *= 2

print(decimal)