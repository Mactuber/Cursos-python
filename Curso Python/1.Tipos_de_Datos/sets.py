# miset = set()

# miset.add(1)
# miset.add(2)

# print(miset)

# miset tomará el valor de {1}, solo tienen valores únicos, si poner otro .add(1) solo cogerá un único 1
# lo usamos cuando queremos ver los valores de una lista que se esta repitiendo

miset = set()

milista = [1,1,1,1,2,2,2,2,3,3,3,3]

set(milista)

print(set(milista))

# solo mostrará que tenemos el 1,2 y 3
# los sets no tienen orden