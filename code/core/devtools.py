import os
from pyfiglet import Figlet
from code.colors import MAGENTA


def devtools():
    os.system("cls")
    choix = input(f"""{MAGENTA}
    ████▄  ██████ ██  ██ ██████ ▄████▄ ▄████▄ ██     ▄█████
    ██  ██ ██▄▄   ██▄▄██   ██   ██  ██ ██  ██ ██     ▀▀▀▄▄▄
    ████▀  ██▄▄▄▄  ▀██▀    ██   ▀████▀ ▀████▀ ██████ █████▀

    Devtools for xql : """)
    f = Figlet(font="slant")
    print(f.renderText(choix))
