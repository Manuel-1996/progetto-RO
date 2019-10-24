from citta import citta
from popolazione import popolazione
import random
from Algoritmo_Genetico import Algoritmo_Genetico


class Main:
    file = open("risultati.txt", mode='w')
    initpercorso = []
    if __name__ == "__main__":

        numcitta = input("Inserire il numero delle citta/paesi : ")
        index = 0
        orig = input("Location:")
        cit = citta(orig)
        initpercorso = initpercorso + [cit]
        while (index < int(numcitta) - 1):
            orig = input("OtherLocation:")
            cit = citta(orig)
            initpercorso = initpercorso + [cit]
            index = index + 1
        print("\nBene.Cominciamo")
        print("\nCitta Inserite : ")
        for citta in initpercorso:
            print(citta.get_nome())
        input()

        generazioni = 0
        popolazioneiniziale = popolazione(initpercorso)

        popolazioneiniziale.ordina_fitnes()
        file.writelines("POPOLAZIONE N.ro ")
        file.writelines(str(generazioni) + "\n")
        file.writelines(
            "Percorso                                                                                          Durata Viaggio         [Km]\n")
        generazioni = generazioni + 1
        popolazioneiniziale.stampa(file)
        print("Generazioni Effettuata")
        algoritmo_genetico = Algoritmo_Genetico(initpercorso)
        while (generazioni < 20):
            popolazione = algoritmo_genetico.evoluzione(popolazioneiniziale)
            popolazione.ordina_fitnes()
            file.writelines("POPOLAZIONE N.ro ")
            generazioni = generazioni + 1

            file.writelines(str(generazioni) + "\n")
            file.writelines(
                "Percorso                                                           Durata Viaggio        [Km]\n")
            popolazione.stampa(file)
            print("generazione Effettuata")
            popolazioneiniziale = popolazione

        file.writelines("\n\nmiglior percorso trovato \n")
       # for index in range(len(popolazioneiniziale.get_percorsi()[0].get_citta())):
       #     file.writelines(str(popolazione.get_percorsi()[0].get_citta()[index].get_nome) + "  ")
       #     file.writelines(
       #         "\n Durata Viaggio\n" + self.converti_minuti_ore(popolazione.get_percorsi()[0].get_fitness()))
        file.close()

    def converti_minuti_ore(self, minuti):
        ore = int(minuti / 60)
        minuti = minuti - (ore * 60)
        return str(ore) + ":" + str(minuti) + ":00"

