def automatico():
    a = input("\003[1;34;40m Escribe el primer numero  \n")
    a = eval(a)
    b = input("\003[1;34;40m Escribe el segundo numero \n")
    b = eval(b)

    suma = (a + b) 
    resta = (a - b)
    multiplicacion = (a * b)
    division = (a / b)
    division_entera = (a // b)
    resto_division = (a % b)


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
    a = print("Has elegido el modo Manual ", "\n Hay 6 opciones disponibles ", "\n suma, resta, multiplicacion, division, division_entera, resto_division", "\033[1,31,40m TIENES QUE ESCRIBIRLO TAL Y COMO ESTA \n" )
    n1 = input("Escribe el primer numero ")
    n1 = eval(n1)
    n2 = input("Escribe el segundo numero ")
    n2 = eval(n2)
    
    if a == "suma":
        print(n1 + n2)
    if a == "resta":
        print(n1 - n2)
    if a == "multiplicacion":
        print(n1 * n2)
    if a == "division":
        print(n1 / n2)
    if a == "division_entera":
        print(n1 // n2)
    if a == "resto_division":
        print(n1 % n2)


print("Elige el modo que quieres '\003[1;36;40m Automatico, Manual' ", "\n En el Modo Automatico se haran todas las operaciones ", "\n Mientras que en el modo Manual tu eliges que operacion queires hacer" )
modo = input("Elige el modo que quieras: ")

if modo == "automatico":
    automatico()

if modo == "manual":
    manual()








