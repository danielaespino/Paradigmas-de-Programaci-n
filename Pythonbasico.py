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
lista = [1, 2, 3, 4, 
        5, 6, 7, 8, 
        9, 10, 11, 12]

matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

print(lista)
print(matriz)

#=====================================================================
# Indentención estricta para procesos dependientes de : (dos puntos)
#=====================================================================
if 10>5:
 print("diez es mayor que cinco")
 print("otra indentación")
for i in lista:
    print(i)
    print("ok")
if 10>5:
        print ("diez es mayor que cinco")
        print("otra indentación")
for i in lista:
        print(i)
        print("ok")
if 10>5:
        print("verdadero")
        if 10<20:
            print("verdadero")
if 10<20:
        print("verdadero")
elif 5>3: # comienza segundo condicional
   print("esto no se imprimirá")
else:
   print("aquí nunca llega")

#==============
#  FUNCIONES
#==============

def say_hello(name):
              print("Hello ", name)
              print("Welcome to Python Tutorials")
              
say_hello("Julián")
              
              
#=====================================================
# Input permite obtener datos del usuario en prompter
#=====================================================
nombre = input("Dame tu nombre: ")
print("Hola como estás",nombre)
              
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
type(número)

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
print(romanNums)
print(romanNums["I"])

print(capitals.get("India"))
print(capitals.get("india"))

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
print(romanNums.keys())

# Reportar valores
print(romanNums.values())

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
for i in range(0,10000):
    potencial.append(float(i))
print(potencial[100])

#=================================
# Generar una tupla con la lista
#=================================
potencial = tuple(potencial)
print(potencial[100])

#****************
# Condicionales
#****************
precio = 50

#*************
# Si esto ...
#*************
if precio < 50:
    print("El precio es menor que 50")

#*****************************
# Si no ... si esto otro ...
#*****************************
elif precio < 50:
    print("El precio es mayor a 50")

#*****************************
# Si nada de lo anterior ...
#*****************************
else:
    print("El precio es 50")

precio = 50
cantidad = 5
total = precio*cantidad

#*************************
# Condicionales anidados
#*************************
if total > 100:
    if total > 500:
        print("Total es mayor que 500")
    else:
        if total < 500 and total > 400:
            print("Total es menor que 500 pero mayor que 400")
        elif total  < 500 and total > 300:
            print("Total entre 300 y 500")
        else:
            print("Total entre 100 y 300")

#**********************************
# Condicional de igualdad son ==
#**********************************
elif total == 100:
    print("Total es 100")
else:
    print("Total menor que 100")

#***********************************************
# Contador mientras la condición sea verdadera
#***********************************************
num = 0
while num < 5:
    num = num + 1
    print(' num = ', num)

num = 0
while num < 5:
    num += 1              # num += 1 es lo mismo que num = num +1
    print('num = ', num)
    if num == 3:          # condición antes de salir del bucle
        break

num = 0
while num < 5:
    num += 1
    if num > 3:
        continue          # evitar lo que sigye, continuar con la iteraciones
    print('num = ', num)

#*******************
# Bucle sobre lista
#*******************
nums = [10, 20, 30, 40, 50]
for i in nums:
    print(i)

#*************************
# Bucle sobre un string
#*************************
for char in 'Hello':
    print (char)

#******************************
# Bucle sobre un diccionario
# items = elementos
#******************************
numNames = {1:'One', 2:'Two', 3:'Three'}
for pair in numNames.items():
    print(pair)

#******************************
# Bluce sobre diccionario
# Key = llave
# value = valor
#******************************
for k,v in  numNames.items():
    print("key = ", k , ", value =", v)

#-------------------
# Primera Función
#-------------------
def saludo():
    #-------------------------------------
    # Documentación rápida de la función
    #-------------------------------------
    """Esta función saluda"""
    print('¡Quiúboles!, ¿cómo estás?')

#--------------------------
# Llamado de la función
#--------------------------
saludo()

#-------------------------------
# Se ejecuta pero no se asigna
#-------------------------------
salida = saludo()

#-------------------------
# Mostrar documentación
#-------------------------
#help(saludo)

#--------------------------
# Función con argumento
#--------------------------
def salu2(nombre):
    """Esta función te saluda por tu nombre"""
    print("¡Que onda ese",nombre,"!")
salu2("Julián")
salu2("Ángel")

#------------------------------------------
# Ahorrar trabajo del intérprete
# nombre:str la variable nombre es un str
#------------------------------------------
def saludos(nombre:str):
    """ Esta función te saluda por tu nombre estrictamente"""
    print("¡Qué onda ese",nombre,"!")
saludos("Julián")
a = 123
print(type(a))
saludos(a)

#----------------------------------
# Función con muchos argumentos
#----------------------------------
def saludos_multiples(nombre1,nombre2,nombre3):
    """Esta función saluda a 3 personas al mismo tiempo"""
    print("Hola ", nombre1, ",", nombre2, "y", nombre3)
saludos_multiples("Hugo","Paco","Luis")

#---------------------------------------------
# Función con cualquier número de argumentos
#---------------------------------------------
def muchos_saludos(*nombres):
    """Esta función saluda a todos los que quieras"""
    i = 0
    #-----------------------------------
    # end = es para ponerlo de corrido
    #-----------------------------------
    print("Hola ", end ="")
    while len(nombres) > i:
      # Último nombre
      if (i==len(nombres)-1):
        print(nombres[i])
      else:
        # Cualquier otro nombre
        print(nombres[i], end=", ")
      i+=1

muchos_saludos("Bosco","Angel","David","Tamara","MIli","Edwin","Lev","Luis","Abigail")

def greet(firstname, lastname):
    print('Hello', firstname, lastname)

#----------------------------------------------
# Llamar la función con argumentos en desorden
#----------------------------------------------
greet(lastname='Jobs', firstname='Steve') #Se puedem especificar las variables en desorden


#----------------------------------------
# Función con argumentos escondidos **
#----------------------------------------
def greet(**person):
    #----------------------------------------------------
    # Persona tiene características firstname y lastname
    #----------------------------------------------------
    print('Hello ', person['firstname'], person['lastname'])

greet(firstname='Steve', lastname='Jobs')
greet(lastname='JObs', firstname='Steve')
greet(firstname='Bill', lastname='Gates', age=55) #Se pueden pasar más parámetros de los necesarios


#---------------------------------
# Función con valores por defecto
#---------------------------------
def greet(name = 'Guest'):
    print('Hello', name)

greet() # Utiliza el valor dado de antemano
greet('Steve')

#------------------------
# Función con resultado
#------------------------
def suma(a,b):
    return a+b

#--------------------------------------
# Programación funcional
# Se pueden funciones en funciones
#-------------------------------------
total=suma(5, suma(10, 20))
print(total)

#--------------------------------------------------
# Cálculo lambda
# Nombre de la función = lambda variable : función
#--------------------------------------------------
x_al_cuadrado = lambda x : x * x
al = x_al_cuadrado(5)
print(al)


#-----------------------------
# Lambda de varias variables
#-----------------------------
suma = lambda x1, x2, x3,: x1+x2+x3
print(suma(99,98,97))

sumas = lambda *x: x[0]+x[1]+x[2]+x[3]

print(sumas(100,200,300,400))

#-------------------------------------------
# Uso de una función anónima
# El argumento va afuera entre paréntesis
#-------------------------------------------
print((lambda x: x*x)(6)) # Función anónima

#-------------------------------
# Función con variable global
# EVITE EL EXCESO !!!!!
#-------------------------------
name = 'Steve'
def greet():
    global name #Para utilizar una variable global (que viene de fuera del bloque)
    name = 'Bill'
    print('Hello ', name)

greet()
