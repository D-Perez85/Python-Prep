#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
a = 2
if a <0: 
    print("El nro es menor que cero")
elif a > 0:
     print("El nro es mayor que cero")
else:
     print("El nro es cero")




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
a = 3
b = False
if type(a) == type(b):
    print("Los tipos de datos son iguales")
else:
    print("Los tipos de datos no son iguales")




# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
for i in range(1,21):
    if i % 2 == 0:
        print(i , "es par")
    else:
        print(i , "es impar")




# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for i in range(0,6):
    i=i**3
    print(i)




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
a = 8
for i in range(0,a):
    print(i)




# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
n = 4
if (n > 0):
    factorial = n
    while (n > 2):
        n = n - 1
        factorial = factorial * n
        print('El factorial es', factorial)
    else:
        print('La variable no es mayor a cero')
else:
    print('La variable no es un entero')



# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
num = 1
while num < 5:
    print('Ciclo while nro ', num)  # Imprime el número del ciclo while
    for i in range(1, num+1): 
        print('Ciclo for nro ', i)  # Imprime el número del ciclo for
    num += 1




# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
num = 4
for i in range(1,n):
    while num < 4:
        num -= 1
    print("Soy el valor while" , num)
    print("Soy el valor for" , i)




# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
fin=30
inicio = 0
primo = True
while (inicio < fin):
    for div in range(2, inicio):
        if (inicio % div == 0):
            primo = False
    if (primo):
        print(inicio)
    else:
        primo = True
    inicio += 1



# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
inicio = 0
primo=True
while (inicio < 30):
    for div in range(2, inicio):
        if (inicio % div == 0):
            primo=False
            break
    if (primo):
        print(inicio)
    else:
        primo=True
    inicio+=1




# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
contador = 0
fin=30
inicio = 0
primo = True
while (inicio < fin):
    for div in range(2, inicio):
        contador += 1
        if (inicio % div == 0):
            primo = False
    if (primo):
        print(inicio)
    else:
        primo = True
    inicio += 1
print(f'cantidad de iteraciones sin break: {contador}')



# In[57]:
contador = 0
inicio = 0
primo = True
while (inicio < 30):
    for div in range(2, inicio):
        contador += 1
        if (inicio % div == 0):
            primo = False
            break
    if (primo):
        print(inicio)
    else:
        primo = True
    inicio += 1
print(f'cantidad de iteraciones con break: {contador}')



# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# In[58]:
contador = 0
fin= 50
inicio = 0
primo = True
while (inicio < fin):
    for div in range(2, inicio):
        contador += 1
        if (inicio % div == 0):
            primo = False
    if (primo):
        print(inicio)
    else:
        primo = True
    inicio += 1
print(f'cantidad de iteraciones sin break: {contador}')




# In[59]:
contador = 0
inicio = 0
primo = True
while (inicio < 50):
    for div in range(2, inicio):
        contador += 1
        if (inicio % div == 0):
            primo = False
            break
    if (primo):
        print(inicio)
    else:
        primo = True
    inicio += 1
print(f'cantidad de iteraciones con break: {contador}')



# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:
inicio = 100
while(inicio <= 300):
    inicio += 1
    if (inicio % 12 != 0):
        continue
    print(inicio, ' SI es divisible!')




# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
n = 1
sigue = 1
primo = True
while (sigue == 1):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
        print('¿Presione 1 si desea encontrar el próximo número primo?')
        if (input() != '1'):
            print('Se finaliza el proceso')
            break
    else:
        primo = True
    n += 1



# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:
inicio = 100
while(inicio<=300):
    if (inicio % 6 == 0):
        print('El número es: ', str(inicio))
        break
    inicio += 1


