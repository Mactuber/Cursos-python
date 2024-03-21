# try:
#     #intentamos correr este código
#     #puede haber errores
#     resultado = 10 + '10' #el error no se ejecutará, pero el except si para avisar del error al usuario
#     print(resultado)
# except:
#     print('Parece que hay un error, escribe correctamente las variables')

try:
    resultado = 10 + '10' 
    print(resultado)
except:
    resultado = 10 + 10
    print(resultado)