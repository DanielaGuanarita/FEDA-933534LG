#Algoritmo de ordenamiento quicksort, es como un mago que divide en partes mas pequeñas, las ordena y luego las junta para que queden en orden correcto

# #pivote es el numero que vamos a tomar para dividir o comparar la lista 
#arr abreviatura de array es la estructura de datos que contiene los elementos a ordenar

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr [1:] if x <= pivot]
        greater = [x for x in arr [1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


lista = [7, 4, 10, 1, 6, 9, 2, 3, 8, 5]
lista_ordenada = quicksort(lista)
print(lista_ordenada)


# import random

# #pivote es el numero que vamos a tomar para dividir o comparar la lista 
#arr abreviatura de array es la estructura de datos que contiene los elementos a ordenar

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = random.choice(arr)
#         less = [x for x in arr if x < pivot]
#         equal = [x for x in arr if x == pivot]
#         greater = [x for x in arr if x > pivot]
#         return quicksort(less) + equal + quicksort(greater) 

# #less especificamente en quicksort se usa para comparar elementos de la lista con el pivote, seria un "menor que"
# #greater hace la misma funcion de less pero en este caso es "mayor que" el pivote
# #equal nos hace referencia a los numero que son iguales que el pivot 


# # Ejemplo de uso:
# lista = [7, 4, 10, 1, 6, 9, 2, 3, 8, 5]
# lista_ordenada = quicksort(lista)
# print(lista_ordenada)

