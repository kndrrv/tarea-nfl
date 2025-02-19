# se importa la clase PuntPlay, os para manejar rutas de archivos y csv para leer y escribir archivos csv
from punt_play import PuntPlay
import os
import csv

class LectorData: # se crea la clase LectorData para poder leer y guardar los archivos
    def __init__(self, data_dir="C:\\data\\primeraprogramada"):
        self.data_dir = data_dir # guarda la ruta del directorio de datos

    def leer_punts(self): # acá se leen los archivos, filtra las jugadas que son punt y no tienen fumble
        punts = []
        print("Buscando archivos...")
        
        for year in range(2009, 2018): # recorre los años desde 2009 hasta 2017 ya que es el rango de años de los archivos
            file_path = os.path.join(self.data_dir, f"pbp_{year}.csv") # crea la ruta completa del archivo
            print(f"Buscando archivo: {file_path}")
            
            if os.path.exists(file_path): # verifica que el archivo exista
                print(f"Archivo encontrado: {file_path}")
                with open(file_path, "r", encoding="utf-8") as file: # abre el archivo en modo lectura
                    reader = csv.DictReader(file)
                    row_count = 0 # contador de filas procesadas
                    punt_count = 0 # contador de jugadas de punt encontradas
                    
                    for row in reader: # recorre cada fila del archivos csv
                        row_count += 1 # e incrementa el contador
                        desc = row.get('desc', '').lower() if row.get('desc') is not None else '' # obtiene la descripción de la jugada y la convierte en minúsculas
                        
                        if "punt" in desc and "fumble" not in desc: # verifica si la ugada es un punt sin fumble
                            punt_count += 1 # incrementa el contador de punts
                            try:
                                punt = PuntPlay( # se crea un objeto con los datos de la fila
                                    row.get('GameID', ''),
                                    f"{row.get('AwayTeam', '')}@{row.get('HomeTeam', '')}",
                                    row.get('Yards.Gained', '0'),
                                    row.get('qtr', '1')
                                )
                                punts.append(punt)
                            except Exception as e: # manea errores al crear el objeto
                                print(f"Error en fila {row_count}: {e}")
                                print(f"Datos de la fila: {row}")
                    
                    print(f"Archivo {year}: Procesadas {row_count} filas, encontrados {punt_count} punts") # muestra las estadísticas del arcivo procesado
            else:
                print(f"Archivo no encontrado: {file_path}") # muestra mensaje si el archivo no existe

        print(f"Total de punts encontrados: {len(punts)}") # muestra el total de punts encontrados
        return punts

    def guardar_csv(self, lista_punts, algoritmo): #guarda la lista de punts en un archivo csv
        if not lista_punts:
            print(f"Advertencia: Lista vacía para {algoritmo}")
            return
            
        output_path = os.path.join(self.data_dir, f"{algoritmo}-resultado.csv") # construye la ruta del archivo de salida
        
        with open(output_path, "w", newline="", encoding="utf-8") as file: # abre el archivo en modo escritura
            writer = csv.writer(file)
            writer.writerow(["GameID", "Teams", "YardsGained", "Qtr"]) # escribe la cabecera 
            
            for punt in lista_punts:
                punt_str = str(punt).split(', ')
                writer.writerow(punt_str)
                
        print(f"Archivo guardado: {output_path}") # mensaje de que se guardó el archivo