import os
import time
import requests
from api import api_dns


def dns_lookup():
    os.system("cls")
    dns = input("""
                ██████╗ ███╗   ██╗███████╗    ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗
                ██╔══██╗████╗  ██║██╔════╝    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
                ██║  ██║██╔██╗ ██║███████╗    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
                ██║   ██║██║╚██╗██║╚════██║    ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝
                ██████╔╝██║ ╚████║███████║    ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║
                ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝
                Choisis l'url du site que tu veux lookup : """)
    api = f"https://api.viewdns.info/abuselookup/?domain={dns}&apikey={api_dns}&output=json"
    response = requests.get(api)
    data = response.json()
    try:
        if response.ok:
            print(f"Tool : {data['query']['tool']}")
            print(f"Domaine : {data['query']['domain']}")
            print(f"Abuse contact : {data['response']['abusecontact']}")
            time.sleep(2)
            print("")
            print("Tu va ètre renvoyer a l'acueil dans 2s")
            time.sleep(2)
        else:
            print(f"Error: {response.status_code}, {response.text}")
            time.sleep(2)
            print("Tu va ètre renvoyer a l'acueil dans 2s")
            time.sleep(2)
    except Exception as e:
        print(f"Error {e}")
