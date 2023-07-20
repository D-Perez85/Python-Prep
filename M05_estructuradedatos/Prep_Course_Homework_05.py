#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:
ciudades_del_mundo = ["Madrid", "Roma", "Viena", "Vaticano", "Milan"]
print(ciudades_del_mundo)



# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print(ciudades_del_mundo[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:

print(ciudades_del_mundo[1:4])



# 4) Visualizar el tipo de dato de la lista

# In[12]:

print(type(ciudades_del_mundo))



# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:

print(ciudades_del_mundo[2:])


# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:

print(ciudades_del_mundo[:4])

    
# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:
ciudades_del_mundo.append("Jamaica")
ciudades_del_mundo.append("Viena")

print(ciudades_del_mundo) #no arroja error 


# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:
ciudades_del_mundo.insert(3, "Buenos AIres")



# In[21]:
print(ciudades_del_mundo)


# 9) Concatenar otra lista a la ya creada

# In[22]:
ciudades_del_mundo.extend(["Salta", "Catamarca", "La Rioja"])
print(ciudades_del_mundo)



# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:
print(ciudades_del_mundo.index("Viena")) #Me retorna la primera posicion que encuentra

# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:
print(ciudades_del_mundo.index("Vieno")) #Indica que el elemento no pertenece a mi lista




# 12) Eliminar un elemento de la lista

# In[25]:
ciudades_del_mundo.remove("Jamaica")
print(ciudades_del_mundo)


# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:
ciudades_del_mundo.remove("Jamaica") #Indica que el elemento no pertenece a mi lista

# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:
ultimo_elemento = ciudades_del_mundo.pop()
print(ultimo_elemento)


# 15) Mostrar la lista multiplicada por 4

# In[29]:
print(ciudades_del_mundo * 4)



# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:
tupla_nros = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)



# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:
tupla_nros[10:16]



# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:
print(20 in tupla_nros)
print(30 in tupla_nros)


# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:
ciudad_a_buscar = "Paris"
if (ciudad_a_buscar in ciudades_del_mundo):
     print("Paris", ciudad_a_buscar, "existe dentro de mi tupla")
else:
    ciudades_del_mundo.append(ciudad_a_buscar)
    print("Se agrega a mi tupla", ciudad_a_buscar)

print(ciudades_del_mundo) #corroboro

# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:
ciudades_del_mundo.count("Viena")


# 21) Convertir la tupla en una lista

# In[52]:
print(type(tupla_nros))
lista_de_nros = list(tupla_nros)
print(type(lista_de_nros))

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:
primero = tupla_nros[0]
segundo = tupla_nros[1]
tercero = tupla_nros[2]

print(primero)
print(segundo)
print(tercero)

# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:
diccionario_lista = dict()
type(diccionario_lista)

diccionario_lista = {
    "ciudad" : ciudades_del_mundo,
    "habitantes" : [1000, 2000, 3000, 4000, 5000, 6000, 3000, 7000, 8000, 9000],
    "idioma" : ["Español", "Italiano","Italiano", "Español", "Español", "Ingles", "Italiano", "Portugues", "Portugues", "Italiano"]                 
}

print(diccionario_lista)

# 24) Imprimir las claves del diccionario

# In[59]:
print(diccionario_lista.keys())

# 25) Imprimir las ciudades a través de su clave

# In[61]:
print(diccionario_lista[('ciudad')])

