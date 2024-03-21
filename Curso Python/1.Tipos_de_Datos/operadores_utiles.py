# milista = [1,2,3]

# for num in range(10):  ---hemos creado un rango que va del 0 al 9
#     print(num)

# milista = [1,2,3]

# for num in range(0,11,2):  #va del 0-11 dando dos pasos
#     print(num)

# milista = [1,2,3]

# print(list(range(0,11,2))) ahora se creará la lista anterior en horizontal

# contador_indice = 0
# palabra = 'hola'

# for letter in palabra:
#     print(palabra[contador_indice])
#     contador_indice += 1 --te dice hola en vertical 



# palabra = 'hola'

# for item in  enumerate(palabra):
#     print(item) #te enumera las letras en vertical


# from operator import index


# palabra = 'hola'

# for index,letter in  enumerate(palabra):
#     print(index)
#     print(letter) --imprimes por separado mezclando la numeración con la palabra
#     print('\n') --esto separa 

# milista1 = [1,2,3]
# milista2 = ['a','b','c']

# for item in zip(milista1,milista2):
#     print(item)
 #----zip para emparejar 1 con a, 2 con y 3 con c


# milista1 = [1,2,3,4,5,6] --en este caso no imprimirá 4,5,6 debido a que no cumple con el minimo de las otras listas
# milista2 = ['a','b','c']
# milista3 = [100,200,300]

# for item in zip(milista1,milista2,milista3):
#     print(item)

# milista1 = [1,2,3,4,5,6]
# milista2 = ['a','b','c']
# milista3 = [100,200,300]

# print(list(zip(milista1,milista2))) ahora ya se juntan por parejas en horizontal

# milista1 = [1,2,3,4,5,6]
# milista2 = ['a','b','c']
# milista3 = [100,200,300]

# if 'a' in milista2:
#     print('Verdadero') --imprimirá verdaadero porque hemos encontrado la a

# milista1 = [1,2,3,4,5,6]
# milista2 = ['a','b','c']
# d = {'k1' : 1}
# milista3 = [100,200,300]

# if 'k1' in d:
#     print('Verdadero')  #--buscará si tenemos la llave k1 en diccionario

# milista1 = [1,2,3,4,5,6]
# milista2 = ['a','b','c']
# d = {'k1' : 1}
# milista3 = [100,200,300]

# if 1 in d.keys():
#     print('Verdadero')
# else:
#     print('Falso') --te imprimirá falso porque 1 no es llave sino solo valor


# from random import shuffle 

# milista1 = [1,2,3,4,5,6,7,8,9,10]
# milista2 = ['a','b','c']
# d = {'k1' : 1}
# milista3 = [100,200,300]

#print(min(milista1))  --te dice el valor minimo de la lista

#print(max(milista1)) --aquí te imprimirá el máximo

# milista1 = shuffle(milista1)

# print(shuffle(milista1)) shuffle funciona en terminal, te desordena la lista

# from random import randint, shuffle #--randint agarra números aleatorios

# milista1 = [1,2,3,4,5,6,7,8,9,10]
# milista2 = ['a','b','c']
# d = {'k1':1}
# milista3 = [100,200,300]

# resultado = input('Escribe un número aquí') ---te deja insertar un número y salga en consola

# print(resultado)

# resultado = input('Escribe un número aquí')

# print(type(resultado)) ---el 10 se imprimmirá como una cadena de texto

resultado = input('Escribe un número aquí')

print(type(float(resultado))) #-- en este caso se convierte en un float