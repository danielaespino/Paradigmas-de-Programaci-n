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
        print("esto no se imprimirá)
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
              
#======================================================================
# Los complejos se escriben con la raíz de menos uno              
