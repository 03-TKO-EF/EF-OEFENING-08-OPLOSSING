import FreeSimpleGUI as sg

fntStandaard = ('Calibri', 14)
fntKop = ('Calibri', 24, 'bold')

def vensterKop():
    return [
        sg.Push(),
        sg.Image(
            source = 'assets/logo.png'
        ),
        sg.Text(
            text = 'UITGAVEN BOODSCHAPPEN',
            font = fntKop
        ),
        sg.Push()
    ]

sg.theme('DefaultNoMoreNagging')

sg.set_options(
    icon = 'assets/favicon.ico',
    font = fntStandaard
)