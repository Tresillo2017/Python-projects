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


positivo = 0
negativo = 0

def po():
    positive = positivo + 1
    opositivas = positive * 'o'
    
def ne():
    negative = negativo + 1

print("Escribe numeros (el 0 termina el programa)")

while True:
    number = int(input(bcolors.HEADER))
    print(bcolors.ENDC)
    if number == 0:
        break
    elif number >= 1:
        po()
    elif number <= 0:
        ne()
    

print(bcolors.BOLD, "Positivos", bcolors.ENDC, opositivas)