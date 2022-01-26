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
        for n in range(2, k): # Define un rango desde 2 hasta k 
            if (k % n) == 0: # Comprueba si k / n su resto da 0
                return False  # No es primo
        return True # Es primo
    else:
        return False # No es primo

for n in range(2, k): # Define un rango desde 2 hasta k
        if esprimo(n) == True: # Si la funcion 'esprimo' da true entra en el bucle
            print(bcolors.HEADER, n, bcolors.ENDC, "es primo", bcolors.WARNING,"(True)", bcolors.ENDC) # Imprime en pantalla que n es primo
            contador = contador + 1 # Suma 1 al contador
            time.sleep(0.1) # Espera 0.1 segundos
        else:
            time.sleep(0) # Espera 0 segundos

print(bcolors.BOLD,"en total hay",bcolors.ENDC,bcolors.OKGREEN,contador,bcolors.ENDC,bcolors.BOLD,"numeros que son primos desde el 2 hasta",bcolors.OKCYAN,k,bcolors.ENDC)
