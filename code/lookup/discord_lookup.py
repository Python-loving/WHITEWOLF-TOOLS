import os
import time
import requests


def discord_lookup():
    os.system("cls")
    lookup = input(f"""
                        ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗
                        ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
                        ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
                        ██║   ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
                        ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
                        ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝

                        Choisis L'id Du gars que tu veux lookup : """)

    url = f"https://api.vaultcord.com/webhooks/public-lookup/{lookup}"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.ok:
            try:
                data = response.json()
                print(f"Id : {data.get('id')}")
                print(f"Username : {data.get('username')}")
                print(f"Avatar : {data.get('avatar')}")
                print(f"Discriminator : {data.get('discriminator')}")
                print(f"Public flags : {data.get('public_flags')}")
                print(f"Flags : {data.get('flags')}")
                print(f"Global name : {data.get('global_name')}")
                time.sleep(7)
            except ValueError:
                print("La réponse n'est pas au format JSON :")
                print(response.text)
                time.sleep(3)
        else:
            print(f"Erreur HTTP {response.status_code}")
            print(response.text)
            time.sleep(3)
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")
