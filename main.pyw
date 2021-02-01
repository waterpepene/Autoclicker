from functions import *
from windowGui import *
import threading

while True:
    event, values = window.read(timeout=1000)

    if event in (None, "kot"):
        if kot1or0 == 1:                # on/off button to keep the autoclicker on top
            kot1or0 = 0
            window.TKroot.wm_attributes("-topmost", kot1or0)
        elif kot1or0 == 0:
            kot1or0 = 1
            window.TKroot.wm_attributes("-topmost", kot1or0)

    try:
        window['cpstxt'].update("CPS:" + str(round(60 / float(values["__INTERVAL__"]))))
        # pass because it sends those exceptions as soon as the . is written
    except (ZeroDivisionError, ValueError):
        pass

    if event in (None, "infClicks") and not infclicks:
        window["__CLICKS__"].update("∞")
        infclicks, event = True, ""

    if event in (None, "infClicks") and infclicks:
        infclicks, event = False, ""

    if event in (None, "acStart") and infclicks:
        threading.Thread(target=infiniteClicks, args=(values["__INTERVAL__"], values["__WAIT-TIME__"]), daemon=True).start()
    # starting new threads so that the auto clicker doesn't crash
    if event in (None, "acStart") and not infclicks:
        threading.Thread(target=clicks, args=(values["__CLICKS__"], values["__INTERVAL__"], values["__WAIT-TIME__"]),
                         daemon=True).start()

    if event == sg.WIN_CLOSED:  # break out of the loop if user closes window
        break

    if event in (None, "Clear"):
        window['cpstxt'].update("CPS: 0")
        updateValues(("__INTERVAL__", 0), ("__CLICKS__", 0), ("__WAIT-TIME__", 1), window_name=window)

    deleteLetters(window, values, infclicks, "__INTERVAL__", "__CLICKS__", "__WAIT-TIME__")

    keepFirstChar(window, values, ("__INTERVAL__", 0), ("__CLICKS__", 0), ("__WAIT-TIME__", 1), inf_on=infclicks)