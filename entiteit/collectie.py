from .uitgave import Uitgave
from statistics import mean
import json
from os.path import exists

class Collectie:
    def __init__(self):
        self._uitgaven = []

        if exists('data/uitgaven.json'):
            with open('data/uitgaven.json', 'rt', encoding='utf-8') as bestand:
                lijstUitgaven = json.load(bestand)['lijstUitgaven']
                for itemUitgave in lijstUitgaven:
                    self._uitgaven.append(Uitgave(winkel = itemUitgave['winkel'], bedrag = itemUitgave['bedrag']))

    def nieuw(self) -> Uitgave:
        '''
        creëert een nieuwe instantie van de klasse Uitgave

        :return :Uitgave
        '''
        return Uitgave()
    
    def update(self, oUitgave:Uitgave, winkel:str='', bedrag:str='0.0') -> None:
        '''
        update een instantie van de klasse Uitgave
        '''
        if oUitgave not in  self._uitgaven:
            self._uitgaven.append(oUitgave)

        oUitgave.winkel = winkel
        oUitgave.bedrag = bedrag

    def verwijder(self, oUitgave) -> None:
        '''
        verwijdert het object oUitgave uit de lijst met uitgaven

        :param oUitgave:Uitgave
        '''
        if oUitgave in self._uitgaven:
            self._uitgaven.remove(oUitgave)

    def totaal(self) -> float:
        '''
        berekent het totaal aan uitgaven

        :return :float
        '''
        totaal = 0

        if len(self._uitgaven) > 0:
            for oUitgave in self._uitgaven:
                totaal += oUitgave.bedrag

        return round(totaal, 2)

    def gemiddelde(self) -> float:
        '''
        berekent de gemiddelde uitgave

        :return :float
        '''
        gemiddelde = 0.0
        bedragen = []

        if len(self._uitgaven) > 0:
            for oUitgave in self._uitgaven:
                bedragen.append(oUitgave.bedrag)
                                
            gemiddelde = mean(bedragen)

        return round(gemiddelde, 2)
    
    def lijst(self) -> list:
        '''
        levert de inhoud van de eigenschap _uitgaven

        :return :list[Uitgave]
        '''
        return self._uitgaven
    
    def sorteer(self, sorteerMode:str='WINKEL') -> None:
        '''
        zet de sorteerMode

        :param sorteerMode:str
        '''
        for oUitgave in self._uitgaven:
            oUitgave.sorteer(sorteerMode)

        self._uitgaven = sorted(self._uitgaven)

    def bewaar(self) -> None:
        '''
        schrijft _uitgaven weg naar JSON-bestand
        '''
        lijstUitgaven = []

        for oUitgave in self._uitgaven:
            lijstUitgaven.append(
                {
                    'winkel': oUitgave.winkel,
                    'bedrag': oUitgave.bedrag
                }
            )

        with open('data/uitgaven.json', 'wt', encoding='utf-8') as bestand:
            json.dump({'lijstUitgaven': lijstUitgaven}, bestand, indent = 4)