# se importa la clase PuntPlay, Lista, Tuple y random
from punt_play import PuntPlay
from typing import List
from typing import Tuple
import random

class SortingAlgorithms: # se crea la clase SortingAlgorithms que contiene los algoritmos de ordenamiento
    @staticmethod # se utiliza el método estadístico para ordenar cada algortimo
    def bubble_sort(arr: List[PuntPlay]) -> tuple: # ordena una lista usando el algoritmo bubble sort
        comparaciones = 0 # contador de comparaciones
        intercambios = 0 # contador de intercambios
        n = len(arr) ## longitud de la lista
        
        for i in range(n): # se recorre la lista
            for j in range(0, n-i-1): 
                comparaciones += 1 # incrementa las comparaciones
                if arr[j] < arr[j+1]:  # ordenar de mayor a menor
                    arr[j], arr[j+1] = arr[j+1], arr[j] # intercambia los elementos
                    intercambios += 1 # e incrementa los interccambios
        
        return arr, comparaciones, intercambios # retorna la lista ordenada y los contadores

    @staticmethod
    def insertion_sort(arr: List[PuntPlay]) -> tuple: # ordena una lista de objetos usando el algoritmo insertion sort
        comparaciones = 0 # contador de compariones
        intercambios = 0 # contador de intercambios
        
        for i in range(1, len(arr)): # recorre la lista desde el segundo elemento
            key = arr[i] # es el elemento actual a insertar
            j = i-1 # indice del elemento anterior
            while j >= 0: # mueve los elementos a la derecha
                comparaciones += 1 # incrementa las comparaciones
                if arr[j] < key:  # ordena de mayor a menor
                    arr[j + 1] = arr[j]
                    intercambios += 1 # incrementa los intercambios
                    j -= 1
                else:
                    break
            arr[j + 1] = key # inserta key en la posición correcta
            
        return arr, comparaciones, intercambios # retorna la lista ordenada y los contadores

    @staticmethod
    def merge_sort_recursive(arr: List[PuntPlay]) -> tuple: # ordena la lista usando merge sort recursivo
        comparaciones = [0] # contador de comparaciones
        intercambios = [0] # contador de intercambios
        
        def merge(left: List[PuntPlay], right: List[PuntPlay]) -> List[PuntPlay]: # función para mezclar los dos array ordenados
            result = [] # array resultante
            i = j = 0 # indices para recorrer left y right
            
            while i < len(left) and j < len(right): # mezclar left y right
                comparaciones[0] += 1 # incrementa comparaciones 
                if left[i] > right[j]: # ordena de mayor a menor
                    result.append(left[i]) # va añadiendo los resultados
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
                intercambios[0] += 1 # incrementa intercambios
            result.extend(left[i:]) # agrega los elementos resultantes de left y right
            result.extend(right[j:])
            return result
        
        def sort(arr: List[PuntPlay]) -> List[PuntPlay]: # función recursiva para dividir y ordenar el array
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2 # punto medio del array
            left = sort(arr[:mid]) # ordena la mitad izquierda
            right = sort(arr[mid:]) # ordena la mitad derecha
            
            return merge(left, right) # mezcla ambas mitades
        
        sorted_arr = sort(arr) # se llama la función sort y retorna los resultados
        return sorted_arr, comparaciones[0], intercambios[0]

    @staticmethod
    def merge_sort_iterative(arr: List[PuntPlay]) -> tuple: # ordena una lista usando merge sort iterativo
        comparaciones = 0 # contador de comparaciones
        intercambios = 0 # contador de intercambios
        n = len(arr) # longitud del array
        
        def merge(left: int, mid: int, right: int): # función para mezclar dos subarreglos
            nonlocal comparaciones, intercambios # usar contadores
            
            left_part = arr[left:mid + 1] # array ziquierdo
            right_part = arr[mid + 1:right + 1] # array derecho
            
            i = j = 0 # indice para recorrer left_part y right_part
            k = left # indice para el array original
            
            while i < len(left_part) and j < len(right_part): # mezclar left_part y right_part 
                comparaciones += 1 # incrementa las comparaciones
                if left_part[i] > right_part[j]: # ordena de mayor a menor
                    arr[k] = left_part[i]
                    i += 1
                else:
                    arr[k] = right_part[j]
                    j += 1
                intercambios += 1 # incrementa los intercambios
                k += 1
            
            while i < len(left_part): # agrega los elementos restantes de right_part
                arr[k] = left_part[i]
                i += 1
                k += 1
                intercambios += 1 # incrementa intercambios
            
            while j < len(right_part): # agrega elementos restantes de right_part
                arr[k] = right_part[j]
                j += 1
                k += 1
                intercambios += 1 # incrementa intercambios
        
        size = 1 
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(left + size - 1, n - 1) # punto medio
                right = min(left + 2 * size - 1, n - 1)
                merge(left, mid, right) # mexclar bloques
            size *= 2
        
        return arr, comparaciones, intercambios # retorna la lista ordenada y los contadores

    @staticmethod
    def quicksort_safe(arr: List[PuntPlay]) -> Tuple[List[PuntPlay], int, int]: # ordena una lista usando quick sort seguro con pivot aleatorio
        comparaciones = 0 # contador de comparaciones
        intercambios = 0 # contador de intercambios
        
        if len(arr) <= 1: # si la lista tiene 1 o 0 elementos, ya está ordenada
            return arr, comparaciones, intercambios
        
        def partition(low: int, high: int) -> int: # fucnión para partir el array
            nonlocal comparaciones, intercambios # usar contadores
            
            pivot_idx = random.randint(low, high) # selecciona un pivot aleatorio y lo mueve al final
            arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
            intercambios += 1 # le suma al contador
            
            pivot = arr[high] # pivot 
            i = low - 1 # indice del menor elemento
            
            for j in range(low, high): # recorre el array
                comparaciones += 1 # incrementa las comparaciones
                if arr[j] > pivot:  # ordenar de mayor a menor
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i] # intercambia elementos
                    intercambios += 1 # incrementa los intercambios
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1] # coloca el pivot en su posición correcta
            intercambios += 1 # incrementa intercambios
            return i + 1 # retorna la posición del pivot
        
        stack = [] # alamcena los límites del array
        start = 0 # indice inicial
        end = len(arr) - 1 # indice fianl
        stack.append((start, end)) # agrega los límites iniciales a la pila
        
        while stack: # procesa la pila hasta que esté vacía
            start, end = stack.pop() # obtiene los límites actuales
            
            if start < end:
                if end - start < 10: # si el arreglo es pequeño, usar insertion sort
                    for i in range(start + 1, end + 1):
                        key = arr[i]
                        j = i - 1
                        comparaciones += 1
                        while j >= start and arr[j] < key:
                            arr[j + 1] = arr[j]
                            intercambios += 1
                            j -= 1
                            if j >= start:
                                comparaciones += 1
                        arr[j + 1] = key
                else: # partir el array y agregar los nuevos límites a la pila
                    pivot_index = partition(start, end)
                    
                    if pivot_index - 1 - start < end - (pivot_index + 1): # agrega el array más pequeño para optimizar el uso de la pila
                        stack.append((pivot_index + 1, end))
                        stack.append((start, pivot_index - 1))
                    else:
                        stack.append((start, pivot_index - 1))
                        stack.append((pivot_index + 1, end))
        
        return arr, comparaciones, intercambios # retorna la lista ordenada y los contadores

    @staticmethod
    def quicksort_recursive(arr: List[PuntPlay]) -> tuple: # ordena la lista usando quicksort recursivo
        return SortingAlgorithms.quicksort_safe(arr)

    @staticmethod
    def quicksort_iterative(arr: List[PuntPlay]) -> tuple: # ordena la lista utilizando quicksort iterativo
        return SortingAlgorithms.quicksort_safe(arr)