#==========================
#   OPERACIONES BÁSICAS
#==========================
print (2+3)
print (2*3)
print (2/3)
print (2**10)
print (2**0.5)  # raíz cuadrada
print (10%2)
print (10%0.1) # exclusivo en python

#===========================================
# Para saber el tipo de objeto se usa type
#===========================================
t=0
print(type(t)) # entero
t=3.6
print(type(t)) # real (flotante)
t=True 
print(type(t)) # booleano (bool)

#========================
# Mensaje de pantalla
#========================
print ("ESte es un comando de python. ", "Este es otro enunciado. ", t)
print('id: ', 1)
print('Cirst Name: ', 'Steve')
print('Last Name: ', 'JObs')
print("Vamos a sumar esto" + " con esto otro")

#================================================
# Continuar una instrucción en varios renglones
#================================================
if 100 > 99 and \
        200 <= 300 and \
        True != False:
            print('Hello WOrld!')

#=======================================
# Comandos diferentes en la misma línea
#=======================================
print("Hola "); print("tu!!") # Se considera mala práctica

#==================================================
# Usanado paréntesis redondos, cuadrados o llaves
# Se puede escribir en varios renglones
#==================================================
list = [1, 2, 3, 4, 
        5, 6, 7, 8, 
        9, 10, 11, 12]

matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

print(list)
print(matriz)

#=====================================================================
# Indentención estricta para procesos dependientes de : (dos puntos)
#=====================================================================
if 10>5;
 print("diez es mayor que cinco")
 print("otra indentación")
for i in list:
    print(i)
    print("ok")
if 10>5:
        print ("diez es mayor que cinco")
        print("otra indentación")
for i in list:
        print(i)
        print("ok")
if 10>5:
        print("verdadero")
        if 10<20:
            print("verdadero")
if 10<20:
        print("verdadero")
elif 5>3: #comienza segundo condicional
        print("esto no se imprimirá")
              else:
              print("aquí nunca llega")
#==============
  FUNCIONES
#==============

def say_hello(name):
              print("Hello ", name)
              print("Welcome to Python Tutorials")
              
say hello("Julián")
              
              
#=====================================================
# Input permite obtener datos del usuario en prompter
#=====================================================
nombre = input("Dame tu nombre: ")
              print("Hola como estás", nombre)
              
#=========================================
# Los enteros son de precisión ilimitada
#=========================================         
y = 5000000000000000000000000000000000
print(y)
              
#====================================================================
#   Se pueden delimitar números con guión bajo pero no con coma
#====================================================================
y = 5_000_000
print(y)
              
#=====================================================
# La función int() cambia strings y floats a enteros
#=====================================================
número = int(input("Dame tu edad: "))
type(numero)

#=====================================================
# La notación científica de flotantes utiliza e o E
#=====================================================              
# 1.2 x 10^{-9}
#================
y = 1.2E-09
print(y)
              
#===========================================================
# La función float() convierte strings y enteros a floats
#===========================================================
y = float("14.3")
print(y)
              
#=====================================================
# Los complejos se escriben con la raíz de menos uno  
# j siempre con un número como prefijo
# no acepta la j suelta
#=====================================================
z = 1+1j

# suma +
# resta -
# multiplicación *
# división /
# modulo %
# exponente **
# // función piso
# Funciones para transformar números int() float() complex()
# Operaciones abs() round() pow()

print(round(3.14159,4))

#==========================
# Strings de varias líneas
#==========================
parrafo = """ En el bosque de la china
              la chinita se perdió """
print(parrafo)

#===============================================
# La función len() obtiene el tamaño del string
#===============================================
n=len(parrafo)
print(n)

#=============================================================
# Las letras en un string ocupan lugares como en un arreglo
# (también de atrás para adelante comenzando en -1 el último)
#=============================================================
palabra = "hola"
print(palabra[0])
print(palabra[-4])

#=======================
#  Conjunto en python
#=======================
even_nums ={2, 4, 6 , 8, 10} # conjunto de números paresw
print(even_nums)

# El bool no es parte del conjunto
emp = {1, 'Steve', 10.5, True} # conjunto de diferentes objetos
print(emp)

nums = {1, 2, 2, 3, 4, 4, 5, 5}
print(nums)

#===================================
# Convertir secuencia a conjunto
# No lo genera en orden
#===================================
s = set('Hello')
print(s)
s = set((1,2,3,4,5)) # tupla a conjunto
print(s)

#===============================================
# De diccionario a conjunto: conjunto de llaves
#===============================================
d = {1:'One', 2: 'Two'}
s = set(d)
print(s)

s.add(100)
print(s)

s.update(nums)
print(s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

su = s1|s2 # Unión
print(su)

s1 = s1&s2 # Intersección

sr = s1-s2 # Diferenciaq de conjuntos
print(sr)

sp = s2-s1
print(sp)

ss = s1^s2 # Diferencia simétrica
print(ss)

#===========================
#    Uso de diccionarios
#===========================
capitals = {"USA":"Washington D.C", "France":"Paris", "India":"New Delhi"}
print(capitals)

#==================
#  llave:valor
#==================

# diccionario vacío
d ={}

# Llave entera, valor string
numNames={1:"One", 2:"Two", 3:"Three"}

# Llave real, valor string
decNames={1.5:"One and Half", 2.5:"Two and Half", 3.5:"Three and Half"}

# LLave tupla, valor string
items={("Parker","Reynolds","Camlin"):"pen", ("LG","Whirlpool","Samsung-"): "Refrigerator"}

# Llave string, valor int
romanNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5}
print(romanNUms)
print(romanNums["I"])

print(capitals.get("India"))
print(capital.get("india"))

# Reportar llave y valor 
for k in capitals:
    print("Key = " + k + ", Value = " + capitals[k])

# Nuevo dato para el diccionario
capitals["Mexico"] = "CDMX"
print(capitals)

# Borrar dato del diccionario
del capitals["Mexico"]
print(capitals)

# Borrar todo el diccionario
del capitals

# Reportar llaves
print(romanNUms.keys())

# Reportar valores
print(romaNUMS.VALUES())

# Juicio de llave (está o no está la llave en el diccionario)
print("I" in romanNums)
print("X" in romanNums)
print("XX" not in romanNums)



#================================================
# Listas
# Las listas pueden ser de objetos diferentes
#================================================

miprimeralista = []  #Lista vacía
print(miprimeralista)


#=====================
#  Llenado de lista
#=====================

miprimeralista = [1, "Javier",1.34,"Bosco","Angel","Abigail",True]
print(miprimeralista)

#========================================
#  list: hacer una lista
#  range(i,j): secuencia de i hasta j-1
#========================================
nums = list(range(1,61))
for i in nums:
    print(i)

#========================================
# Incluír nuevos elementos en la lista
#========================================
nums.append(61)
nums.append(62)
nums.append(61)
print(nums)


#================================
# Quitar elemento con índice i
#================================
i = 61
del nums[i]
print(nums)

#===========================
#  Borrar la lista
#===========================
del nums

#================
# Sumar listas
#================
L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2)

#=================
# Llenado a mano
#=================
potencial = []
for i in range(0,10000)
    potencial.append(float(i))
print(potencial[100])

#=================================
# Generar una tupla con la lista
#=================================
potencial = tuple(potencial)
print(potencial[100])


