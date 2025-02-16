class PuntPlay: # se crea la clase para representar la jugada punt
    def __init__(self, game_id, teams, yards, quarter):
        self.__game_id = game_id # el ID del juego
        self.__teams = teams # equipos jugando
        self.__yards = int(yards) # yardas ganadas en la jugada
        self.__quarter = int(quarter) # cuarto en el que ocurrió la jugada

    def __str__(self): # esto devuelve na representación en string de la jugada
        return f"{self.__game_id}, {self.__teams}, {self.__yards}, {self.__quarter}"

# operadores de comparación basados en las yardas ganadas
    def __eq__(self, other):
        if not isinstance(other, PuntPlay):
            return NotImplemented
        return self.__yards == other.__yards
    
    def __lt__(self, other):
        if not isinstance(other, PuntPlay):
            return NotImplemented
        return self.__yards < other.__yards
    
    def __gt__(self, other):
        if not isinstance(other, PuntPlay):
            return NotImplemented
        return self.__yards > other.__yards
    
    def __le__(self, other):
        if not isinstance(other, PuntPlay):
            return NotImplemented
        return self.__yards <= other.__yards
    
    def __ge__(self, other):
        if not isinstance(other, PuntPlay):
            return NotImplemented
        return self.__yards >= other.__yards