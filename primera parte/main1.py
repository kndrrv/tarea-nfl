# importamos lo que necesitamos
from lector_data import LectorData
from algoritmos import SortingAlgorithms
import time
from datetime import datetime
import copy

def main():
    lector = LectorData()
    
    print("Leyendo archivos...")
    punt_plays = lector.leer_punts()
    print(f"Se encontraron {len(punt_plays)} jugadas de punt")
    
    algoritmos = [ # definimos la lista de los algoritmos que vamos a ejecutar
        ("BubbleSort", SortingAlgorithms.bubble_sort),
        ("InsertionSort", SortingAlgorithms.insertion_sort),
        ("MergeSort-Recursivo", SortingAlgorithms.merge_sort_recursive),
        ("MergeSort-Iterativo", SortingAlgorithms.merge_sort_iterative),
        ("QuickSort-Recursivo", SortingAlgorithms.quicksort_recursive),
        ("QuickSort-Iterativo", SortingAlgorithms.quicksort_iterative)
    ]
  
    for nombre, algoritmo in algoritmos: # se ejecutan los algoritmos
        print(f"\nEjecutando {nombre}...")
        
        plays_copy = copy.deepcopy(punt_plays) # crear una copia de la lista para cada algoritmo
        
        tiempo_inicio = time.time() # mide el tiempo de inicio
        inicio_str = datetime.fromtimestamp(tiempo_inicio).strftime('%H:%M:%S.%f')
        
        plays_ordenadas, comparaciones, intercambios = algoritmo(plays_copy)
        
        tiempo_fin = time.time() # mide el tiempo final
        fin_str = datetime.fromtimestamp(tiempo_fin).strftime('%H:%M:%S.%f')
        duracion = tiempo_fin - tiempo_inicio
        
        lector.guardar_csv(plays_ordenadas, nombre)
        
        # imprime las estadisticas
        print(f"Estadísticas para {nombre}:")
        print(f"Tiempo de inicio: {inicio_str}")
        print(f"Tiempo final: {fin_str}")
        print(f"Duración: {duracion:.4f} segundos")
        print(f"Comparaciones realizadas: {comparaciones}")
        print(f"Intercambios realizados: {intercambios}")

if __name__ == "__main__":
    main()