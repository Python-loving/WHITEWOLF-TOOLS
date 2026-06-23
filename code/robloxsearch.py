import os
import requests
import time
from colorama import Fore, Back, Style
import questionary
from code.colors import *

def roblox():
    os.system("cls")
    choix = questionary.select(
        "Choisis",
        [
            "Roblox Lookup",
            "Quit"
        ]
    ).ask()

    if choix == "Roblox Lookup":
        try:
            os.system("cls")
            roblox_lookup = input(f"""{RED}
                ██████╗  ██████╗ ██████╗ ██╗      ██████╗ ██╗  ██╗
                ██╔══██╗██╔═══██╗██╔══██╗██║     ██╔═══██╗╚██╗██╔╝
                ██████╔╝██║   ██║██████╔╝██║     ██║   ██║ ╚███╔╝ 
                ██╔══██╗██║   ██║██╔══██╗██║     ██║   ██║ ██╔██╗ 
                ██║  ██║╚██████╔╝██████╔╝███████╗╚██████╔╝██╔╝ ██╗
                ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝
                
                Met l'id de la personne roblox : """)
        except ValueError as e:
            print(f"Error {e}")

        try:
            url = f"https://users.roblox.com/v1/users/{roblox_lookup}"
            data = requests.get(url).json()

            if data:
                print("Pseudo utilisateur :", data["name"])
                print("Pseudo Affichage :", data["displayName"])
                print("Description :", data["description"])
                print("Crée Quand :", data["created"])
                print("Banni Oui ou Non :", data["isBanned"])
                print("Vérfié Oui ou Non :", data["hasVerifiedBadge"])
            else:
                print("Ca n'as pas marché")

        except Exception as e:
            print(f"Error {e}")
                
    if choix == "Quit":
        print("Au-Revoir")
        time.sleep(2)
        
if __name__ == "__main__":
    roblox()