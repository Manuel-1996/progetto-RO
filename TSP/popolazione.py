from percorso import percorso
import random
import sys


class popolazione:

    def __init__(self, percorsoiniziale):
        self.percorsi = []
        self.d = {}
        for index in range(8):
            self.percorsi = self.percorsi + [percorso(percorsoiniziale)]

    def stampa(self, file):
        for percorso in self.percorsi:
            percorso.stampa(file)
        print(
            "----------------------------------------------------------------------------------------------------------------------------------")

    def get_percorsi(self):
        return self.percorsi

    def set_percorso(self, percorso, index):
        self.percorsi[index] = percorso

    def ordina_fitnes(self):
        self.insertion_sort(self.percorsi)

    def insertion_sort(self, array):
        # il ciclo for parte dal secondo elemento fino all’ultimo
        for j in range(1, len(array)):
            # ad ogni iterazione del ciclo viene salvato il valore j-esimo nella variabile key
            key = array[j]
            i = j - 1
            # si ordina tale elemento tra tutti quelli che lo precedono
            while i >= 0 and array[i].get_fitness() > key.get_fitness():
                array[i + 1] = array[i]
                i = i - 1
            array[i + 1] = key


