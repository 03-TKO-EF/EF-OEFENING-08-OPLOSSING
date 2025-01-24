import FreeSimpleGUI as sg
from . import init_layout

from .app_layout import appLayout
from entiteit.collectie import Collectie
from .dlguitgave import DlgUitgave

class App:
    def __init__(self):
        self._collectie = Collectie()

    def toon(self):
        venster = sg.Window(
            title = 'UITGAVEN BOODSCHAPPEN',
            layout = appLayout(),
            disable_close = True,
            finalize = True            
        )

        venster['-TXT-TOTAAL-'].update(self._collectie.totaal())
        venster['-TXT-GEMIDDELDE-'].update(self._collectie.gemiddelde())
        venster['-LBX-UITGAVEN-'].update(values = self._collectie.lijst())

        while True:
            evt, vals = venster.read()

            match evt:
                case sg.WIN_CLOSED | '-BTN-AFSLUITEN-':
                    self._collectie.bewaar()
                    break

                case '-BTN-NIEUW-':
                    oUitgave = self._collectie.nieuw()
                    self._update(venster, 'NIEUW', oUitgave)

                case '-LBX-UITGAVEN-':
                    if len(oUitgave = vals['-LBX-UITGAVEN-']) > 0:
                        oUitgave = vals['-LBX-UITGAVEN-'][0]
                        self._update(venster, 'WIJZIG', oUitgave)

                case '-RBN-WINKEL-':
                    self._sorteer(venster, 'WINKEL')

                case '-RBN-BEDRAG-':
                    self._sorteer(venster, 'BEDRAG')

        venster.close()

    def _sorteer(self, venster, sorteerMode):
        self._collectie.sorteer(sorteerMode)
        venster['-LBX-UITGAVEN-'].update(values = self._collectie.lijst())

    def _update(self, venster, status, oUitgave):
        dlgUitgave = DlgUitgave()
        dlgUitgave.toon(status, self._collectie, oUitgave)
        
        venster['-TXT-TOTAAL-'].update(self._collectie.totaal())
        venster['-TXT-GEMIDDELDE-'].update(self._collectie.gemiddelde())
        venster['-LBX-UITGAVEN-'].update(values = self._collectie.lijst())