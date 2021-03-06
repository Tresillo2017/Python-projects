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
    
print(bcolors.HEADER, "Programa que reordena palindromos", bcolors.ENDC)
print("Ingresa el palindromo")
palindromo = input(bcolors.OKBLUE)
print(bcolors.ENDC)

# def espalindromo(s):
for s in palindromo:
    if s == s[::-1]:
        print("es palindromo")
        # return True
    else:
        print("No es palindromo")
        # return False

comprobacion = espalindromo(palindromo)

if comprobacion:
    print(bcolors.OKGREEN,"Si es un palindromo", bcolors.ENDC, "(", bcolors.BOLD, espalindromo(palindromo), bcolors.ENDC, ")")
else:
    print(bcolors.FAIL, "No es un palindromo", bcolors.ENDC, "(", bcolors.BOLD, espalindromo(palindromo), bcolors.ENDC, ")")