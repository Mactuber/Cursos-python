# name = 'VARIABLE GLOBAL' #esto es una variable global porque s eencuentra afuera de la función y 
                        #todas las funciones la puedan usar.

# def saludo():

#     name ='Elver Galarga'

#     def hola():
#         print('Hola ' + name)

#     hola()

# saludo()

# #GLOBAL
# name = 'VARIABLE GLOBAL' 

# def saludo():
#     #Enclosing
#     name ='Elver Galarga'

#     def hola():
#         #local
#         name = 'Variable Local'
#         print('Hola ' + name) #--usará la variable local

#     hola()


# saludo()


# x = 50

# def func(x):
#     #Re asignación local
#     x = 200
#     print(f'Fui Localmente Cambiada de x a {x}')

# func(x)


x = 50

def func():
    global x
    print(f' X es {x}')
    #Re asignación global
    x = 'NUEVO VALOR'
    print(f'Fui Localmente Cambiada de X a {x}')

func()
print(x)

# ahora no hace falta darle valor a la función porque coge la función global 