

def executar_selection_sort (lista):
    
    n = len(lista)
    
    for i in range(0, 8):
        index_menor = i
        for j in range(i+1, n):
            if lista[j] < lista[index_menor]:
                index_menor = j
                lista[i], lista[index_menor] = lista[index_menor],lista[i]
                return lista
            
    