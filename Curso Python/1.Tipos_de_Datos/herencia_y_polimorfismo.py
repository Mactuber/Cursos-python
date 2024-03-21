
# class Animal():
#     def __init__(self):
#         print('ANIMAL CREADO')


#     def quien_soy(self):
#         print("Soy un animal")

#     def comer(self):
#         print("Estoy comiendo")

# class Perro(Animal):

#     def __init__(self):
#         Animal.__init__(self)
#         print("Perro creado")

# nuevoPerro = Perro()

# saldrá animal creado y perro creado


# class Animal():
#     def __init__(self):
#         print('ANIMAL CREADO')


#     def quien_soy(self):
#         print("Soy un animal")

#     def comer(self):
#         print("Estoy comiendo")

# class Perro(Animal):

#     def __init__(self):
#         Animal.__init__(self)
#         print("Perro creado")

#     def quien_soy(self):
#         print("Soy un perro")

# miPerro = Perro()

# miPerro.quien_soy()

#se ejecuta ANIMAL CREADO, Perro creado, Soy un perro

class Animal():
    def __init__(self):
        print('ANIMAL CREADO')


    def quien_soy(self):
        print("Soy un animal")

    def comer(self):
        print("Estoy comiendo")

class Perro(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Perro creado")

    def quien_soy(self):
        print("Soy un perro")

miPerro = Perro()

miPerro.quien_soy()