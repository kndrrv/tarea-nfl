# se importa csv y os para poder leer los archivos
import csv
import os

class PuntPlay: # se crea la clase para representar la jugada punt
    def __init__(self, game_id, teams, yards, quarter):
        self.__game_id = game_id # el ID del juego
        self.__teams = teams # equipos jugando
        self.__yards = int(yards) # yardas ganadas en la jugada
        self.__quarter = int(quarter) # cuarto en el que ocurrió la jugada

    def __str__(self, other): # esto devuelve na representación en string de la jugada
        return f"{self.__game_id}, {self.__teams}, {self.__yards}, {self.__quarter}"

    def __eq__(self, other):
        return self.__yards == other.__yards

    def __lt__(self, other):
        return self.__yards < other.__yards

    def __gt__(self, other):
        return self.__yards > other.__yards

    def get_yards(self):
        return self.__yards