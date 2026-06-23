import os
import json
import time
import requests


def leak_check():
    os.system("cls")
    choix_mail = input("""
                ██╗     ███████╗ █████╗ ██╗  ██╗
                ██║     ██╔════╝██╔══██╗██║ ██╔╝
                ██║     █████╗  ███████║█████╔╝
                ██║     ██╔══╝  ██╔══██║██╔═██╗
                ███████╗███████╗██║  ██║██║  ██╗
                ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                Choisis Le mail que tu veux verifié : """)
    url = f"https://leakcheck.io/api/public?check={choix_mail}"
    response = requests.get(url)
    data = response.json()
    try:
        if response.ok:
            print("Tout les données sont dasn result.json")
            time.sleep(5)
            with open("result.json", "w", encoding="utf-8") as fichier:
                json.dump(data, fichier, ensure_ascii=False, indent=4)
        else:
            print("Aucun Resultas ou bug", response.status_codes)
            time.sleep(5)
    except Exception as e:
        print(f"Error {e}")
