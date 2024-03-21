def mirar_numero_par_en_lista(num_list):

    for number in num_list:
        if number % 2 == 0:
            print('True')
            return True
            

        else:
            pass
    print('False')
    return False  #asi miramos is tenemos números pares, es falso si no encuentra números pares en la lista
   

mirar_numero_par_en_lista([2,3,5])