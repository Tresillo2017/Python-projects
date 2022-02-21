

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


print(bcolors.HEADER, "Imprime el valor de x centro")
xc = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)

print(bcolors.HEADER, "Imprime el valor de y centro")
yc = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)

print(bcolors.HEADER, "Imprime el valor de x")
x = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)

print(bcolors.HEADER, "Imprime el valor de y")
x = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)
  
# preguntas_centro()
# preguntas()

def distancia():
    valor = ((x-xc)**2+(y-yc)**2)**0.5
    return distancia
    print("Quieres introducir mas valores (y/n)")
    
    print = distancia()
    
while True:
    sigo = input(bcolors.OKCYAN)
    print(bcolors.ENDC)  
    if sigo == "y" or sigo == "Y":
        print(bcolors.HEADER, "Imprime el valor de x")
        x = eval(input(bcolors.OKBLUE))
        print(bcolors.ENDC)

        print(bcolors.HEADER, "Imprime el valor de y")
        x = eval(input(bcolors.OKBLUE))
        print(bcolors.ENDC)
        distancia(x, y)
    else:
        break

print(bcolors.ENDC)