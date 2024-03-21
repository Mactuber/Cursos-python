class Perro():  #clases
    
    def __init__(self,raza,nombre,puntos):

        #Atributos
        self.raza = raza 
        self.nombre = nombre

        #Esperamos valor booleano Verdadero/Falso
        self.puntos = puntos

haskie = Perro(raza='huskie',nombre='Benito',puntos=False) #podemos definir diferentes variables así