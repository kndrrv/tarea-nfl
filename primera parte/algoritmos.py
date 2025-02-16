# se importa lista y puntplay
from typing import List
from punt_play import PuntPlay

class SortingAlgorithms: # clase que contiene los algoritmos de ordenamiento
    @staticmethod
    def bubble_sort(arr: List[PuntPlay]) -> tuple: # algoritmo bubble sort
        comparaciones = 0 # contador de comparaciones
        intercambios = 0 # contador de intercambios
        n = len(arr) 
        
        for i in range(n):
            for j in range(0, n-i-1): 
                comparaciones += 1
                if arr[j] < arr[j+1]:  # ordenar de mayor a menor
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    intercambios += 1
        
        return arr, comparaciones, intercambios # lo retorna ordenado

    @staticmethod
    def insertion_sort(arr: List[PuntPlay]) -> tuple: # algoritmo insertion sort
        comparaciones = 0
        intercambios = 0
        
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0: # mueve los elementos mayores que key a la derecha
                comparaciones += 1
                if arr[j] < key:  
                    arr[j + 1] = arr[j]
                    intercambios += 1
                    j -= 1
                else:
                    break
            arr[j + 1] = key # pone a key en la posicion correcta
            
        return arr, comparaciones, intercambios 

    @staticmethod
    def merge_sort_recursive(arr: List[PuntPlay]) -> tuple: # algoritmo merge sort recursivo
        comparaciones = [0]
        intercambios = [0]
        
        def merge(left: List[PuntPlay], right: List[PuntPlay]) -> List[PuntPlay]: # función para mezclar dos subarreglos ordenados
            result = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                comparaciones[0] += 1
                if left[i] > right[j]:  
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
                intercambios[0] += 1
            # agrega los elementos restantes de left y right
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        def sort(arr: List[PuntPlay]) -> List[PuntPlay]:
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = sort(arr[:mid])
            right = sort(arr[mid:])
            
            return merge(left, right) # mezcla ambas mitades
        
        sorted_arr = sort(arr)
        return sorted_arr, comparaciones[0], intercambios[0]

    @staticmethod
    def merge_sort_iterative(arr: List[PuntPlay]) -> tuple: # algoritmo merge sort iterativo
        comparaciones = 0
        intercambios = 0
        n = len(arr)
        
        def merge(left: int, mid: int, right: int):
            nonlocal comparaciones, intercambios
            
            left_part = arr[left:mid + 1]
            right_part = arr[mid + 1:right + 1]
            
            i = j = 0
            k = left
            
            while i < len(left_part) and j < len(right_part):
                comparaciones += 1
                if left_part[i] > right_part[j]:  
                    arr[k] = left_part[i]
                    i += 1
                else:
                    arr[k] = right_part[j]
                    j += 1
                intercambios += 1
                k += 1
            
            while i < len(left_part):
                arr[k] = left_part[i]
                i += 1
                k += 1
                intercambios += 1
            
            while j < len(right_part):
                arr[k] = right_part[j]
                j += 1
                k += 1
                intercambios += 1
        
        size = 1
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(left + size - 1, n - 1)
                right = min(left + 2 * size - 1, n - 1)
                merge(left, mid, right)
            size *= 2
        
        return arr, comparaciones, intercambios

    @staticmethod
    def quicksort_recursive(arr: List[PuntPlay]) -> tuple: # algortimo quicksort recursivo
        comparaciones = [0]
        intercambios = [0]
        
        def partition(low: int, high: int) -> int: # funcion para partirlo
            pivot = arr[high]
            i = low - 1
            
            for j in range(low, high):
                comparaciones[0] += 1
                if arr[j] > pivot:  # Ordenar de mayor a menor
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    intercambios[0] += 1
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1] # coloca al pivot en la posicion correcta
            intercambios[0] += 1
            return i + 1
        
        def sort(low: int, high: int):
            if low < high:
                pi = partition(low, high)
                sort(low, pi - 1)
                sort(pi + 1, high)
        
        sort(0, len(arr) - 1)
        return arr, comparaciones[0], intercambios[0]

    @staticmethod
    def quicksort_iterative(arr: List[PuntPlay]) -> tuple: # quicksort iterativo
        comparaciones = 0
        intercambios = 0
        
        def partition(low: int, high: int) -> int:
            nonlocal comparaciones, intercambios
            pivot = arr[high]
            i = low - 1
            
            for j in range(low, high):
                comparaciones += 1
                if arr[j] > pivot:  # Ordenar de mayor a menor
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    intercambios += 1
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            intercambios += 1
            return i + 1
        
        stack = [(0, len(arr) - 1)]
        
        while stack:
            low, high = stack.pop()
            if low < high:
                pi = partition(low, high)
                stack.append((low, pi - 1))
                stack.append((pi + 1, high))
        
        return arr, comparaciones, intercambios
