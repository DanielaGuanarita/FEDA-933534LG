#Algoritmo de ordenamiento quicksort, es como un mago que divide en partes mas pequeñas, las ordena y luego las junta para que queden en orden correcto



# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [x for x in arr [1:] if x <= pivot]
#         greater = [x for x in arr [1:] if x > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)


# lista = [7, 4, 10, 1, 6, 9, 2, 3, 8, 5]
# lista_ordenada = quicksort(lista)
# print(lista_ordenada)


import random

#pivote es el numero que vamos a tomar para dividir la lista 

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort(less) + equal + quicksort(greater) 
#less especificamente en quicksort se usa para comparar elementos de la lista con el pivote, seria un "menor que"
#greater hace la misma funcion de less pero en este caso es "mayor que" el pivote

# Ejemplo de uso:
lista = [5, 2, 8, 1, 4]
lista_ordenada = quicksort(lista)
print(lista_ordenada)

