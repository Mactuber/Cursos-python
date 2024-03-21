# from cgitb import reset
# from unittest import result


# numeros = [1,2,3,4,5]

# def square(num):
#     result = num **2
#     return result


# for item in map(square,numeros):
#     print(item)
#-- aquí sale todo al cuadrado

#si quieres ver la lista retornada aquí abajo

# numeros = [1,2,3,4,5]

# def square(num):
#     result = num **2
#     return result

# print(list(map(square,numeros))) me sale lo mismo que el de arriba, pero en horizontal

# numeros = [1,2,3,4,5,6,7]

# def chek_even(num):
#     return num%2== 0 #--con el % te inidica los n´meros que son divisibles sin ningún resto de la lista

# for n in filter(chek_even,numeros):
#     print(n)

# numeros = [1,2,3,4,5,6,7]

# square = lambda num: num**2

# print(square(5)) #me da el valor de 5 al cuadrado, lambda para cuando usamos otras funciones

# numeros = [1,2,3,4,5,6,7]

# square = lambda num: num ** 2

# print(list(map(lambda num: num ** 2,numeros))) #--dentro de la lista hacemos el mapeo con funcion lambda para verlo mejor

# me dará la raíz cuadrada de todos los números de la lista

numeros = [1,2,3,4,5,6,7]

square = lambda num: num ** 2

print(list(filter(lambda num: num%2 == 0,numeros))) #--aquí filtramos usando lambda para que me salgan los números divisibles