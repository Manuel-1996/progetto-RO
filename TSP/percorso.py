from citta import citta
import random
import sys
import requests
import urllib.parse

# KEY & URL per le richiesta HTTPS al sito MaPQuest
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "ILgdVnw9nFyienjyuhPjq2TzefdbY25R"


class percorso:
    def __init__(self, citta):
        self.totale_secondi = 0
        self.boolean = False
        cittamia = [];
        self.citta = []

        for citta in citta:
            cittamia = cittamia + [citta]

        r = random.SystemRandom()
        r.shuffle(cittamia)
        self.fitness = 0
        index = 0;

        for c in cittamia:
            self.citta = self.citta + [cittamia[index]]
            index = index + 1

    def stampa(self, file):
        for i in range(len(self.citta)):
            file.writelines(self.citta[i].get_nome() + " ")
        file.writelines("                                                           " + self.converti_minuti_ore(
            self.fitness) + "                   ")
        file.writelines(str(self.calcolaDistanzaTotale()) + "\n")

    def converti_minuti_ore(self, minuti):
        ore = int(minuti / 60)
        minuti = minuti - (ore * 60)
        return str(ore) + ":" + str(minuti) + ":00"

    def set_citta(self, citta, index):
        self.citta[index] = citta

    def get_fitness(self):
        if self.boolean == False:
            self.calcolaDistanzaTotale();
            self.fitness = 1/(self.totale_secondi)
            self.boolean = True
        return self.fitness

    def get_citta(self):
        return self.citta

    # calcolaDistanzaTotale() calcola la distanza tra ogni città
    # del percorso partendo dalla prima in lista fino all'ultima, e infine
    # le somma con la distanza tra l'ultima città e la prima
    def calcolaDistanzaTotale(self):
        cities = self.get_citta();
        totale = 0
        for index in range(len(cities) - 1):
            # CREATE_URL_FOR_HTTP_REQUEST
            url = main_api + urllib.parse.urlencode(
                {"key": key, "from": cities[index].get_nome(), "to": cities[index + 1].get_nome(), "unit": "k"})
            # print("Directions from "  , cities[index].get_nome()           , " to " ,cities[index+1].get_nome(),sep=" ")
            json_data = requests.get(url).json()
            # AGGIORNO TOTALE
            totale = totale + float(json_data["route"]["distance"])
            self.totale_secondi = self.totale_secondi + json_data["route"]["time"]
        # A questo punto manca l'ultima tratta (ultima destinazione con l'origine)
        # CREATE_URL_FOR_HTTP_REQUEST
        url = main_api + urllib.parse.urlencode(
            {"key": key, "from": cities[len(cities) - 1].get_nome(), "to": cities[0].get_nome(), "unit": "k"})
        json_data = requests.get(url).json()
        # AGGIORNO TOTALE
        totale = totale + float(json_data["route"]["distance"])
        self.totale_secondi = self.totale_secondi + json_data["route"]["time"]
        return totale

    def somma_orari(self, orario1, orario2):
        ore1 = int(orario1[:2])
        minuti1 = int(orario1[3:5])
        secondi1 = int(orario1[6:8])
        ore2 = int(orario2[:2])
        minuti2 = int(orario2[3:5])
        secondi2 = int(orario2[6:8])
        secondi_tot = secondi1 + secondi2
        piu_m = 0
        piu_ora = 0
        if (secondi_tot > 59):
            secondi_tot = secondi_tot - 60
            piu_m = 1
        minuti_tot = minuti1 + minuti2 + piu_m
        if (minuti_tot > 59):
            minuti_tot = minuti_tot - 60
            piu_ora = 1
        totale = ore1 + ore2 + piu_ora
        return str(totale) + ":" + str(minuti_tot) + ":" + str(secondi_tot)

    def converti_ora_minuti(self, orario):
        ore = int(orario[:2])
        minuti = int(orario[3:5])
        secondi = int(orario[6:8])
        return (60 * ore) + minuti + (secondi / 60)


