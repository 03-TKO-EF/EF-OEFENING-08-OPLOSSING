import FreeSimpleGUI as sg
from .init_layout import vensterKop

def dlgUitgaveLayout(status, oUitgave):
    return [
        # RIJ 1
        vensterKop(),
        # RIJ 2
        [
            sg.HorizontalSeparator(
                pad = (0, 10)
            )
        ],
        # RIJ 3
        [
            sg.Text(
                text = 'Winkel',
                size = (17, 1)
            ),
            sg.Input(
                default_text = '',
                size = (15, 1),
                key = '-INP-WINKEL-'
            )
        ],
        # RIJ 4
        [
            sg.Text(
                text = 'Bedrag (in €)',
                size = (17, 1)
            ),
            sg.Input(
                default_text = '',
                size = (15, 1),
                key = '-INP-BEDRAG-',
                justification = 'right'
            )
        ],
        # RIJ 5
        [
            sg.HorizontalSeparator(
                pad = (0, 10)
            )
        ],
        # RIJ 6
        [
            sg.Push(),
            sg.Button(
                button_text = 'Verwijder',
                size = (10, 2),
                key = '-BTN-VERWIJDER-'
            ),
            sg.Button(
                button_text = 'Bewaar',
                size = (10, 2),
                key = '-BTN-BEWAAR-'
            ),
            sg.Button(
                button_text = 'Annuleer',
                size = (10, 2),
                key = '-BTN-ANNULEER-'
            ),
        ]
    ]