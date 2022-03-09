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
    
lista = list()
espacios = 0
print(bcolors.BOLD, "Programa que calcula la longitud de un texto", bcolors.ENDC)
print("Introduce el texto")
texto = input(bcolors.OKCYAN)
print(bcolors.ENDC)
# print(lista)
for i in texto:   
    if i == " ": 
        espacios += 1      

print("El texto tiene", bcolors.OKGREEN, espacios+1, bcolors.ENDC, "palabras")