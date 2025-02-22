
import time
import copy
from algoritmos_comparador import SortingAlgorithms
from lector_data2 import LectorData2

def main():
    # inicializar el lector de datos y algoritmos
    lector = LectorData2()
    sorting = SortingAlgorithms()
    
    plays = lector.leer_punts() # lee los datos
    if not plays:
        print("No se encontraron jugadas para ordenar")
        return

    algorithms = { # algortimos a ejecutar
        'Bubble': sorting.bubble_sort,
        'Insertion': sorting.insertion_sort,
        'Merge Recursive': sorting.merge_sort_recursive,
        'Merge Iterative': sorting.merge_sort_iterative,
        'Quick Recursive': sorting.quick_sort_recursive,
        'Quick Iterative': sorting.quick_sort_iterative
    }

    for name, algorithm in algorithms.items():
        print(f"\nEjecutando algoritmo de ordenamiento: {name}")
        
        plays_copy = copy.deepcopy(plays)
        
        start_time = time.time()
        sorted_plays = algorithm(plays_copy)
        execution_time = time.time() - start_time
        
        print(f"Tiempo de ejecución: {execution_time:.4f} segundos")
        
        lector.guardar_resultados(sorted_plays, f"resultados_{name.lower()}.csv", execution_time)

if __name__ == "__main__":
    main()