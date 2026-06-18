import os
import time
import threading
import colorama
from colorama import Fore
from pypresence import Presence
from pyfiglet import Figlet
from code.commands.lookup import run_lookup
from code.commands.security import run_security
from code.commands.discord_menu import run_discord
from code.commands.covid_menu import run_covid

colorama.init(autoreset=True)


def rpc():
    rpc_presence = Presence("1441226984024965221")
    rpc_presence.connect()
    rpc_presence.update(
        state="White Wolf",
        details="Best Tools",
        large_image="tools",
        large_text="by xql",
        buttons=[
            {"label": "Repository", "url": "https://github.com/Python-loving/WHITEWOLF-TOOLS"},
            {"label": "Telegram", "url": "https://t.me/whitewolf_tools"}
        ]
    )
    while True:
        time.sleep(15)


def devtools():
    os.system("cls")
    choix = input(f"""{Fore.MAGENTA}
    ████▄  ██████ ██  ██ ██████ ▄████▄ ▄████▄ ██     ▄█████
    ██  ██ ██▄▄   ██▄▄██   ██   ██  ██ ██  ██ ██     ▀▀▀▄▄▄
    ████▀  ██▄▄▄▄  ▀██▀    ██   ▀████▀ ▀████▀ ██████ █████▀

    Devtools for xql : """)
    f = Figlet(font="slant")
    print(f.renderText(choix))


def show_informations():
    os.system("cls")
    print(f"""{Fore.RED}
 Informations
        Telegram - https://t.me/whitewolf_tools
        Gunslol  - https://guns.lol/xqldev
    """)
    time.sleep(5)


threading.Thread(target=rpc, daemon=True).start()

while True:
    os.system("cls")
    choix = input(f"""{Fore.WHITE}
            ██╗    ██╗██╗  ██╗██╗████████╗███████╗██╗    ██╗ ██████╗ ██╗     ███████╗
            ██║    ██║██║  ██║██║╚══██╔══╝██╔════╝██║    ██║██╔═══██╗██║     ██╔════╝
            ██║ █╗ ██║███████║██║   ██║   █████╗  ██║ █╗ ██║██║   ██║██║     █████╗
            ██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██║███╗██║██║   ██║██║     ██╔══╝
            ╚███╔███╔╝██║  ██║██║   ██║   ███████╗╚███╔███╔╝╚██████╔╝███████╗██║
             ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝
        [I]. Informations

            1. [Lookup]    4. [Covid]
            2. [Sécurity]  5. [Quit]
            3. [Discord]

            Fais ton choix : """).lower()

    if choix == "i":
        show_informations()
    elif choix == "1":
        run_lookup()
    elif choix == "2":
        run_security()
    elif choix == "3":
        run_discord()
    elif choix == "4":
        run_covid()
    elif choix == "5":
        print("Au-Revoir a bientot l'ami")
        time.sleep(2)
        break
