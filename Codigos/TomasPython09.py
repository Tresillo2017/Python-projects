import time

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
    
print(bcolors.WARNING,"Si el programa no puede ejeacutarse prueba a instalar el modulo sympy (pip install sympy)", bcolors.ENDC)
time.sleep(2) # Sleep for 3 seconds
from sympy import *



print("Programa que calcula todos los numeros primos desde 2 hasta el numero dado")
print("Escribe un numero")
n = eval(input(bcolors.OKBLUE))
numero = n-1
contador = 0
print(bcolors.ENDC)


for n in range(2, numero):
    if isprime(n) == True:
        print(bcolors.HEADER, n, bcolors.ENDC, "es primo", bcolors.WARNING,"(True)", bcolors.ENDC)
        time.sleep(0.2) # Sleep for 0.2 seconds (for slow computers)
    else:
        contador = contador + 1
print(bcolors.BOLD,"en total hay",bcolors.ENDC,bcolors.OKGREEN,contador,bcolors.ENDC,bcolors.BOLD,"numeros que no son primos desde el 2 hasta",bcolors.OKCYAN,numero,bcolors.ENDC)