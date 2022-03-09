import math


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

print("Programa que calcula una ecuacion de segundo grado\n")
print("A continuacion se le pedira el valor de a, b y c")
print("Introduce el valor de a", bcolors.OKBLUE)
a = eval(input())
print(bcolors.ENDC,"\n","Introduce el valor de b", bcolors.OKCYAN)
b = eval(input())
print(bcolors.ENDC,"\n","Introduce el valor de c", bcolors.OKCYAN)
c = eval(input())
print(bcolors.ENDC)


x1 = (b*b) - (4*a*c)
print(x1)
if x1 < 0:
    print(bcolors.FAIL, "No hay soluciones reales", bcolors.ENDC)
elif x1 == 0:
    x4 = -b/2*a
    print("La unica solucion es", bcolors.BOLD, x4, bcolors.ENDC)
else:
    x3 = math.sqrt(x1)
    a1 = (-b + x3)/2*a 
    a2 = (-b - x3)/2*a
    print("La primera solucion es", bcolors.OKCYAN, a1, bcolors.ENDC)
    print("La segunda solucion es", bcolors.OKBLUE, a2, bcolors.ENDC)
        
