def insertion_sort(lista):
    length = len(lista)
    for ind in range(1,length):
        current_value = lista[ind]
        j = ind-1
        while(lista[j]>current_value and j>=0):
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = current_value
    return lista

lista = [4,7,9,1,5,0,8,6,2]
print(insertion_sort(lista))e