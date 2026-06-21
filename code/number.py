import time
import os
import requests
from api import api_number

def numberchoix():
    os.system("cls")
    choixnumber = input("""
    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
    ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
    ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

Choisis Le numéro de téléphone que tu veux lookup : """)
    try:
        myreq2 = requests.get(f"http://apilayer.net/api/validate?access_key={api_number}&number={choixnumber}")
        data2 = myreq2.json()
        print(f"Country: {data2['country_name']}")
        print(f"Format: {data2['local_format']}")
        print(f"international_format: {data2['international_format']}")
        print(f"Carrier: {data2['carrier']}")
        time.sleep(2)
        print("")
        print("Retour A l'accueil dnas 2s")
        time.sleep(2)
    except Exception as e:
        print(f"Error {e}")

if __name__ == "__main__":
    numberchoix()