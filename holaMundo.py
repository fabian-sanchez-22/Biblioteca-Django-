#Ejercicio 1
nombre_curso = input("Digite el nombre del curso")
longitud_nombre_curso = nombre_curso.__len__()
print(longitud_nombre_curso)


#Ejercicio 2
print (nombre_curso[0])


#Ejercicio 3
print (nombre_curso[0:8])


#Ejercicio 4
print (nombre_curso[8:])


#Ejercicio 5
print (nombre_curso[:8])


#Ejercicio 6
print (nombre_curso[:])


#Ejercicio 7
nombre = input("digite el nombre")
apellido = input("digite el apellido")
print (f"{nombre}{apellido}")


#Ejercicio 8
animal = "   perro zorro  "
animal_limpio = animal.strip()
print(animal_limpio)


#Ejercicio 9
print(animal.upper())


#Ejercicio 10 
print(animal.lower())


#Ejercicio 11
print(animal.capitalize())


#Ejercicio 12
print(animal.title())


#Ejercicio 13
print(animal.replace("rr", "ll"))


#Ejercicio 14
print("rr" in animal)


#Ejercicio 15
print("rr" not in animal)


#Ejercicio 16
numero1 = 1
numero2 = 3
print(numero1 / numero2)


#Ejercicio 17
print(round(1.5))


#Ejercicio 18
numero1 = int(input("Ingrese un numero"))
numero2 = int(input("Ingrese otro numero"))
print(numero1 + numero2)


#Ejercicio 19
edad = input("ingrese la edad")


if int(edad) >= 18:
    print("Mayor")
    
else:
    print("Menor")



#Ejercicio 20
n = input("ingrese un numero")
if int(n) > 0:
    print("positivo")
elif int(n) == 0:
        print("cero")
else:
        print("negativo")


##jercicio 21
n = input("ingrese un numero")
if int(n) % 2 == 0 and int(n) >= 0:
    print("El numero es positivo y par")
else:
    print("No es ni par ni positivo")



#Ejercicio 22
nombre = input("ingrese su nombre")
edad = input("ingrese la edad")
validate = f"{nombre}" + "mayor de edad" if int(edad) >= 18 else "menor de edad"
print(validate)



#Ejercicio 23
for i in range(10):
    print(i+1)



#Ejercicio 24
numeroB = int(input("digite un numero de 1 a 10"))
encontrado = False
for numero in range(10):
    if numero == numeroB:
        encontrado = True
        break
    
if encontrado:
    print(f"el numero {numeroB} fue encontrado")
else: 
    print (f"no se encontro el numero")
    


#Ejercicio 25
cadena = input("Ingrese un texto: ")
for caracter in cadena:
    print(caracter)
    

#Ejercicio 26
n1 = int(input("ingrese un numero"))
n2 = int(input("ingrese otro numero"))
if (n1 > 10 and n2 > 10) or (n1 == 5 or n2 == 5):
    print ("cumple")
else:
    print("no cumple")


#Ejercicio 27
n1 = input("ingrese un numero")

if float(n1) >= 5:
    print("cumple") 
else:
    print("no cumple")      
