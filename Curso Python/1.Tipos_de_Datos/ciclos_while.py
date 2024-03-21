# x = 0

# while x < 5:  -la condición necesariamente debe ser falsa
#     print(f'El valor actual de x es {x}') ---solamente hasta aquí aparecerá unn cilo infinito de valor de x es 0
#     x = x + 1 ---agregadon esto aparecerá el valro actual de x es 0 y luego x es 1 .... es lo mismo que x += 1


# x = 0

# while x < 5:  
#     print(f'El valor actual de x es {x}')
#     x += 1   -el else se aplica cuando acabamos de usar el while
# else:
#     print('X no es mayor que 5')

# Ahora el uso del pass

# x = [1,2,3]

# for item in x:
#     #comment ---- con el pass de abajo superas  un problema anterior
#     pass

# print('fin del libreto')

# x = "Eric"

# for letter in x:
#    if letter == 'i':
#        continue #--imprimiremos tosas las letras menos a
# print(letter)

x = "Eric"

for letter in x:
   if letter == 'r':
       break #--rompe la cadena a paratir de r
print(letter)