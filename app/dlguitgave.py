import FreeSimpleGUI as sg

from .dlguitgave_layout import dlgUitgaveLayout

class DlgUitgave:
    def toon(self, status, oCollectie, oUitgave):
        detailVenster = sg.Window(
            title = 'UITGAVE BOODSCHAP',
            layout = dlgUitgaveLayout(status, oUitgave),
            modal = True,
            disable_close = True,
            resizable = False,
            finalize = True
        )

        detailVenster['-INP-WINKEL-'].update(oUitgave.winkel)
        detailVenster['-INP-BEDRAG-'].update(f'{oUitgave.bedrag:0.2f}')
        detailVenster['-BTN-VERWIJDER-'].update(visible = False if status == 'NIEUW' else True)

        while True:
            evt, vals = detailVenster.read()

            match evt:
                case '-BTN-VERWIJDER-':
                    if sg.popup_yes_no('Wil je deze uitgave uit de lijst verwijderen ?',
                                       title = 'Uitgave verwijderen') == 'Yes':
                        try:
                            oCollectie.verwijder(oUitgave)
                        except Exception as ex:
                            sg.popup(ex, title='VERWIJDER')
                    break

                case '-BTN-BEWAAR-':
                    winkel = vals['-INP-WINKEL-'].strip()
                    bedrag = vals['-INP-BEDRAG-'].strip()

                    try:
                        oCollectie.update(oUitgave, winkel, bedrag)
                        break
                    except Exception as ex:
                        sg.popup_error(
                            ex,
                            title = 'FOUT...'
                        )

                case '-BTN-ANNULEER-':
                    status = 'ANNULEER'
                    break

        detailVenster.close()