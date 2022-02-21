from math import *

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

print(bcolors.HEADER, "Introduce el valor del radio")
radio = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)

print(bcolors.HEADER, "Introduce el valor de x centro")
xc = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)

print(bcolors.HEADER, "Introduce el valor de y centro")
yc = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)

print(bcolors.HEADER, "Introduce el valor de x")
x = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)

print(bcolors.HEADER, "Introduce el valor de y")
y = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)



def esta_dentro(xc, yc, x, y, radio):
    distancia = ((x-xc)**2+(y-yc)**2)**0.5 
    if distancia <= radio:
        return "dentro del circulo"
    elif distancia == radio: # abs(distancia - radio) <= 10^(-d) siendo d el numero de digitos decimales
       return "sobre el circulo"
    else:
        return "fuera del circulo"
    
while True:
    print(bcolors.OKBLUE, "Esta", esta_dentro(xc, yc, x, y, radio) , bcolors.ENDC, "\n")
    print("Quieres introducir otro punto (y/n)")
    sigo = input(bcolors.OKCYAN)
    print(bcolors.ENDC)  
    if sigo == "y" or sigo == "Y":
        print(bcolors.HEADER, "Introduce el valor de x")
        x = eval(input(bcolors.OKBLUE))
        print(bcolors.ENDC)

        print(bcolors.HEADER, "Introduce el valor de y")
        x = eval(input(bcolors.OKBLUE))
        print(bcolors.ENDC)
    else:
        break

print(bcolors.ENDC)