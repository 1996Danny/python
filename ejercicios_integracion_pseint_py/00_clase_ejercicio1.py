
# 3. solicitar al usuario un numero 
# y mostrar si es par o impar.

numero = int(input("Ingrese un número: "))

# % para obtener el modulo o restor de una división.
if numero % 2 == 0:
    print(f"el número {numero} es par")
else:
    print(f"el número {numero} es impar")