# importar, punt_play csv y os para poder leer los archivos
from punt_play import PuntPlay
import csv
import os

class LectorData:
    def __init__(self, data_dir = "c:\\data\\primeraprogramada)"): # constructor de la clase lector data para recibir el directorio donde se almacenan los archivos
        self.data_dir = data_dir # ruta de los archivos

    def leer_punts(self): # acá se leen los archivos, filtra las jugadas que son punt y no tienen fumble
        punts = [] # lista para almacenar los punts

        for year in range(2009, 2018): # recorre los años del 2009 al 2017 ya que es el rango de años de los archivos
            file_path = os.path.join(self.data_dir, f"pbp_{year}.csv") # crea la ruta completa del archivo

            if os.path.exists(file_path): # verifica que el archivo exista
                with open(file_path, "r", encoding = "utf-8") as file:
                    reader = csv.DictReader(file)

                    for row in reader:
                        desc = row[desc].lower() # convierte la descripcion en minusculas

                        if "punt" in desc and "fumble" not in desc:
                            punts.append(PuntPlay)(
                                row["GameID"],
                                f"{row['AwayTeam'] @ ['HomeTeam']}",
                                int(row['Yards.Gained']),
                                int(row['qtr'])
                            )
            else:
                print(f"Archivo no encontrado: {file_path}")

        return punts
    
    def guardar_csv(self, lista_punts, algoritmo): # guarda la lista ordenada en un archivo csv
        output_path = os.path.join(self.data_dir, f"{algoritmo}-resultado.csv")

        with open(output_path, "w", newline = "", encoding = "utf-8") as file:
            writer = csv.writer(file)
            writer.writerow["GameID", "Teams", "YardsGained", "Qrt"]

            for punt in lista_punts:
                writer.writerow([punt.GameID, punt.Teams, punt.YardsGained, punt.Qrt])

        print(f"archivo guardado: {output_path}") # muestra si se guardó el archivo