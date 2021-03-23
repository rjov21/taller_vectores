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

# parte c


def num_mayor(numeros):
    numeros.sort()
    mayor = numeros[(len(numeros) - 1):]
    print(f'el numero mayor es: {mayor}')

# parte d


def num_menor(numeros):
    numeros.sort()
    menor = numeros[:1]
    print(f'el numero menor es: {menor}')


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
num_mayor(numeros)
num_menor(numeros)

# ejercicio 2
# parte a


def cant_pares(numeros):
    pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
    print(f'la cantidad de numeros pares ingresados fueron: {pares}')


# parte b


def cant_impares(numeros):
    impares = 0
    for numero in numeros:
        if numero % 2 == 1:
            impares += 1
    print(f'la cantidad de numeros impares ingresados fueron: {impares}')


# parte c


def cant_primos(numeros):
    cont = 0
    primos = 0
    for valor in numeros:
        for i in range(valor):
            i += 1
            if valor % i == 0:
                cont += 1
            if cont == 2:
                primos += 1
    print(f'la cantidad de numeros primos es: {primos}')


i = 1
numeros = []
while True:
    num = int(input(f'ingrese el numero {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    numeros.append(num)
    i += 1
print(f'los numeros ingresados fueron {numeros}')

cant_pares(numeros)
cant_impares(numeros)
cant_primos(numeros)


# ejercicio 3
# parte a


def operaciones_vectores_suma(v, v1):
    vresultado = []
    for i in range(len(v)):
        x = v[i] + v1[i]
        vresultado.append(x)
    print(f'el vector resultante de la suma es: {vresultado}')


# parte b
def operaciones_vectores_resta(v, v1):
    vresultado = []
    for i in range(len(v)):
        x = v[i] - v1[i]
        vresultado.append(x)
    print(f'el vector resultante de la suma es: {vresultado}')


i = 1
v = []
while True:
    num = int(input(f'ingrese el numero {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    v.append(num)
    i += 1
print(f'los numeros ingresados fueron {v}')

i = 1
v1 = []
while True:
    num = int(input(f'ingrese el numero {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    v1.append(num)
    i += 1
print(f'los numeros ingresados fueron {v1}')

operaciones_vectores_suma(v, v1)
operaciones_vectores_resta(v, v1)

# ejercicio 4


def num_repetido(numeros):
    cont = 0
    aux = 0
    for i in numeros:
        cont = 0
        for valor in numeros:
            if i == valor:
                cont += 1
        if cont > aux:
            aux = cont
            num = i
    print(f'el numero que mas se repite es {num} y se repite {aux} veces')


i = 1
numeros = []
while True:
    num = int(input(f'ingrese el numero {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    numeros.append(num)
    i += 1
print(f'los numeros ingresados fueron {numeros}')


num_repetido(numeros)

# ejercicio 5


def vector_2_partes(numeros):
    if len(numeros) % 2 != 0:
        print('la longitud del vector no es par,ingrese una longitud par')
    mitad = int(len(numeros) / 2)
    v1 = numeros[:mitad]
    v2 = numeros[mitad:]
    productoria(v1)
    sumatoria(v2)


i = 1
numeros = []
while True:
    num = int(input(f'ingrese el numero {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    numeros.append(num)
    i += 1
print(f'los numeros ingresados fueron {numeros}')

vector_2_partes(numeros)


# ejercicio 6


def vector_simetrico(numeros):
    mitad = int(len(numeros) / 2)
    v = numeros[:mitad]
    v2 = numeros[mitad:]
    v2.reverse()
    if v == v2:
        print('el vector es simetrico')
    else:
        print('el vector no es simetrico')


i = 1
numeros = []
while True:
    num = int(input(f'ingrese el numero {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    numeros.append(num)
    i += 1
print(f'los numeros ingresados fueron {numeros}')


vector_simetrico(numeros)


# ejercicio 7
# parte a

def conjuntos_union(A, B):
    C = list(set(A + B))
    print(f'la union de los dos vectores es: {C}')


# parte b


def conjuntos_interseccion(A, B):
    C = []
    for i in A:
        for valor in B:
            if i == valor:
                C.append(i)
    print(f'la intersecion de los dos vectores es: {C}')


# parte c


def diferencia_A(A, B):
    C = []
    C = A
    for i in A:
        for valor in B:
            if i == valor:
                C.remove(i)
    print(f'la diferencia es: {C}')


# parte d


def diferencia_B(A, B):
    C = []
    C = B
    for i in B:
        for valor in A:
            if i == valor:
                C.remove(i)
    print(f'la diferencia es: {C}')


i = 1
A = []
while True:
    num = int(input(f'ingrese el numero {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    A.append(num)
    i += 1
print(f'los numeros ingresados fueron {A}')

i = 1
B = []
while True:
    num = int(input(f'ingrese el numero {i} o ingrese 0 para finalizar: '))
    if num == 0: break
    B.append(num)
    i += 1
print(f'los numeros ingresados fueron {B}')

conjuntos_union(A, B)
conjuntos_interseccion(A, B)
diferencia_A(A, B)
diferencia_B(A, B)
