class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("Programa para comprobar si un numero es divisible o no por: 2, 3, 5, 7, 11\n")
print("Escribe un numero", bcolors.OKBLUE)
numero = input()
print(bcolors.ENDC, "\n")

numero = int(numero)
# print(numero)

if (numero % 2 == 0):
    print("El numero", bcolors.OKGREEN , numero , bcolors.ENDC ,bcolors.OKBLUE ,"SI" , bcolors.ENDC , "es divisible por 2")
else:
    print("El numero", bcolors.OKGREEN, numero, bcolors.ENDC, bcolors.WARNING,"NO", bcolors.ENDC, "es divisible por 2")

if (numero % 3 == 0):
    print("El numero", bcolors.OKGREEN, numero, bcolors.ENDC, bcolors.OKBLUE, "SI", bcolors.ENDC, "es divisible por 3")
else:
    print("El numero", bcolors.OKGREEN, numero, bcolors.ENDC, bcolors.WARNING, "NO", bcolors.ENDC, "es divisible por 3")

if (numero % 5 == 0):
    print("El numero", bcolors.OKGREEN, numero, bcolors.ENDC, bcolors.OKBLUE, "SI", bcolors.ENDC, "es divisible por 5")
else:
    print("El numero", bcolors.OKGREEN, numero, bcolors.ENDC, bcolors.WARNING, "NO", bcolors.ENDC, "es divisible por 5")

if (numero % 7 == 0):
    print("El numero", bcolors.OKGREEN, numero, bcolors.ENDC, bcolors.OKBLUE, "SI", bcolors.ENDC, "es divisible por 7")
else:
    print("El numero", bcolors.OKGREEN, numero, bcolors.ENDC, "NO es divisible por 7")

if (numero % 11 == 0):
    print("El numero", bcolors.OKGREEN, numero, bcolors.ENDC, "SI es divisible por 11")
else:
    print("El numero", bcolors.OKGREEN, numero, bcolors.ENDC, "NO es divisible por 11")

