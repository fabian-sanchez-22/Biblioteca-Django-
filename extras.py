#arbitrary
# def saludar (nombre, apellido):
#     print(f"Hola Mundo  {nombre} {apellido}")
    
# saludar(apellido="martinez", nombre="pedro") 


#args
# def sumar(n1, n2, *n3):
#     print(n1 + n2)
#     print (n3[4])
#     result = 0
#     for n in n3:
#         result += n
#         print (result)
        
# sumar(3, 4, 5, 7, 99, 77, 97)


# **kwargs
# def empleado(nombre, salario, **tareas):
#     print(f"El empleado {nombre}")
#     print(f"tiene un salario de {salario}")

#     for t, n in tareas.items():
#         print(f"{t} = {n}")

# empleado("Pedro", 500,tarea1="ventas",tarea2="inventario",tarea3="aseo")

    
# def fib (n):
#     a = 0
#     b = 1
    
#     for k in range(n):
#         c = a + b
#         a = b
#         b = c
#     return b

# for x in range(2000000):
#     print(fib(x))


frutas = ["banano", "fresa", "mora", "pera", "manzana", "maracuya"]
fruta1, *fruta2, fruta3 = frutas

# print(frutas[2:5:2])

# print(frutas[0])
# frutas[1] = "Mango"
# frutas.append("Papaya")
# frutas.pop(0)
# print(frutas)
# print(frutas.count("banano"))

# frutas.reverse()
# print(frutas)

# for f, n in enumerate(frutas):
#     print(f, n)

# frutas.insert(3, "Guayaba")

# frutas2 = [x for x in frutas if "b" in x]
# print(frutas2)