"""Ejercicio 1: Imprimir tu Nombre
Crea un programa que imprima tu nombre en la pantalla.
nombre="Gine"
print(nombre)"""
#--------------------------------------------------------------------------
"""Ejercicio 2: Sumar Dos Números
Escribe un programa que pida al usuario dos números y muestre la suma de ambos.

num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))
suma=num1+num2
print(f"La suma de {num1} con {num2} es {suma}")"""

#--------------------------------------------------------------------------
"""Ejercicio 3: Verificar Mayoría de Edad
Crea un programa que pida la edad del usuario y le diga si es mayor o menor de edad.

edad=int(input("Ingrese su edad: "))
if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")"""

#------------------------------------------------------------------------
"""Ejercicio 4: Contar del 1 al 10
Escribe un programa que use un bucle para imprimir los números del 1 al 10

for n in range(1,11):
    print(f"-{n}")"""
    
#-----------------------------------------------------------------------
"""Ejercicio 5: Función para Calcular el Área de un Círculo
Crea una función que reciba el radio de un círculo y devuelva su área. (Usa la fórmula: área = π * radio²)    

def circulo(radio):
    area=3.14 * (radio**2)
    return F"El area del circulo es {area}"

radio=int(input("Ingrese el radio del circulo: "))
print(circulo(radio))"""

#--------------------------------------------------------
#listas
"""Ejercicio 1: Crear y Modificar una Lista
Crea una lista llamada colores que contenga al menos cinco colores.

colores=["azul","amarillo","verde","rojo","morado"]

#Imprime el tercer color de la lista

print(f"El tercer color de la lista es: {colores[2]}")

#Cambia el primer color por "rojo"

colores[0]="rojo"
print(colores)

#Añade "verde" al final de la lista.

colores.append("verde")
print(colores)"""

#--------------------------------------------------------------------------------
"""Ejercicio 2: Usar Métodos de Listas
Crea una lista llamada numeros con los números del 1 al 10.
numeros=[2,4,1,3,7,5,8,6,9,10]
#Usa el método remove() para eliminar el número 5.
numeros.remove(5)
print(numeros)
#Usa el método pop() para eliminar el último número de la lista.
numeros.pop()
print(numeros)
#Ordena la lista y luego imprímela.
numeros.sort()
print(numeros)"""

#-------------------------------------------------------------------------
"""#Ejercicio 3: Contar Elementos

#Crea una lista llamada animales que contenga al menos cinco nombres de animales.
animales=["perro","gato","loro","elefante","oso"]
#Imprime la cantidad de animales en la lista.
print(f"Hay disponible {len(animales)} animales")
#Usa un bucle para imprimir cada animal en la lista.
print("Lista de animales disponibles")
for animal in animales:
    print(f"-{animal}")"""
    
#-------------------------------------------------------------------
"""Ejercicio 4: Listas Anidadas
Crea una lista llamada estudiantes que contenga tres listas, cada una representando un estudiante con su nombre y edad.

estudiantes = [["Juan", 20], ["Ana", 22], ["Luis", 19]]

#Imprime el nombre y la edad de cada estudiante.

for estudiante in estudiantes:
    nombre=estudiante[0]
    edad=estudiante[1]
    print(f"-El estudiante {nombre} tiene {edad} años")  """
    
#-------------------------------------------------------------------------
#tuplas

"""Ejercicio 1: Crear y Acceder a una Tupla
#Crea una tupla llamada colores que contenga al menos cinco colores.
colores=("azul","rojo","amarillo","verde","morado")
#Imprime el segundo color de la tupla.  

print(f"El segundo elemento de la tupla es {colores[1]}") """
#--------------------------------------------------------------------------
"""Ejercicio 2: Contar Elementos en una Tupla
#Crea una tupla llamada numeros que contenga los números del 1 al 10, con algunos números repetidos
numeros=(2,6,3,5,8,3,8,4,6,2,5,7,1,5,8,9,2,8,5,2,9)
#Usa el método count() para contar cuántas veces aparece el número 5.
contador=numeros.count(5)
print(f"El numero 5 aparece {contador} veces")"""

#---------------------------------------------------------------------------
"""Ejercicio 3: Encontrar el Índice de un Elemento
#Crea una tupla llamada animales que contenga al menos cinco nombres de animales.
animales=("perro","gato","raton","loro","tigre")
#Usa el método index() para encontrar el índice de un animal específico en la tupla.

indice=animales.index("raton")
print(f"El indice del raton es {indice}")"""

#---------------------------------------------------------------------
"""Ejercicio 4: Conversión entre Listas y Tuplas
#Crea una lista llamada frutas_lista que contenga al menos tres frutas.
frutas_lista=["manzana","pera","mora"]
#Convierte la lista en una tupla y luego imprime la tupla resultante.
tupla_frutas=tuple(frutas_lista)
print(tupla_frutas) """

#--------------------------------------------------------------
#diccionarios
"""Ejercicio 1: Crear y Acceder a un Diccionario
#Crea un diccionario llamado libro con las siguientes claves y valores:"título": "Cien años de soledad","autor": "Gabriel García Márquez","año": 1967

libro={
    "titulo":"cien años de soledad",
    "autor":"gabriel garcia marquez",
    "año": 1967
}

#Imprime el título y el autor del libro.  

print(f"El titulo del libro es {libro['titulo']} y el autor es {libro['autor']}")""" 

#-------------------------------------------------------------------------
"""Ejercicio 2: Modificar y Agregar Elementos
#Agrega una nueva clave-valor al diccionario libro con la clave "género" y el valor "Realismo mágico".

libro={
    "titulo":"cien años de soledad",
    "autor":"gabriel garcia marquez",
    "año": 1967
}

libro["genero"]="realismo magico"

#Cambia el año de publicación a 1977

libro["año"]=1977

#Imprime el diccionario actualizado.

print(libro)"""  

#----------------------------------------------------------------------------
"""Ejercicio 3: Usar Métodos de Diccionarios
#Crea un diccionario llamado estudiantes que contenga al menos tres estudiantes, donde cada clave sea un nombre y cada valor sea una lista con las calificaciones del estudiante.

estudiantes={
    "ana":[18,20,16],
    "pedro":[13,10,17],
    "maria":[15,19,8]
}

#Usa el método keys() para imprimir los nombres de los estudiantes.
print("Nombres de estudiantes")
for clave in estudiantes.keys():
    print(f"{clave}")

#Usa el método values() para imprimir las calificaciones de cada estudiante.

print("Calificaciones de los estudiantes")
for valor in estudiantes.values():
    print(f"{valor}")"""
    
#----------------------------------------------------
"""#Ejercicio 4: Buscar Valores en un Diccionario
#Crea un diccionario llamado capitales que contenga al menos cinco países como claves y sus respectivas capitales como valores.

capitales={
    "mexico":"ciudad de mexico",
    "españa":"madrid",
    "estados unidos":"washington D.C",
    "brasil":"brasilia",
    "argentina":"buenos aires"
}

#Pide al usuario que ingrese un país y usa el método get() para imprimir la capital de ese país. Si el país no se encuentra en el diccionario, imprime un mensaje indicando que no se encontró.   

pais=input("Ingrese un pais: ")

capital=capitales.get(pais, "No se encontro")

print(capital)"""

#------------------------------------------------------------------------------
#condicionales
"""Ejercicio 1: Verificar Mayoría de Edad
#Crea un programa que pida al usuario su edad y determine si es mayor de edad (18 años o más) o menor de edad.

edad=int(input("Ingrese su edad: "))

if edad >= 18:
    print("Ud es mayor de edad")
else:
    print("Ud es menor de edad")  """
    
#------------------------------------------------------------------------------
"""Ejercicio 2: Calificaciones
#Escribe un programa que pida al usuario su calificación (un número entre 0 y 100) y muestre un mensaje según la calificación:
#"Aprobado" si la calificación es 60 o más.
#"Reprobado" si la calificación es menor de 60.  

nota=int(input("Ingrese su calificacion: ")) 
if nota in range(0,101):
    if nota >= 60:
        print("Aprobado :)")
    else:
        print("Reprobado :(")
else:
    print("Ingrese una nota valida")"""
    
#----------------------------------------------------------------------------------
"""Ejercicio 3: Clasificación de Números
#Crea un programa que pida al usuario un número y determine si es positivo, negativo o cero.  

numero=int(input("Ingrese un numero: "))
if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Es cero") """  
 
#-----------------------------------------------------------------------------
"""Ejercicio 4: Evaluar un Número
#Escribe un programa que pida al usuario un número y determine si es par o impar.
  
numero=int(input("Ingrese un numero: "))

if numero%2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")""" 
    
#---------------------------------------------------------------------
"""#Ejercicio 5: Juego de Adivinanza
#Crea un programa que genere un número aleatorio entre 1 y 10 y le pida al usuario que adivine el número. Si el usuario adivina correctamente, imprime "¡Correcto!", de lo contrario, imprime "Intenta de nuevo".   

import random

numero_aleatorio= random.randint(1, 10)

numero=int(input("adivina un numero del 1 al 10: "))

if numero == numero_aleatorio:
    print("Ganaste wiiiiii")
else:
    print(f"Perdiste :( que mal el {numero} no era :( era el {numero_aleatorio}")  """   
    
#----------------------------------------------------------------
#bucles
"""#Ejercicio 1: Imprimir Números del 1 al 10
#Escribe un programa que use un bucle for para imprimir los números del 1 al 10.  

for n in range(1,11):
    print(f"-{n}") """
    
#------------------------------------------------------------
"""#Ejercicio 2: Sumar Números
#Crea un programa que use un bucle while para sumar todos los números del 1 al 10.

suma=0
contador=1
while contador<=10:
    suma+=contador
    contador+=1
print(f"La suma de los numeros del 1 al 10 es: {suma}") """

#--------------------------------------------------------------------
"""#Ejercicio 3: Adivinar un Número
#Escribe un programa que genere un número aleatorio entre 1 y 10 y le pida al usuario que adivine el número. Si el usuario adivina incorrectamente, sigue pidiendo una adivinanza hasta que sea correcta. 

import random

numero_aleatorio=random.randint(1, 10)

while True:
    numero=int(input("adivine un numero del 1 al 10: "))
    if numero == numero_aleatorio:
        print("Ganaste wiiii")
        break
    else:
        print("No era el numero :( vuelve a intentarlo")
        continue"""
        
#---------------------------------------------------------------------------
"""#Ejercicio 4: Tabla de Multiplicar
#Crea un programa que use un bucle for para imprimir la tabla de multiplicar de un número dado por el usuario

print("---Tablas de Multiplicar---")
tabla=int(input("Ingrese la tabla de multiplicar: "))
if tabla in range(1,11):
    print("Tablas del {tabla} ")
    for r in range(1, 11):
        print(f"{tabla}x{r}={tabla*r}")
else:
    print("Ingrese una opcion valida") """
    
#------------------------------------------------------------
"""#Ejercicio 5: Contar Vocales
#Escribe un programa que use un bucle for para contar el número de vocales en una cadena de texto ingresada por el usuario.

texto=input("Ingrese un texto: ")

vocales=0
lista=["a","e","i","o","u"]
texto_m=texto.lower()
for letra in texto_m:
    if letra in lista :
        vocales+=1
        
print(f"El texto {texto} tiene {vocales} vocales") """

#----------------------------------------------------------------------
#ejercicios de practica completos
"""#Ejercicio 1: Invertir una Cadena
#Escribe un programa que pida al usuario una cadena de texto y la imprima al revés.

texto=input("Ingrese un texto: ")

al_reves=texto[::-1]

print(f"El texto {texto} pero al reves: {al_reves}")"""
#----------------------------------------------------------------------------
"""#Ejercicio 2: Contar Palabras
#Pide al usuario que ingrese una frase y cuenta cuántas palabras hay en la frase. Imprime el resultado.
texto=input("Ingrese un texto: ")

palabras=texto.split()
numero_de_palabras=len(palabras)

print(f"La frase {texto} tiene {numero_de_palabras} palabras")"""       
#-------------------------------------------------------------------------                
        
"""#Ejercicio 3: Filtrar Números Pares en una Lista
#Crea una lista de números del 1 al 20. Usa un bucle for para imprimir solo los números pares de la lista.
numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for n in numeros:
    if n%2 == 0:
        print(n)"""
#---------------------------------------------------------------------
"""#Ejercicio 4: Tupla de Colores
#Crea una tupla llamada colores que contenga al menos cinco colores. Luego, imprime el tercer color de la tupla.
colores=("azul","amarillo","verde","naranja","rojo")
print(f"El tercer elemento es: {colores[2]}")"""
#----------------------------------------------------------------

#Ejercicio 5: Diccionario de Productos
"""#Crea un diccionario llamado productos que contenga al menos tres productos con sus precios. Pide al usuario que ingrese el nombre de un producto y muestra su precio. Si el producto no está en el diccionario, imprime un mensaje indicando que no se encontró.

productos={
    "harina":3000,
    "aceite":5000,
    "azucar":4000
}

nombre=input("Ingrese el producto que desea ver: ")

precio=productos.get(nombre, "No se encontro")

print(f"El producto {nombre}:{precio} ")"""
#-------------------------------------------------------------
"""#Ejercicio 6: Contar Vocales en una Cadena
#Pide al usuario que ingrese una cadena de texto y cuenta cuántas vocales hay en la cadena. Imprime el número de vocales encontradas.

texto=input("Ingrese un texto: ")
vocales=["a","e","i","o","u"]
vocal=0
for v in texto:
    if v in vocales:
        vocal+=1
print(f"El texto \"{texto}\" tiene {vocal} vocales") """       
#-----------------------------------------------------------        
        
"""#Ejercicio 7: Lista de Nombres
#Crea una lista llamada nombres que contenga al menos cinco nombres. Usa un bucle for para imprimir cada nombre en una línea separada y verifica si el nombre es "Juan". Si es "Juan", imprime un mensaje especial.

nombres=["maria","ana","luis","juan","mario"]
for nombre in nombres:
    if nombre =="juan":
      print(f"-{nombre} como estas mi amor")
    else:
          print(f"-{nombre}")"""
#------------------------------------------------------------------------          
        
"""#Ejercicio 8: Sumar Elementos de una Tupla
#Crea una tupla llamada numeros que contenga cinco números. Usa un bucle for para sumar todos los números de la tupla y muestra el resultado.

numeros=(30,10,45,83,7)
suma=0
for n in numeros:
    suma+=n
print(f"La suma de todos los numeros es: {suma}")"""    
#-------------------------------------------------------------------------    

"""#Ejercicio 9: Clasificación de Estudiantes
#Crea un diccionario llamado estudiantes que contenga tres estudiantes y sus calificaciones. Usa un bucle for para imprimir el nombre de cada estudiante y su calificación. Indica si el estudiante aprobó (calificación >= 60) o reprobó.

estudiantes={
    "maria": (15,17,20),
    "luis":(12,10,14),
    "mario":(5,12,14)
}

for nombre, notas in estudiantes.items():
    suma=sum(notas)//3
    if suma >=12:
        promedio="Aprobado"
    else:
        promedio="Reprobado"
    print(f"-Estudiante {nombre}: su Calificacion final es: {suma} usted esta {promedio}") """

#-----------------------------------------------------------------------
           
"""#Ejercicio 10: Crear una Lista de Frutas
#Crea una lista llamada frutas que contenga al menos cinco frutas. Usa un bucle for para imprimir cada fruta y verifica si la fruta es "manzana". Si es "manzana", imprime un mensaje indicando que es tu fruta favorita.

frutas=["manzana","pera","limon","naranja","fresa"]

for fruta in frutas:
    if fruta =="limon":
        print(f"-El {fruta} es mi fruta favorita")
    else:
        print(f"-{fruta}") """
        
#------------------------------------------------------------
#ejercicios mas dificiles
"""#Ejercicio 1: Análisis de Texto
#Escribe un programa que pida al usuario que ingrese un texto y realice las siguientes tareas:
#Contar el número total de caracteres en el texto.
#Contar el número de palabras en el texto.
#Contar el número de vocales y consonantes.
#Imprimir las 5 palabras más frecuentes en el texto.
#Permitir al usuario buscar una palabra específica en el texto y mostrar cuántas veces aparece.
#Sueños hechos realidad
texto=input("Ingrese un texto largo: ")

#numero total de caracteres
espacios=texto.replace(" ", "")
c=len(espacios)
print(f"El texto tiene un total de {c} caracteres")

#número de palabras en el texto
palabras=texto.split()
palabra=len(palabras)
print(f"El texto tiene un total de {palabra} palabras")    
 
# número de vocales y consonantes
espacios=texto.replace(" ", "")
vocales=["a","e","i","o","u"]
vocal=0
consonante=0
for c in espacios:
    if c in vocales:
        vocal+=1
    else:
        consonante+=1
print(f"El texto tiene un total de {vocal} vocales")
print(f"El texto tiene un total de {consonante} consonantes")



# 5 palabras más frecuentes en el texto
frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

palabras_frecuentes = sorted(frecuencia, key=frecuencia.get, reverse=True)[:5]
print(f"Las 5 palabras más frecuentes en el texto son: {', '.join(palabras_frecuentes)}")       
        
#Permitir al usuario buscar una palabra específica en el texto y mostrar cuántas veces aparece

buscar=input("ingrese la palabra que desea buscar: ")
palabras=texto.split()
lista=list(palabras)
for p in lista:
    if p == buscar:
        contador=lista.count(buscar)

print(f"La palabra {buscar} aparece {contador} veces en el texto") """
#-----------------------------------------------------------            
"""#Ejercicio 2: Gestión de Estudiantes
#Crea un programa para gestionar información de estudiantes. Deberá:
#Permitir al usuario crear un diccionario de estudiantes, donde la clave sea el número de identificación del estudiante y el valor sea una lista con su nombre, edad y calificaciones.
#Imprimir una lista de todos los estudiantes con su información.
#Permitir al usuario buscar un estudiante por su número de identificación y mostrar su información.
#Calcular el promedio de calificaciones de cada estudiante y determinar si aprobó o reprobó (aprobación mínima de 60).
#Imprimir una lista de los estudiantes aprobados y reprobados por separado.

print("Programa de gestion de informacion de estudiantes")
estudiante={}


while True:
    print("---Menu---")
    print("1.Agregar Estudiante")
    print("2.Listar Estudiantes")
    print("3.Buscar Estudiante")
    print("4.Lista de Aprobados y Reprobados")
    print("0.Salir")
    opcion=input("Ingrese una opcion: ")
    if opcion == "1":
        print("---Agregar Estudiantes---")
        cedula=input("Ingrese la cedula: ")
        if cedula in estudiante:
            print("Esta cedula ya existe")
        else:
            nombre=input("Ingrese el nombre del estudiante: ")
            edad=input("Ingrese la edad del estudiante: ")
            notas_lista=[]
            nota1=int(input("Ingrese la nota 1: "))
            notas_lista.append(nota1)
            nota2=int(input("Ingrese la nota 2: "))
            notas_lista.append(nota2)
            nota3=int(input("Ingrese la nota 3: "))
            notas_lista.append(nota3)
            tupla=tuple(notas_lista)
            estudiante[cedula]=[nombre, edad, tupla]
            print("Estudiante Agregado Exitosamente")
    elif opcion=="2":
        print("---Listado de Estudiantes---")
        for clave, valor in estudiante.items():
            print(f"*Estudiante {valor[0]}:")
            print(f"Cedula: {clave}")
            print(f"Edad: {valor[1]}")
            print(f"Calificaciones: {valor[2]}")
            print("-------------------------------------")
    elif opcion == "3":
        print("---Buscador de Estudiantes---")
        cedula=input("Ingrese la cedula del estudiante que quiere buscar: ")
        if cedula in estudiante:
            valor=estudiante[cedula]
            print(f"El estudiante de la cedula {cedula}: ")
            print(f"Nombre: {valor[0]}")
            print(f"Edad: {valor[1]}")
            print(f"Calificaciones: {valor[2]}")
        else:
            print("No se encontró el estudiante con esa cedula") 
    elif opcion =="4":
        aprobados=[]
        reprobados=[]
        for clave, valor in estudiante.items():
            final=sum(valor[2])//3
            if final >=12:
                
                aprobados.append(valor[0])
            else:
                
                reprobados.append(valor[0])
        print("---Lista de Estudiantes Aprobados y Reprobados")
        print("----Aprobados----")
        for nombre in aprobados:
            print(f"-{nombre}")
        print("----Reprobados----")
        for nombre in reprobados:
            print(f"-{nombre}") 
    elif opcion=="0":
        print("Gracias!! Vuelva Pronto")
        break
    else:
        print("Opcion invalida") """
#---------------------------------------------------------------------
"""#Ejercicio 3: Juego de Adivinar la Palabra
#Crea un juego en el que el programa elija una palabra aleatoria de una lista predefinida y el usuario debe adivinarla. Deberá:
#Almacenar una lista de al menos 20 palabras en una tupla.
#Elegir una palabra aleatoria de la lista.
#Mostrar al usuario una serie de guiones bajos, uno por cada letra de la palabra.
#Permitir al usuario ingresar una letra y verificar si está en la palabra.
#Si la letra está en la palabra, reemplazar los guiones correspondientes con la letra.
#Si la letra no está en la palabra, incrementar un contador de intentos fallidos.
#Repetir el paso 4 hasta que el usuario adivine la palabra completa o se quede sin intentos.
#Al final, mostrar un mensaje indicando si el usuario ganó o perdió, y la palabra completa.

import random

palabras=("perro","amigo","pelota","gato","fresa","cama","ornitorrinco","lucas","nombre","koala","pala","peluche","jugo","escoba","habitacion","pantalon","loro","fideo","bolsa","telefono")

palabra_secreta=random.choice(palabras)

guiones=["_"]*len(palabra_secreta)

contador_intentos_fallidos=0

max_intentos=6

print("Bienvenido al juego de adivinar la palabra")
print(f"Tienes {max_intentos} intentos para adivinar la palabra")

while True:
    print(" ".join(guiones))
    letra=input("ingrese una letra: ").lower()
    if letra in palabra_secreta:
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i]==letra:
                guiones[i]=letra
    else:
        contador_intentos_fallidos+=1
        print(f"Intento fallido te quedan {max_intentos-contador_intentos_fallidos} intentos ")
    if "_" not in guiones:
        print(f"Felicidades haz adivinado la palabra: {palabra_secreta} ")
        break
    else:
        if contador_intentos_fallidos>=max_intentos:
            print(f"Lo siento, no has adivinado la palabra :( La palabra era: {palabra_secreta}")
            break"""
            
#---------------------------------------------------------------------------------                        

"""#Ejercicio 4: Análisis de Ventas
#Crea un programa para analizar las ventas de una tienda. Deberá:
#Permitir al usuario ingresar las ventas diarias de la tienda durante una semana.
#Almacenar las ventas en un diccionario, donde la clave sea el día de la semana y el valor sea la cantidad de ventas.
#Calcular y mostrar el total de ventas de la semana.
#Determinar y mostrar el día con mayores ventas.
#Calcular y mostrar el promedio de ventas diarias.
#Permitir al usuario buscar las ventas de un día específico.

print("---Programa de Analisis de Ventas---")

ventas={}

ventas["lunes"]=int(input("Ingrese la venta del dia lunes: "))
ventas["martes"]=int(input("Ingrese la venta del dia martes: "))
ventas["miercoles"]=int(input("Ingrese la venta del dia miercoles: "))
ventas["jueves"]=int(input("Ingrese la venta del dia jueves: "))
ventas["viernes"]=int(input("Ingrese la venta del dia viernes: "))
ventas["sabado"]=int(input("Ingrese la venta del dia sabado: "))
ventas["domingo"]=int(input("Ingrese la venta del dia domingo: "))
print("Ventas Agregadas")

print("---Reportes de la venta semanal---")

total_ventas=sum(ventas.values())
print(f"*Total de venta de la semana: {total_ventas} pesos")

mayor_venta=max(ventas.values())
for dia, venta in ventas.items():
    if venta == mayor_venta:
        print(f"*El dia {dia} tuvo mayor ventas con un total de {venta} pesos")
        
promedio=total_ventas/len(ventas)
print(f"*El promedio de ventas diarias fue de {promedio}")
while True:
    op=input("Desea buscar la venta de algun dia?: ").lower()
    if op == "si":
        dia=input("Ingrese el dia de la semana que desea buscar: ").lower()
        if dia in ventas:
            print(f"ventas del dia {dia}: {ventas[dia]} pesos")
        elif dia == "no":
            print("Gracias!!")
            break"""

#----------------------------------------------------------------------------            
#Ejercicio 5: Gestión de Inventario
#Crea un programa para gestionar el inventario de una tienda. Deberá:
#Permitir al usuario crear un diccionario de productos, donde la clave sea el código del producto y el valor sea una lista con el nombre, precio y cantidad en stock.
#Imprimir una lista de todos los productos con su información.
#Permitir al usuario buscar un producto por su código y mostrar su información.
#Permitir al usuario agregar o retirar unidades de un producto.
#Generar un reporte de productos con stock bajo (menos de 10 unidades).
#Calcular el valor total del inventario."""  

print("---Gestion de Inventario---")

productos={}
while True:
    print("---Menu---")
    print("1.Agregar Producto")
    print("2.Listar de Productos")
    print("3.Buscar Producto")
    print("4.Agregar o Retirar unidades")
    print("5.Reporte de productos con stock bajo")
    print("6. Valor total del inventario")
    print("0.Salir")
    
    opcion=input("Ingrese una opcion: ")
    if opcion == "1":
        print("---Agregar Producto---")
        codigo=input("ingrese el codigo del producto: ")
        if codigo in productos:
            print("Este codigo ya existe")
        else:
            lista=[]
            nombre=input("Ingrese el nombre del producto: ")
            lista.append(nombre)
            precio=int(input("Ingrese el precio del producto: "))
            lista.append(precio)
            cantidad=int(input("Ingrese la cantidad del producto: "))
            lista.append(cantidad)
            productos[codigo]=lista
            print("Producto Agregado")
    elif opcion =="2":
        print("---Listado de Producto---")
        for clave, valor in productos.items():
            print(f"Producto: {valor[0]}")
            print(f"Codigo: {clave}")
            print(f"Precio: {valor[1]}")
            print(f"Cantidad existente: {valor[2]}")
            print("---------------------------------------")
    elif opcion=="3":
        print("---Buscar Productos---")
        buscar=input("Ingrese el codigo del producto a buscar: ")
        if buscar in productos:
            valor=productos[buscar]
            print(f"El producto del codigo {buscar}")
            print(f"Nombre: {valor[0]}")
            print(f"Precio: {valor[1]}")
            print(f"Cantidad: {valor[2]}")
        else:
            print("Este codigo no existe. Intente de nuevo")
    elif opcion =="4":
        print("---Agregar o Retirar unidades---")
        codigo=input("Ingrese el codigo del producto: ")
        
        print(f"cantidad Existente del producto {productos[codigo][0]}: {productos[codigo][2]} ")
        op=input("Quieres retirar o agregar? (r/a): ").lower()
        if op == "r":
            cantidad=int(input("Ingrese la cantidad a retirar: "))
            if cantidad <= productos[codigo][2]:
                productos[codigo][2]-=cantidad
            else:
                print("No se encuentra esa cantidad en el stock")    
        elif op =="a":
            cantidad=int(input("Ingrese la cantidad a agregar: "))
            productos[codigo][2]+=cantidad
        else:
            print("Opcion Invalida")
        print(f"Cantidad actualizada:{productos[codigo][2]}") 
    elif opcion =="5":
        print("---reporte de los productos con stock bajo---")
        bajo=[]
        for clave,valor in productos.items():
            if valor[2] <= 10:
                bajo.append((valor[0],valor[2]))
        for valor in bajo:
            print(f"-{valor}") 
    elif opcion =="6":
        print("---Valor total del inventario---")
        final=0
        for valor in productos.values():
            total=valor[1]*valor[2]
            final+=total
        print(f"El valor total es: {total}") 
    elif opcion=="0":
        print("gracias!!")
        break
    else:
        print("Opcion invalida")                      
            
            
                      
                 
                
        
        
                            
                
                
    







