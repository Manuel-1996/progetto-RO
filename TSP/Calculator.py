class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.
    The decorated class can define one `__init__` function that
    takes only the `self` argument. Also, the decorated class cannot be
    inherited from. Other than that, there are no restrictions that apply
    to the decorated class.
    To get the singleton instance, use the `instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.
    """
    def __init__(self, decorated):
        self._decorated = decorated
    def instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.
        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance
    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')
import urllib.parse
import requests
from citta import citta
initpercorso = [citta("Trapani"),citta("Cosenza"),citta("Bolzano"),citta("Novara"),citta("Arezzo"),citta("Barletta"),citta("Pisa"),citta("Lucca"),citta("Viterbo"),citta("Savona")]
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "AbrBmasLEQOJRu2dOqTSwolJAXnALuJD"
@Singleton
class Calculator:
    
    def __init__(self):
        self.vettore=[]
        print("calculator_create")
        print("CALCOLO DISTANZE E TEMPI")
        distanzekm={}
        tempi={}
        for i in range(0,len(initpercorso)):
            list={}
            list_tempi={}
            for j in range(0,len(initpercorso)):
                if(initpercorso[i].get_nome()==initpercorso[j].get_nome()) : 
                    list[initpercorso[j].get_nome()] = 0
                    list_tempi[initpercorso[j].get_nome()] = 0
                else:
                    url = main_api + urllib.parse.urlencode({"key": key, "from": initpercorso[i].get_nome(), "to": initpercorso[j].get_nome(), "unit": "k"}) 
                    json_data = requests.get(url).json()
                    dist = float(json_data["route"]["distance"])
                    tempo = float(json_data["route"]["time"])
                    list[initpercorso[j].get_nome()] = dist
                    list_tempi[initpercorso[j].get_nome()] = tempo
            distanzekm.setdefault(initpercorso[i].get_nome(),list)
            tempi.setdefault(initpercorso[i].get_nome(),list_tempi)
        self.vettore = [distanzekm,tempi]
    
    def get_vettore(self):
        return self.vettore
        

