#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:
lista = []  # Creo una lista vacía
condicion = -15  # Inicializo la variable condicion con el valor -15
while condicion < 0:  # Si condicion es menor que 0 el bucle se repite
    lista.append(condicion)  # Agrego el valor de condicion a la lista
    condicion += 1  # Incremento el valor de condicion en 1 por iteración
print(lista)  # Imprime la lista resultante


# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:
condicion = 0  #inicializo una variable en 0
while condicion < len(lista):  # Se repite el bucle mientras mi variable sea menor que la longitud de la lista 
    if lista[condicion] % 2 == 0:  # Chequeo con el operador resto si se puede dividir condicion entre 2
        print(lista[condicion])  # De ser verdadero se imprime el valor
    condicion += 1  # Incrementa el valor de la variable condicion en 1 por cada iteración  




# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:
for elemento in lista: #Itero todos los elemento de la lista
    if elemento % 2 == 0: #Chequeo con el operador resto si se puede dividir elemento entre 2
        print(elemento) #Imprimio si es divisible




# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:
for elemento in lista[:3]: # Esto asume que inicia desde el indice 0 de la lista hasta el indice 03
    print(elemento)



# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:
# enumerate genera una tupla que contiene el indice y su valor correspondiente
for a,b in enumerate(lista): # a corresponde al indice - b al elemento (valor en esa posicion)
    print(a,b)



# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:
lista = [1,2,5,7,8,10,13,14,15,17,20] # Lista inicial
indice = 1 # Indice con el cual voy buscando
final = 20 # Valor final de la lista, todas las posiciones
while indice < final: # Indico el inicio y fin del bucle
    if not(indice in lista): # Pregunto a ver si la condicion existe
        lista.insert(indice-1, indice) # Si no existe agrego el elemento a la lista
    indice +=1 # Sumo uno al indice para continuar el bucle
print(lista)




# In[11]:


# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:
fibonacci = [0, 1]  # Creo lista con los primeros dos números de la secuencia de Fibonacci
indice = 2  # Inicializa el indice con el valor posterior al ultimo de mi lista inicial
while indice < 30:  # Indico el inicio y fin del bucle
    fibonacci.append(fibonacci[indice - 1] + fibonacci[indice - 2])  # Agrega el siguiente número de Fibonacci a la lista
    indice += 1  # Incrementa el valor de indice en 1 en cada iteración
print(fibonacci)  # Imprime la lista de la secuencia de Fibonacci




# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:
sum(fibonacci)



# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:
primeros = 15  # Número de elementos que se imprimirán
n = primeros - 5  # Valor inicial de n
while n < primeros:  # Mientras n sea menor que el número de elementos a imprimir, se ejecuta el bucle
    print(fibonacci[n] / fibonacci[n - 1])  # Imprime el resultado de la división de dos elementos consecutivos de la lista fibo
    n += 1  # Incrementa el valor de n en 1 en cada iteración



# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

for a, b in enumerate(cadena):  # Iterar la cadena buscando el índice y el carácter de cada iteración
    if b == 'n':  # Chequeo si el carácter es igual a 'n'
        print(a)  # Imprimo el índice correspondiente al carácter 'n'


# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:
diccionario = {  'Ciudad': ['Rosario', 'Saujil', 'Villa Gesell', 'Pinamar'], 
'País': ['Brasil','Paraguay','Ecuador','Uruguay','Chile','Perú','Venezuela','Colombia','Méjico','Uruguay','España','Italia','Francia'], 
'Continente' : ['América','América','América','América','América','América','América','América','América','América','Europa','Europa','Europa']}

for i in diccionario: 
    print(i)

# print(dicc.keys()) Opcional


# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
print(type(cadena))  # Verifico el tipo de dato de la variable cadena
cadena = list(cadena)  # Convierte la cadena en una lista
print(type(cadena))  # Verifico el tipo de dato de la variable cadena después de pasarlo a tipo lista




# In[45]:
recorre = iter(cadena)  # Crea un iterador a partir de la cadena
largo = len(cadena)  # Obtiene la longitud de la cadena
for i in range(0, largo):  # Itera sobre el rango de índices desde 0 hasta largo-1
    print(next(recorre))  # Imprime el próximo elemento del iterador




# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:
lista_a = ['a', 'b', 'c']
lista_b = [1,2,3]
lista_combinada = zip(lista_a, lista_b) #combinacion mediante el metodo zip
print(type(lista_combinada)) #Chequeo el tipo de dato despues de usar el metodo zip
print(list(lista_combinada)) #Tupla




# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:
lista = [18, 21, 29, 32, 35, 42, 56, 60, 63, 71, 84, 90, 91, 100]  # Lista a iterar
compresion_de_lista = [i for i in lista if i % 7 == 0]  # Comprensión de lista para filtrar elementos divisibles por 7
print(compresion_de_lista)  # Impresión del resultado




# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]



# In[51]:
contador = 0  # Inicializo contador de elementos
for elemento in lis:  # Iteración sobre cada elemento de la lista 
    if type(elemento) == list:  # Verificación si el elemento es una lista
        contador += len(elemento)  # Si es una lista, se incrementa el contador por la cantidad de elementos que contiene
    else:
        contador += 1  # Si no es una lista, se incrementa el contador por 1, ya que se trata de un solo elemento
print('La lista contiene',contador, 'elementos')  # Resultado final


# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:
for indice, elemento in enumerate(lis):  # Itero cada elemento e índice de la lista
    if type(elemento) != list:  # Chequeo si el elemento no es una lista
        lis[indice] = [elemento]  # Si no lo es, se reemplaza por una lista que contiene ese elemento
print(lis)  # Impresión de la lista modificada


