import archivo1_modulos_y_pack

print("Nivel Top en archivo2_modlos_y_pack.py")

archivo1_modulos_y_pack.func()

if __name__ == '__main__':
    print('archivo2_modulos_y_pack.py esta siendo corrido directamente!')
else:
    print('archivo2_modulos_y_pack.py esta siendo IMPORTADO!')

#archivo 1 se importa y el 2 esta corriendo directamente