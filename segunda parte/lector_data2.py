# se importa la clase PuntPlay2, os para manejar rutas de archivos y csv para leer y escribir archivos csv
from punt_play2 import PuntPlay2
import os
import csv

class LectorData2: # se crea la clase LectorData2
    def __init__(self, data_dir="C:\\data\\primeraprogramada"): 
        self.__data_dir = data_dir # guarda la ruta del directorio de archivos

    def leer_punts(self): # acá se leen los archivos
        punts = []
        print("Buscando archivos...")

        for year in range(2009, 2018): # recorre los años desde 2009 hasta 2017 ya que es rango de años de los archivos
            file_path = os.path.join(self.__data_dir, f"pbp_{year}.csv") # se crea la ruta completa del archivo
            print(f"Buscando archivo: {file_path}")

            if os.path.exists(file_path): # verifica que el archivo exista
                print(f"Archivo encontrado: {file_path}")
                with open(file_path, "r", encoding="utf-8", newline='') as file: # abre el archivo en modo lectura
                    reader = csv.DictReader(file)
                    for row in reader: # itera sobre cada fila del archivo
                        if row['PlayType'] == 'Punt' and 'Fumble' not in row['desc']: # verifica si la jugada es un punt sin fumble
                            punts.append(PuntPlay2( # crea un objeto en puntplay2 y lo agrega a la lista
                                row['GameID'], row['AwayTeam'], row['HomeTeam'],
                                int(row['Yards.Gained']), int(row['qtr']), row['time'], row['Date']
                            ))
                    print(f"Total de punts encontrados: {len(punts)}") # imprime cuantos punts se encontraron
                return punts
                 
    def guardar_resultados(self, punts, filename, tiempo_ejecucion): # se guardan los archivos
        
        try:
            if not filename.endswith('.csv'):
                filename = filename.replace('.txt', '.csv')
            
            output_path = os.path.join(self.__data_dir, filename)
            
            with open(output_path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                
                writer.writerow(['Tiempo de ejecución (segundos)', f"{tiempo_ejecucion:.4f}"])
                writer.writerow([])  
                
                headers = ['Fecha', 'Tiempo', 'Away Team', 'Home Team', 'Cuarto', 'Distancia (yds)', 'Game ID']
                writer.writerow(headers)

                for punt in punts:
                    writer.writerow([
                        punt.get_date(),
                        punt._PuntPlay2__time, 
                        punt.get_AwayTeam(),
                        punt.get_HomeTeam(),
                        punt.get_qtr(),
                        punt.get_distance(),
                        punt.get_GamedID()
                    ])
                    
            print(f"Resultados guardados en: {output_path}")
        except Exception as e:
            print(f"Error guardando resultados en {filename}: {str(e)}")