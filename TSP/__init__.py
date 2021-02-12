from citta import citta
from popolazione import popolazione
import random
from Algoritmo_Genetico import algoritmo_genetico
import requests
import requests
import urllib.parse

from Calculator import Calculator

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "AbrBmasLEQOJRu2dOqTSwolJAXnALuJD"

class Main:
    file = open("./risultati/risultati.txt", mode='w')
    initpercorso = [citta("Trapani"),citta("Cosenza"),citta("Bolzano"),citta("Novara"),citta("Arezzo"),citta("Barletta"),citta("Pisa"),citta("Lucca"),citta("Viterbo"),citta("Savona")]
    #initpercorso = [citta("Trapani"),citta("Cosenza"),citta("Roma")]
    if __name__ == "__main__":
        c = Calculator.instance()
        print("INIZIO ALGORITMO")
        generazioni = 0
        popolazioneiniziale = popolazione(initpercorso)

        popolazioneiniziale.ordina_fitnes()
        #Scrivi su file 
        file.writelines("")
        file.writelines(str(generazioni) + "\n")
        file.writelines(
            "Percorso                                                                               Fitness         [Km]\n")
        generazioni = generazioni + 1
        popolazioneiniziale.stampa(file)
        print("Generazioni Effettuata--->1")
        algoritmo_genetico = Algoritmo_Genetico(initpercorso)
        while (generazioni < 40):
            popolazione = algoritmo_genetico.evoluzione(popolazioneiniziale)
            popolazione.ordina_fitnes()
            file.writelines("")
            generazioni = generazioni + 1

            file.writelines(str(generazioni) + "\n")
            file.writelines(
                "Percorso                                                       Fitness       [Km]\n")
            popolazione.stampa(file)
            print("generazione Effettuata" , generazioni,sep = "--->")
            popolazioneiniziale = popolazione

        file.writelines("\n\nmiglior percorso trovato \n")
        popolazioneiniziale.stampa_finale(file)
        file.close()
        
    def converti_minuti_ore(self, minuti):
        ore = int(minuti / 60)
        minuti = minuti - (ore * 60)
        return str(ore) + ":" + str(minuti) + ":00"

