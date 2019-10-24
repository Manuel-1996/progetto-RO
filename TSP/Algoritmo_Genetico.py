from random import random
from percorso import percorso
from popolazione import popolazione


class Algoritmo_Genetico:

    def __init__(self, percorsoiniziale):
        self.percorsoiniziale = []
        for index in range(len(percorsoiniziale)):
            self.percorsoiniziale = self.percorsoiniziale + [percorsoiniziale[index]]

    def evoluzione(self, popolazioneingresso):
        return self.mutazione_popolazione(self.crossover_popolazione(popolazioneingresso))

    # crossoverPopolazione() ritorna la popolazione dopo aver applicato l'operatore di crossover ai percorsi di essa.
    # In particolare applica l'operatore di crossover a tutti i percorsi lasciando intatto però il primo percorso
    # ossia quello con fitness maggiore (poiché i percorsi sono ordinati per fitness decrescente).
    # Successivamente seleziona a caso 2 percorsi dalla lista dei percorsi e ne fa il crossover.
    # Il risultato è inserito nella lista chiamata "crossoverPopolazione"

    def crossover_popolazione(self, popolazione_precedente):
        popolazionecross = popolazione(self.percorsoiniziale)
        popolazionecross.set_percorso(popolazione_precedente.get_percorsi()[0], 0)
        for index in range(1, len(popolazione_precedente.get_percorsi())):
            random1 = int(random() * (len(popolazione_precedente.get_percorsi())))
            random2 = int(random() * (len(popolazione_precedente.get_percorsi())))

            percorso1 = popolazione_precedente.get_percorsi()[random1]
            percorso2 = popolazione_precedente.get_percorsi()[random2]
            popolazionecross.set_percorso(self.crossover_percorso(percorso1, percorso2), index)
        return popolazionecross

    # crossoverPercorso() effettua il crossover tra due percorsi.
    # Sceglie un percorso a caso tra i due; crea un percorso intermedio inserendo in esso 5 città
    # del percorso scelto, e ponendo a null
    # le altre posizioni; tramite la funzione riempiNullsInCrossover() inserisce al posto delle posizioni
    # null tutte le città del percorso
    # non scelto tranne quelle già inserite all'interno del percorso intermedio (per garantire il vincolo di
    # attraversare ogni città una
    # sola volta)
    # Esempio:
    #
    # percorso1:           [Firenze, Roma, Reggio calabria, Napoli, Bari, Venezia, Bologna, Milano, Torino, Genova]
    # percorso2:           [Napoli, Torino, Venezia, Roma, Bari, Reggio calabria, Firenze, Genova, Milano, Bologna]
    # percorso intermedio: [Firenze, Roma, Reggio calabria, Napoli, Bari, null, null, null, null, null]
    # percorso finale:     [Firenze, Roma, Reggio calabria, Napoli, Bari, Torino, Venezia, Genova, Milano, Bologna]

    def crossover_percorso(self, percorso1, percorso2):
        percorso_finale = percorso(self.percorsoiniziale)
        citta1 = percorso1.get_citta()
        for index in range(int(len(percorso1.get_citta()) / 2)):
            percorso_finale.set_citta(percorso1.get_citta()[index], index)
        for index in range(int(len(percorso1.get_citta()) / 2), int(len(percorso1.get_citta()))):
            percorso_finale.set_citta(None, index)
        for index in range(int(len(percorso1.get_citta()) / 2), int(len(percorso1.get_citta()))):
            if percorso2.get_citta()[index] in percorso_finale.get_citta():
                pass
            else:
                percorso_finale.set_citta(percorso2.get_citta()[index], index)
        return self.riempi_nulli(percorso_finale)

    def riempi_nulli(self, percorso_finale):
        for citta in self.percorsoiniziale:
            if not (citta in percorso_finale.get_citta()):
                index = 0
                ciclo = 0
                while (ciclo < len(percorso_finale.get_citta())):
                    if percorso_finale.get_citta()[index] == None:
                        percorso_finale.set_citta(citta, index)
                        break
                    else:
                        index = index + 1
        return percorso_finale

    # mutazionePopolazione() applica l'operatore di mutazione ad ogni percorso (cromosoma) della popolazione alla quale
    # precedentemente è
    # stato applicato l'operatore di crossover.
    # In particolare applica l'operatore di mutazione ai percorsi in lista tranne al primo di essi (quello con fitness maggiore)

    # mutazionePercorso() effettua uno switch tra 2 o più città all'interno di un percorso della popolazione
    # Seleziona ogni città per la quale un numero random tra 0 e 1 è minore di PRB_MUTAZIONE;
    # per ognuna di esse seleziona poi una città
    # random con la quale deve essere scambiata; effettua lo scambio.
    # Può essere inteso anche come filtro perché garantisce la proprietà del ciclo h. : ogni città deve essere attraversata una sola volta
    # Esempio:
    #
    # percorso originale: [Firenze, Roma, Reggio calabria, Napoli, Bari, Venezia, Bologna, Milano, Torino, Genova]
    # percorso mutato:    [Firenze, Roma, Bari, Napoli, Reggio calabria, Venezia, Bologna, Torino, Milano, Genova]

    def mutazione_popolazione(self, popolazioneingresso):
        for index in range(1, len(popolazioneingresso.get_percorsi())):
            r = random()
            if r < 0.25:
                random1 = int(random() * len(popolazioneingresso.get_percorsi()[index].get_citta()))
                random2 = int(random() * len(popolazioneingresso.get_percorsi()[index].get_citta()))
                swap = popolazioneingresso.get_percorsi()[index].get_citta()[random1]
                popolazioneingresso.get_percorsi()[index].get_citta()[random1] = \
                popolazioneingresso.get_percorsi()[index].get_citta()[random2]
                popolazioneingresso.get_percorsi()[index].get_citta()[random2] = swap
            r = random()
            if r < 0.25:
                random1 = int(random() * len(popolazioneingresso.get_percorsi()[index].get_citta()))
                random2 = int(random() * len(popolazioneingresso.get_percorsi()[index].get_citta()))
                swap = popolazioneingresso.get_percorsi()[index].get_citta()[random1]
                popolazioneingresso.get_percorsi()[index].get_citta()[random1] = \
                popolazioneingresso.get_percorsi()[index].get_citta()[random2]
                popolazioneingresso.get_percorsi()[index].get_citta()[random2] = swap

        return popolazioneingresso



