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

print("Numeros impares entre 1, 1000")

for n in range(1,1000):
    if (n % 2 == 1):
        print(bcolors.OKBLUE,n, bcolors.ENDC,"es un numero impar\n")
    else:
        print("")
