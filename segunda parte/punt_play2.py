class PuntPlay2: # se crea la clase PuntPlay2
    def __init__(self, GameID, AwayTeam, HomeTeam, Yards_Gained, qtr, time, Date):
        self.__GameID = GameID # id del juego
        self.__AwayTeam = AwayTeam # equipo visita
        self.__HomeTeam = HomeTeam # equipo en casa
        self.__distance = Yards_Gained # distancia
        self.__qtr = qtr # cuarto
        self.__time = time # tiempo
        self.__date = Date # fecha
    
    # getters
    def get_GamedID(self):
        return self.__GameID
    
    def get_AwayTeam(self):
        return self.__AwayTeam
    
    def get_HomeTeam(self):
        return self.__HomeTeam
    
    def get_distance(self):
        return int(self.__distance)
    
    def get_qtr(self):
        return int(self.__qtr)

    def get_time(self): # método para obtener el tiempo restante en el cuarto, en segundos
        try:
            minutes, seconds = self.__time.split(':') # divide el tiempo en minutos y segundos
            return int(minutes) * 60 + int(seconds)
        except ValueError: # manejo de errores 
            print(f"Error en formato de tiempo: {self.__time}")
            return 0 # retorna 0 en caso de error
    
    def get_date(self):
        return self.__date

    def __str__(self): # método para representar la instancia como una cadena de texto
        return (f"Fecha: {self.__date}, Tiempo: {self.__time}, "
                f"Away Team: {self.__AwayTeam}, Home Team: {self.__HomeTeam}, "
                f"Cuarto: {self.__qtr}, Distancia: {self.__distance} yds")
