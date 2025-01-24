import re

class Uitgave:
    def __init__(self, winkel:str = '', bedrag:float = 0.0) -> None:
        '''
        constructor
        '''
        self._sorteerMode = 'WINKEL'

        self._winkel = winkel
        self._bedrag = bedrag

    def sorteer(self, sorteerMode:str) -> None:
        '''
        zet de sorteerMode op WINKEL of BEDRAG

        :param sorteerMode:str
        '''
        self._sorteerMode = sorteerMode

    @property
    def winkel(self) -> str:
        '''
        levert de inhoud van de eigenschap _winkel

        :return :str
        '''
        return self._winkel
    
    @winkel.setter
    def winkel(self, winkel:str) -> None:
        '''
        kent een waarde toe aan de eigenschap _winkel

        :param winkel:str
        '''
        winkel = winkel.strip().upper()
        if len(winkel) == 0:
            raise Exception('\'winkel\' is een vereist veld')
        else:
            self._winkel = winkel

    @property
    def bedrag(self) -> float:
        '''
        levert de inhoud van de eigenschap _bedrag

        :return :float
        '''
        return self._bedrag
    
    @bedrag.setter
    def bedrag(self, bedrag:str) -> None:
        '''
        kent een waarde toe aan de eigenschap _bedrag

        :param bedrag:float
        '''
        bedrag = bedrag.strip().strip('.')
        if re.match(r'^\d+(.\d+)?$', bedrag):
            self._bedrag = float(bedrag)
        else:
            raise Exception('\'bedrag\' is vereist en bestaat uit een positief decimaal getal')

    def __str__(self) -> str:
        return f'{self._bedrag:10.2f} | {self._winkel}'
    
    def __repr__(self):
        return f'{self.__class__.__name__}(winkel="{self._winkel}", bedrag={self._bedrag})'
    
    def __lt__(self, oUitgave):
        if self._sorteerMode == 'WINKEL':
            return self._winkel < oUitgave._winkel
        else:
            return self._bedrag < oUitgave._bedrag
    
    def __le__(self, oUitgave):
        if self._sorteerMode == 'WINKEL':
            return self._winkel <= oUitgave._winkel
        else:
            return self._bedrag <= oUitgave._bedrag
    
    def __gt__(self, oUitgave):
        if self._sorteerMode == 'WINKEL':
            return self._winkel > oUitgave._winkel
        else:
            return self._bedrag > oUitgave._bedrag
    
    def __ge__(self, oUitgave):
        if self._sorteerMode == 'WINKEL':
            return self._winkel >= oUitgave._winkel
        else:
            return self._bedrag >= oUitgave._bedrag
    
    def __eq__(self, oUitgave):
        if self._sorteerMode == 'WINKEL':
            return self._winkel == oUitgave._winkel
        else:
            return self._bedrag == oUitgave._bedrag
