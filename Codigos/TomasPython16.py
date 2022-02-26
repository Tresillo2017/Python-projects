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
    
print(bcolors.HEADER, "Introduce el valor de A")
a = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)

print(bcolors.HEADER, "Introduce el valor de B")
b = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)

print(bcolors.HEADER, "Introduce el valor de C")
c = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)

def tipo_lados(a, b, c):
    if a+b+c == 180:
        return "El tipo de triangulo segun sus lados es equilatero"
    elif a == c and a != b and c != b:
        return "El tipo de triangulo segun sus lados es isosceles"
    else:
        return "El tipo de triangulo segun sus lados es escaleno"

def tipo_angulos(a, b, c):
    if pow(a, 2) > pow(b, 2) + pow(c, 2):
        return "El tipo de triangulo segun sus angulos es Obtusangulo"
    elif pow(a, 2) == pow(b, 2) + pow(c, 2):
        return "El tipo de triangulo segun sus angulos es Rectangulo"
    else:
        return "El tipo de triangulo segun sus angulos es Acutangulo"

print (bcolors.OKCYAN,tipo_lados(a,b,c), bcolors.ENDC)
print (bcolors.OKBLUE,tipo_angulos(a,b,c), bcolors.ENDC)
