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

print("Programa que calcula todos los numeros primos desde 2 hasta el numero dado")
print("Escribe un numero")
k = eval(input(bcolors.OKBLUE))
contador = 0
print(bcolors.ENDC)


def esprimo(k):
    if k> 1:
        for n in range(2, k):
            if (k % n) == 0:
                return False
        return True
    else:
        return False

for n in range(2, k):
        if esprimo(n) == True:
            print(bcolors.HEADER, n, bcolors.ENDC, "es primo", bcolors.WARNING,"(True)", bcolors.ENDC)
            contador = contador + 1
            time.sleep(0.1)
        else:
            time.sleep(0)

print(bcolors.BOLD,"en total hay",bcolors.ENDC,bcolors.OKGREEN,contador,bcolors.ENDC,bcolors.BOLD,"numeros que son primos desde el 2 hasta",bcolors.OKCYAN,k,bcolors.ENDC)
