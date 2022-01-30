import PySimpleGUI as sg
import random

#theme
sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '#000000',
                                        'TEXT': '#00ffff',
                                        'INPUT': '#00ffff',
                                        'TEXT_INPUT': '#ff0000',
                                        'SCROLL': '#808080',
                                        'BUTTON': ('#00008b', '#00ffff'),
                                        'PROGRESS': ('# D1826B', '# CC8019'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0,
'PROGRESS_DEPTH': 0, }

sg.theme('MyCreatedTheme')


layout = [[sg.Button("Choose Color")]]

# Create the window
window = sg.Window("RGB", layout)

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break

    if event == "Choose Color":
        a=random.randint(1,3)
        if a == 1:
            sg.Window(title="Red", layout=[[
                sg.Image('Red-2.png')
            ]], margins=(90, 90)).read()
        if a == 2:
            sg.Window(title="Green", layout=[[
                sg.Image('Green-2.png')
            ]], margins=(90, 90)).read()
        if a == 3:
            sg.Window(title="Blue", layout=[[
                sg.Image('Blue-2.png')
            ]], margins=(90, 90)).read()

window.close()