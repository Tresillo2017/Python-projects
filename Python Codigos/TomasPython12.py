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
    

print("Programa que comprueba si un año es bisiesto o no")
print("Ingrese el año")
year = eval(input(bcolors.OKBLUE))
print(bcolors.ENDC)

if year % 4!= 0: 
    print(bcolors.OKCYAN, year, bcolors.ENDC, "No es bisiesto")
elif year % 4 == 0 and year % 100 != 0:
    print(bcolors.HEADER, year, bcolors.ENDC,"Es bisiesto")
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print(bcolors.OKCYAN, year, bcolors.ENDC, "No es bisiesto")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #divisible entre 4, 100 y 400
	print(bcolors.HEADER, year, bcolors.ENDC, "Es bisiesto")