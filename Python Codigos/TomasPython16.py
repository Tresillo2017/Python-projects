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
    
print(bcolors.HEADER, "Introduce las cordenadas de A")
xa = eval(input(bcolors.OKBLUE))
ya = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)

print(bcolors.HEADER, "Introduce las cordenadas de B")
xb = eval(input(bcolors.OKBLUE))
yb = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)

print(bcolors.HEADER, "Introduce las cordenadas de C")
xc = eval(input(bcolors.OKBLUE))
yc = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)


def distancia(x1, y1, x2, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

def maximos_minimos(a, b, c):
    maximo = max(a, b, c)
    if max == a:
        cat1 = b
        cat2 = c
    elif max == b:
        cat1 = a
        cat2 = c 
    else:
        cat1 = a
        cat2 = b
    return maximo, cat1, cat2

def tipo_lados(a, b, c):
    if a+b+c == 180:
        return "El tipo de triangulo segun sus lados es equilatero"
    elif a == c and a != b and c != b:
        return "El tipo de triangulo segun sus lados es isosceles"
    else:
        return "El tipo de triangulo segun sus lados es escaleno"

def tipo_angulos(a, b, c):
    a2 = round(pow(a, 2), 6)
    b2 = round(pow(b, 2), 6)
    c2 = round(pow(c, 2), 6)
    if a2 > b2 + c2:
        return "El tipo de triangulo segun sus angulos es Obtusangulo"
    elif a2 < b2 + c2:
        return "El tipo de triangulo segun sus angulos es Acutangulo"
    else:
        return "El tipo de triangulo segun sus angulos es Rectangulo"

AB = distancia(xa, ya, xb, yb)
AC = distancia(xa, ya, xc, yc)
BC = distancia(xb, yb, xc, yc)

h, c1, c2 = maximos_minimos(AB, AC, BC)

print (bcolors.OKCYAN,tipo_lados(AB,AC,BC), bcolors.ENDC)
print (bcolors.OKBLUE,tipo_angulos(h, c1, c2), bcolors.ENDC)

print(bcolors.ENDC)