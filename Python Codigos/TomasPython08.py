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

print("Numeros impares entre 1, 1000")
print("Introduce el numero")
numero = eval(input(bcolors.OKBLUE))
resultado = True
print(bcolors.ENDC)
contador =  0 
while resultado:
    for n in range(1,numero):
        if (numero % n == 0):
            print(bcolors.OKCYAN, numero, bcolors.ENDC, "es divisible por", bcolors.WARNING, n, bcolors.ENDC)
            contador = contador + 1
        else:
            resultado = False
print("El numero total de divisores es", bcolors.HEADER, contador, bcolors.ENDC)