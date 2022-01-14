---
title: Ejercicio 5
published: true
---
- Enunciado 
> 


- Codigo 

```python
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

print("Programa que analiza una palabra\n")
print("Escribe una palabra: ")
palabra = input(bcolors.OKBLUE)
print(bcolors.ENDC)
longitud = len(palabra[:])

if longitud <= 5: 
    print("La palabra", bcolors.OKBLUE,palabra , bcolors.ENDC,"tiene", bcolors.OKCYAN, len(palabra[:5]), bcolors.ENDC, "letras")
    print("La primera letra es", bcolors.OKGREEN, palabra[0], bcolors.ENDC)
    print("Las ultima letra es", bcolors.OKGREEN, palabra[3:], bcolors.ENDC)

if longitud > 5:
    print("La palabra", bcolors.OKBLUE,palabra , bcolors.ENDC,"tiene", bcolors.OKCYAN, len(palabra[:10]), bcolors.ENDC, "letras")
    print("Las cuatro primeras letras son", bcolors.OKGREEN, palabra[0:4], bcolors.ENDC)
    print("Las cuatros ultimas letras son", bcolors.OKGREEN, palabra[3:], bcolors.ENDC)
```