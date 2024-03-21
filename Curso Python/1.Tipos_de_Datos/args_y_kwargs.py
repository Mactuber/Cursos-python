# def func(a,b): #--a estos parámetros a y b se les dice keywords argumnets, en posicion del 0 y el 1.
#                                 #retorna el 5% de la suma de a y b
#     return sum((a,b)) * 0.05

# func(40,50) #--estos son parámetros posicionales

# def func(*args):
#     return print (sum(args) * 0.05)
# func(40,60,760,890) --esta es una función con argumentos cuantos queramos

# def func(**kwargs):
#     if 'fruit' in kwargs:
#         print('Mi fruta escogida es {}'.format(kwargs['fruit']))
#     else:
#         print('no hay fruta')

# func(fruit='manzana', veggie='lechuga') #--aquí dirá que mi fruta escogida es la manzana

def func(*args,**kwargs):
    print(args)
    print(kwargs)
    print('Me gustaría {} {}'.format(args[0],kwargs['comida']))

func(10,30,50, comida ='paellas', animal='linda')#puedo poner cuantos kwargs quiera, y en este caso me dice que queiro 10 apellas