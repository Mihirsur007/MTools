#import modules
import requests
import PySimpleGUI as sg
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)

    return r.text
#theme
# Add your new theme colors and settings
sg.LOOK_AND_FEEL_TABLE['M'] = {'BACKGROUND': '#264653',
                                        'TEXT': '#E9C46A',
                                        'INPUT': '#E76F51',
                                        'TEXT_INPUT': '#E9C46A',
                                        'SCROLL': '#99CC99',
                                        'BUTTON': ('#000000', '#2A9D8F'),
                                        'PROGRESS': ('#D1826B', '#CC8019'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0,
'PROGRESS_DEPTH': 0, }

sg.theme('M')

# Very basic window.
# Return values using
# automatic-numbered keys
layout = [
    [sg.Text('Please enter Image Name')],
    [sg.Text('Image', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Web Scraper', layout)
event, values = window.read()
window.close()
# The input data looks like a simple list
# when automatic numbered
print("Word Searched")
print(values[0])




var = values[0]

htmldata = getdata("https://unsplash.com/s/photos/" + var)

soup = BeautifulSoup(htmldata, 'html.parser')

for item in soup.find_all('img'):
    print(item['src'])

print('\n')
print('Made By: Mihir S.')
print('\n')
print('\n')
#############


layout = [[sg.Text('Check your terminal for all the links found on this web page')], [sg.Button("EXIT")]]

# Create the window
window = sg.Window("Output", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break

window.close()

