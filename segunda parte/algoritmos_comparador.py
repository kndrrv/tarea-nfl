from datetime import datetime # se importa datetime para manejar fechas

class PlayComparator: # se crea la clase comparator
    @staticmethod
    def compare(play_a, play_b):
        date_a = datetime.strptime(play_a.get_date(), '%Y-%m-%d') # comparar por fecha
        date_b = datetime.strptime(play_b.get_date(), '%Y-%m-%d')

        if date_a < date_b: # si la fecha de play_a es menor que la de play_b
            return -1
        elif date_a > date_b: # viceversa
            return 1

        if play_a.get_qtr() < play_b.get_qtr(): # si el cuarto de play_a es menor que el de play_b
            return -1
        elif play_a.get_qtr() > play_b.get_qtr(): # viceversa
            return 1

        if play_a.get_distance() < play_b.get_distance(): # si la distancia de play_a es menor que la de play_b
            return -1
        elif play_a.get_distance() > play_b.get_distance(): # viceversa
            return 1

        time_a = play_a.get_time() # se obtienen los tiempos en segundos
        time_b = play_b.get_time()

        if time_a < time_b: # si el tiempo de play_a es menor que play_b
            return -1
        elif time_a > time_b: # viceversa
            return 1

        return 0 # si todos son iguales retorna 0

class SortingAlgorithms: # se crea la clase algoritmos
    def __init__(self):
        self.__comparator = PlayComparator()

    def bubble_sort(self, arr): # ordena una lista con el algoritmo bubblesort
        n = len(arr) # longitud del arreglo
        for i in range(n): 
            for j in range(0, n - i - 1):
                if self.__comparator.compare(arr[j], arr[j + 1]) > 0: # comparar elementos
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr # retorna el array ordenado

    def insertion_sort(self, arr): # ordena con el algortimo insertionsort
        for i in range(1, len(arr)): # bucle desde el segundo elemento hasta el fianal
            key = arr[i]
            j = i - 1
            while j >= 0 and self.__comparator.compare(arr[j], key) > 0:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def merge_sort_recursive(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = self.merge_sort_recursive(left)
        right = self.merge_sort_recursive(right)

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if self.__comparator.compare(left[i], right[j]) <= 0:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort_iterative(self, arr):
        if len(arr) <= 1:
            return arr

        temp = arr.copy()
        n = len(arr)
        
        size = 1
        while size < n:
            for left in range(0, n - size, size * 2):
                mid = left + size
                right = min(left + size * 2, n)
                
                i = left
                j = mid
                k = left
                
                while i < mid and j < right:
                    if self.__comparator.compare(arr[i], arr[j]) <= 0:
                        temp[k] = arr[i]
                        i += 1
                    else:
                        temp[k] = arr[j]
                        j += 1
                    k += 1
                
                while i < mid:
                    temp[k] = arr[i]
                    i += 1
                    k += 1
                    
                while j < right:
                    temp[k] = arr[j]
                    j += 1
                    k += 1
            
            for i in range(n):
                arr[i] = temp[i]
                
            size *= 2
            
        return arr

    def quick_sort_recursive(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            return self.quick_sort_recursive_helper(arr, 0, len(arr) - 1)

    def quick_sort_recursive_helper(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort_recursive_helper(arr, low, pi - 1)
            self.quick_sort_recursive_helper(arr, pi + 1, high)
        return arr

    def quick_sort_iterative(self, arr):
        if len(arr) <= 1:
            return arr
            
        stack = []
        
        low = 0
        high = len(arr) - 1
        stack.append((low, high))
        
        while stack:
            low, high = stack.pop()
            
            if low < high:
                pi = self.partition(arr, low, high)
                
                if pi - 1 > low:
                    stack.append((low, pi - 1))
                    
                if pi + 1 < high:
                    stack.append((pi + 1, high))
                    
        return arr

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if self.__comparator.compare(arr[j], pivot) <= 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
