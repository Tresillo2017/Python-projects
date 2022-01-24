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
n = eval(input(bcolors.OKBLUE))
numero = n-1
print(bcolors.ENDC)

for p in range(1, numero):
    if (numero % p != 0):
        print(bcolors.OKCYAN, p, bcolors.ENDC, "es primo", bcolors.HEADER, n, bcolors.ENDC)
