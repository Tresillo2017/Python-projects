---
title: Ejercicio 3
published: true
---


# Ejercicio 3

- Enunciado
> Escribe un programa que genere las siguientes salidas en su ejecucion. 

```
Programa sobre numeros pares                                Programa sobre numeros pares
Escribe un numero que sea par: 24                           Escribe un numero que sea par: 24
CORRECTO !!!                                                Oh, lo siento !!
El numero 24 es un numero par                               El numero 31 no es un numero par 
24 / 2 = 12.0                                               31 / 2 = 15.5
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

print("Programa sobre numeros pares\n")
print("Escribe un numero que sea par", bcolors.OKBLUE)
numero = input()
print(bcolors.ENDC)
resultado = int(numero) % 2
# print(resultado) Debug only don't uncoment this unless you know what are you doing
if resultado == 0:
    print(bcolors.OKBLUE,"CORRECTO !!!", bcolors.ENDC)
    print(bcolors.HEADER,"El numero", numero, "es un numero par", bcolors.ENDC)

elif resultado == 1:
    print(bcolors.OKBLUE,"INCORRECTO !!!", bcolors.ENDC)
    print(bcolors.HEADER,"El numero", numero,"es un numero",bcolors.WARNING,"impar", bcolors.ENDC)

else:
    print(bcolors.FAIL,"Lo siento el numero ",numero, "no puedo clasificarlo", bcolors.ENDC)

print(int(numero), "/ ", "2", "= ", int(numero) / 2)
```