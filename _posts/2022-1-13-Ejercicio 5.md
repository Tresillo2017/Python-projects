---
title: Ejercicio 5
published: true
---
- Enunciado 
> El programa comprobara si la palabra tiene 5 letras o menos, en cuyo caso mostrara la primera y la ulitima letra. 
> en el caso de que tenga ams de 5 letras, mostrara las 4 primeras letras por un lado y las 4 ultimas letras por otro, aunque haya letras coincidentes en las 2 particiones. 
> El programa debe generar las siguientes salidas en su ejecucion

```
Programa que analiza una palabra                    Programa que analiza una palabra 
Escribe una palabra: Hola                           Escribe una palabra: Saludos 
La palabra Hola tiene 4 letras                      La palabra Saludos tiene 7 letras   
La Primera letras es: H                             Las 4 primeras letras son: Salu
La ultima letras es: a                              Las 4 Ultimas letras son: udos
```


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