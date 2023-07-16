#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
a = 10; 
print(a)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
type(8.5)




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
type(a)




# 4) Crear una variable que contenga tu nombre

# In[2]:
mi_nombre= "Damian Perez"



# 5) Crear una variable que contenga un número complejo

# In[3]:
nro_complejo = 1.3 - 7j




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
type(nro_complejo)




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
var_pi = 3.1416

pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
var_uno = "True"
var_dos = True




# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print("La primer variable es de tipo : " , type(var_uno), ". La restante es de tipo : " , type(var_dos)); 




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
suma_de_nros = 3 + 1.5




# 11) Realizar una operación de suma de números complejos

# In[2]:
suma_de_complejos = nro_complejo + 4j
print(suma_de_complejos)




# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
suma_real_complejo = nro_complejo + 10
print(suma_real_complejo)




# 13) Realizar una operación de multiplicación

# In[5]:
multiplicar = 10 *4
print(multiplicar)

print(2**8)


# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
print(2**8)




# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
cociente = 27 / 4
print(cociente)





# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
print(27//4)




# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
print(27 % 4)




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
resultado = 4 * (27 // 4)  + (27 % 4)
print(resultado)




# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
var_alfa1 = "Hola "
var_alfa2 = " Chau"
print(var_alfa1 + var_alfa2)




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
iguales = "2" == 2
print(iguales , ": el tipo de dato no es el mismo")




# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
iguales = int("2") == 2
print(iguales)




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
a = float('3,8')
print(a , "por la coma que esta despues del 3")




# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
variable = 3
variable-= 1
print(variable)




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
print(1 << 4)
print("es un sistema de numeración utilizado para representar números decimales. El sistema binario es de base 2, lo cual quiere decir que dispone solo de 2 números para representar cantidades. El sistema decimal (números comunes) es de base 10")




# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

sumar =  2 + "2"
print("No se permite porque son de distinto tipo los datos.")




# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

Multiplicar	='je ' * 3
print(Multiplicar)

