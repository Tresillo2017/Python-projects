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


print("Programa que analiza una palabra")
print("Escribe la palabra ", bcolors.OKBLUE)
palabra =input() # Informatica
print(bcolors.ENDC)
caracteres = len(palabra[:])
print("La palabra", bcolors.OKBLUE,"'", palabra,"'", bcolors.ENDC, "Tiene", caracteres, "Letras", bcolors.ENDC)
print("La primera letra es", bcolors.OKGREEN, palabra[0], bcolors.ENDC)
print("La ultima letra es", bcolors.OKGREEN, palabra[-1], bcolors.ENDC)
print("Las dos primeras letras son", bcolors.OKGREEN, palabra[0:2], bcolors.ENDC)
print("Las dos ultimas letras son", bcolors.OKGREEN, palabra[9:], bcolors.ENDC)