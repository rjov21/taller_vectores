# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:57:54 2021

@author: DIOS BENDITO
"""
# ejercico1
# parte a


def sumatoria(numeros):
    suma = 0
    for valor in numeros:
        suma = suma + valor
    print(f'el valor de la sumatoria es: {suma}')

# parte b


def productoria(numeros):
    producto = 1
    for valor in numeros:
        producto = producto * valor
    print(f'el valor de la productoria es: {producto}')


i = 1
numeros = []
while True:
    num = int(input(f'ingrese el numero {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    numeros.append(num)
    i += 1
print(f'los numeros ingresados fueron {numeros}')


sumatoria(numeros)
productoria(numeros)
