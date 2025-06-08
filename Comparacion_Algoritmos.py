import random
import time

#Primer algoritmo a analizar: Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#Segundo algoritmo a analizar: Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

#Función para generar una lista aleatoria
def generar_lista(tamaño):
    return [random.randint(0, 10000) for _ in range(tamaño)]

#Función para comparar tiempos
def comparar_algoritmos():
    tamaño = 1000
    lista_original = generar_lista(tamaño)

    lista_bubble = lista_original.copy()
    lista_merge = lista_original.copy()

    #Calculamos los tiempos para cada uno
    inicio_bubble = time.time()
    bubble_sort(lista_bubble)
    fin_bubble = time.time()
    tiempo_bubble = fin_bubble - inicio_bubble

    inicio_merge = time.time()
    merge_sort(lista_merge)
    fin_merge = time.time()
    tiempo_merge = fin_merge - inicio_merge

    #Mostramos los resultados obtenidos
    print(f"Tiempo Bubble Sort: {tiempo_bubble:.6f} segundos")
    print(f"Tiempo Merge Sort:  {tiempo_merge:.6f} segundos")

comparar_algoritmos()
