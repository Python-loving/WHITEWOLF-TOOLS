import time
import os
import requests
from api import api_ip

def ipchoix():
    os.system("cls")
    choixip = input("""
            ██╗██████╗ 
            ██║██╔══██╗
            ██║██████╔╝
            ██║██╔═══╝ 
            ██║██║     
            ╚═╝╚═╝     

Choisis L'ip Que tu veux lookup : """)
    try:
        myreq = requests.get(f"https://geo.ipify.org/api/v2/country,city,vpn?apiKey={api_ip}&ipAddress={choixip}")
        data = myreq.json()
        print(f"IP: {data['ip']}")
        print(f"Pays: {data['location']['country']}")
        print(f"Ville: {data['location']['city']}")
        print(f"ISP: {data['isp']}")
        time.sleep(2)
        print("Vous allez ètre ramener a l'accueil")
        time.sleep(2)
        os.system("cls")
    except Exception as e:
        print(f"Error {e}")