# importar punt_play, csv y os
from punt_play import PuntPlay
import csv
import os

class LectorData:
    def __init__(self, data_dir="C:\\data\\primeraprogramada"):  # # constructor de la clase lector data para recibir el directorio donde se almacenan los archivos
        self.data_dir = data_dir

    def leer_punts(self):# acá se leen los archivos, filtra las jugadas que son punt y no tienen fumble
        punts = []

        for year in range(2009, 2018): # recorre los años del 2009 al 2017 ya que es el rango de años de los archivos
            file_path = os.path.join(self.data_dir, f"pbp_{year}.csv") # crea la ruta completa del archivo
            print(f"Buscando archivo: {file_path}")
            
            if os.path.exists(file_path): # verifica que el archivo exista
                with open(file_path, "r", encoding="utf-8") as file:
                    reader = csv.DictReader(file)

                    for row in reader:
                        desc = row.get('Description', '').lower()  # 

                        if "punt" in desc and "fumble" not in desc:
                            punts.append(PuntPlay(
                                row.get('GameID', ''),
                                f"{row.get('AwayTeam', '')}@{row.get('HomeTeam', '')}", 
                                row.get('Yards.Gained', 0),  # valor por defecto 0
                                row.get('qtr', 1)  # valor por defecto 1
                            ))
            else:
                print(f"Archivo no encontrado: {file_path}")

        return punts
    
    def guardar_csv(self, lista_punts, algoritmo): # guarda la lista ordenada en un archivo csv
        output_path = os.path.join(self.data_dir, f"{algoritmo}-resultado.csv")

        with open(output_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["GameID", "Teams", "YardsGained", "Qtr"])

            for punt in lista_punts:
                punt_data = str(punt).split(', ')
                writer.writerow(punt_data)

        print(f"Archivo guardado: {output_path}") # muestra si se guardó el archivo