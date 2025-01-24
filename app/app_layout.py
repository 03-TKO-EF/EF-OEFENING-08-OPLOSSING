import FreeSimpleGUI as sg
from .init_layout import vensterKop, fntStandaard

kolomLinks = sg.Column(
    layout = [
        [
            sg.Frame(
                title = 'Uitgaven',
                expand_x = True,
                expand_y = True,
                
                layout = [
                    [
                        sg.Listbox(
                            values = [],
                            expand_x = True,
                            expand_y = True,
                            key = '-LBX-UITGAVEN-',
                            enable_events = True,
                            select_mode = sg.LISTBOX_SELECT_MODE_SINGLE,
                            pad = (15, 15),
                            size = (30, 12)
                        )
                    ]
                ]
            )
        ]
    ]
)

kolomRechts = sg.Column(
    scrollable = False,
    expand_y = True,
    expand_x = True,
    layout = [
        # RIJ R1
        [
            sg.Text(
                text = 'Sorteer op'
            )
        ],
        [
            sg.Radio(
                text = 'Winkel',
                group_id = '-GRP-',
                default = True,
                key = '-RBN-WINKEL-',
                enable_events = True
            ),
            sg.Radio(
                text = 'Bedrag',
                group_id = '-GRP-',
                key = '-RBN-BEDRAG-',
                enable_events = True
            )
        ],
        # RIJ R2
        [
            sg.VPush()
        ],
        # RIJ R3
        [
            sg.Text(
                text = 'Totaal',
                size = (12,1)
            ),
            sg.Text(
                text = '0.00',
                font = ('Calibri', 14, 'bold'),
                justification = 'right',
                key = '-TXT-TOTAAL-',
                size = (10,1)
            )
        ],
        # RIJ R4
        [
            sg.Text(
                text = 'Gemiddelde',
                size = (12,1)
            ),
            sg.Text(
                text = '0.00',
                font = ('Calibri', 14, 'bold'),
                justification = 'right',
                key = '-TXT-GEMIDDELDE-',
                size = (10,1)
            )
        ],
        # RIJ R5
        [
            sg.VPush()
        ],
        # RIJ R6
        [
            sg.Button(
                button_text = 'Nieuw',
                size = (26,2),
                key = '-BTN-NIEUW-'
            )
        ],
        # RIJ R7
        [
            sg.Button(
                button_text = 'Afsluiten',
                size = (26,2),
                key = '-BTN-AFSLUITEN-'
            )
        ]
    ]
)


def appLayout():
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
            kolomLinks,
            sg.VerticalSeparator(
                pad = (20, 0)
            ),
            kolomRechts
        ]
    ]