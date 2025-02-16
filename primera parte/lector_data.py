from punt_play import PuntPlay
import csv
import os

class LectorData:
    def __init__(self, data_dir="C:\\data\\primeraprogramada"):  # Corregido el paréntesis
        self.data_dir = data_dir

    def leer_punts(self):
        punts = []

        for year in range(2009, 2018):
            file_path = os.path.join(self.data_dir, f"pbp_{year}.csv")
            print(f"Buscando archivo: {file_path}")
            
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    reader = csv.DictReader(file)

                    for row in reader:
                        # Corregido: 'desc' debe ser una columna del CSV
                        desc = row.get('Description', '').lower()  # Usando get() para evitar KeyError

                        if "punt" in desc and "fumble" not in desc:
                            # Corregido: sintaxis de creación de PuntPlay y formato de teams
                            punts.append(PuntPlay(
                                row.get('GameID', ''),
                                f"{row.get('AwayTeam', '')}@{row.get('HomeTeam', '')}",  # Corregido el formato
                                row.get('Yards.Gained', 0),  # Valor por defecto 0
                                row.get('qtr', 1)  # Valor por defecto 1
                            ))
            else:
                print(f"Archivo no encontrado: {file_path}")

        return punts
    
    def guardar_csv(self, lista_punts, algoritmo):
        output_path = os.path.join(self.data_dir, f"{algoritmo}-resultado.csv")

        with open(output_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # Corregido: writerow recibe una lista, no un diccionario
            writer.writerow(["GameID", "Teams", "YardsGained", "Qtr"])

            for punt in lista_punts:
                # Corregido: acceso a atributos privados usando __str__
                punt_data = str(punt).split(', ')
                writer.writerow(punt_data)

        print(f"Archivo guardado: {output_path}")