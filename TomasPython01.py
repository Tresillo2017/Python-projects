from random import randint

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


def aleatorio():
    print(bcolors.OKBLUE)
    print("Primer numero")
    a = randint(1,100)
    print(a)
    print("Segundo el numero")
    b = randint(1,100)
    print(b)
    print(bcolors.ENDC)


    suma = (a + b) 
    resta = (a - b)
    multiplicacion = (a * b)
    division = (a / b)
    division_entera = (a // b)
    resto_division = (a % b)


def automatico():
    print(bcolors.OKBLUE)
    a = input(" Escribe el primer numero (#aleatorio#)  \n")
    if a == "aleatorio":
        a1 = randint(1,100)
    b = input("Escribe el segundo numero (#aleatorio#) \n")
    if b == "aleatorio":
        b2 = randint(1,100)
    if a and b != "aleatorio":
        a = eval(a)
        b = eval(b)
    print(bcolors.ENDC)

    suma = (a1 + b2) 
    resta = (a1 - b2)
    multiplicacion = (a1 * b2)
    division = (a1 / b2)
    division_entera = (a1 // b2)
    resto_division = (a1 % b2)


    def texto():
        print (a, "+", b, "= ", suma)
        print (a, "-", b, "= ", resta)
        print (a, "*", b, "= ", multiplicacion)
        print (a, "/", b, "= ", division)
        print (a, "//", b, "= ", division_entera)
        print (a, "%", b, "= ", resto_division)
    def resultado():
        print("Operaciones disponibles con ", a, "y", b)

    resultado()
    texto()

    def texto():
        print (a, "+", b, "= ", suma)
        print (a, "-", b, "= ", resta)
        print (a, "*", b, "= ", multiplicacion)
        print (a, "/", b, "= ", division)
        print (a, "//", b, "= ", division_entera)
        print (a, "%", b, "= ", resto_division)
    def resultado():
        print("Operaciones disponibles con ", a, "y", b)

    resultado()
    texto()

def manual():
    print("Has elegido el modo Manual ", "\n Hay 6 opciones disponibles ", bcolors.OKBLUE, "\n suma , resta , multiplicacion , division , division_entera , resto_division" , bcolors.ENDC, bcolors.WARNING, "TIENES QUE ESCRIBIRLO TAL Y COMO ESTA \n", bcolors.ENDC )
    a = input("Elige operacion: ")
    print(bcolors.OKBLUE)
    n1 = input("Escribe el primer numero (#aleatorio#) ")
    #if n1 == "aleatorio":
    #    s1 = randint(1, 100)
    n2 = input("Escribe el segundo numero (#aleatorio#) ")
    #if n2 == "aleatorio":
        #s2 = randint(1,100)
    #if n1 and n2 != "aleatorio":
    s1 = eval(n1)
    s2 = eval(n2)
    print(bcolors.ENDC)
    
    if a == "suma":
        print(s1, "+", s2, "= ", s1 + s2)
    if a == "resta":
        print(s1, "-", s2, "= ", s1 - s2)
    if a == "multiplicacion":
        print(s1, "*", s2, "= ", s1 * s2)
    if a == "division":
        print(s1, "/", s2, "= ", s1 / s2)
    if a == "division_entera":
        print(s1, "//", s2, "= ", s1 // s2)
    if a == "resto_division":
        print(s1, "%", s2, "= ", s1 % s2)


print("Elige el modo que quieres", bcolors.BOLD, "'Automatico, Manual, Aleatorio' ", bcolors.ENDC, "\n En el", bcolors.BOLD, "Modo Automatico", bcolors.ENDC,  "se haran todas las operaciones ", "\n Mientras que en el", bcolors.BOLD ,  "Modo Manual", bcolors.ENDC ,  "tu eliges que operacion queires hacer" )
modo = input("Elige el modo que quieras: ")

if modo == "automatico":
    automatico()
if modo == "manual":
    manual()
if modo == "aleatorio":
    aleatorio()
# else:
#    print (bcolors.FAIL, "Lo siento, no he encontrado ese modo en mi base de datos")


# He puesto una clase para cambiar el color de las letras para que sea mas comodo a la vista


