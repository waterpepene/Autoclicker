import PySimpleGUI as sg
from functions import *

sg.theme('DarkBlue16')  # Add a touch of color

# All the stuff inside the window.

layout = [
    [
        sg.Text(" " * 10),
        sg.Button('Infinite', key="infClicks", pad=(30, 0), border_width=0,
                  tooltip="The amount of clicks becomes infinite.", font=("Segoe UI", 10)),
        sg.Text(" " * 5),
        sg.Button('', image_data=b64_pin,
                  button_color=(sg.theme_background_color(), sg.theme_background_color()),
                  border_width=0, key='kot', tooltip="Keeps the program in front of all other programs.")
    ],

    [
        sg.Text('Clicks: ', key='clicksText', auto_size_text=True, font=("Segoe UI", 10)),
        sg.InputText(size=(10, 1), default_text="0", font=("Segoe UI", 10), key="__CLICKS__",
                     enable_events=True, tooltip="Enter the amount of clicks here.", justification="center")
    ],

    [
        sg.Text('Interval: ', font=("Segoe UI", 10)),
        sg.InputText(tooltip="Enter the interval in-between clicks here.", default_text="0", size=(10, 20),
                     enable_events=True, font=("Segoe UI", 10), key="__INTERVAL__", justification="center"),
        sg.Text('CPS: ' + str(cps), key='cpstxt', font=("Segoe UI", 10), size=(10, 1))
    ],

    [
        sg.Text('Wait time: ', font=("Segoe UI", 10)),
        sg.InputText(tooltip="Enter the amount of time to wait before the clicks start.", default_text="1",
                     size=(10, 20), font=("Segoe UI", 10), key="__WAIT-TIME__", enable_events=True, justification="center")
    ],

    [
        sg.Button('Start', key="acStart", border_width=0, tooltip="Start the auto clicker", font=("Segoe UI", 10)),
        sg.Button('Clear', key='Clear', border_width=0, tooltip="Clear all the input fields", font=("Segoe UI", 10))
    ]
]

# Create the Window
window = sg.Window('Autoclicker',
                   layout,
                   border_depth=5,
                   keep_on_top=True,
                   alpha_channel=0.8,
                   size=(260, 180),
                   icon=b64icon)
