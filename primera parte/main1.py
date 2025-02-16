from lector_data import LectorData
from algoritmos import SortingAlgorithms
import time
from datetime import datetime
import copy

def main():
    # Crear instancia del lector
    lector = LectorData()
    
    # Leer las jugadas de punt
    print("Leyendo archivos...")
    punt_plays = lector.leer_punts()
    print(f"Se encontraron {len(punt_plays)} jugadas de punt")
    
    # Definir los algoritmos a ejecutar
    algoritmos = [
        ("BubbleSort", SortingAlgorithms.bubble_sort),
        ("InsertionSort", SortingAlgorithms.insertion_sort),
        ("MergeSort-Recursivo", SortingAlgorithms.merge_sort_recursive),
        ("MergeSort-Iterativo", SortingAlgorithms.merge_sort_iterative),
        ("QuickSort-Recursivo", SortingAlgorithms.quicksort_recursive),
        ("QuickSort-Iterativo", SortingAlgorithms.quicksort_iterative)
    ]
    
    # Ejecutar cada algoritmo
    for nombre, algoritmo in algoritmos:
        print(f"\nEjecutando {nombre}...")
        
        # Crear una copia de la lista para cada algoritmo
        plays_copy = copy.deepcopy(punt_plays)
        
        # Medir tiempo de inicio
        tiempo_inicio = time.time()
        inicio_str = datetime.fromtimestamp(tiempo_inicio).strftime('%H:%M:%S.%f')
        
        # Ejecutar algoritmo
        plays_ordenadas, comparaciones, intercambios = algoritmo(plays_copy)
        
        # Medir tiempo final
        tiempo_fin = time.time()
        fin_str = datetime.fromtimestamp(tiempo_fin).strftime('%H:%M:%S.%f')
        duracion = tiempo_fin - tiempo_inicio
        
        # Guardar resultados
        lector.guardar_csv(plays_ordenadas, nombre)
        
        # Imprimir estadísticas
        print(f"Estadísticas para {nombre}:")
        print(f"Tiempo de inicio: {inicio_str}")
        print(f"Tiempo final: {fin_str}")
        print(f"Duración: {duracion:.4f} segundos")
        print(f"Comparaciones realizadas: {comparaciones}")
        print(f"Intercambios realizados: {intercambios}")

if __name__ == "__main__":
    main()