import os
import time
import requests
from code.colors import YELLOW


def archive_check():
    os.system("cls")
    choix_url = input(f""" {YELLOW}
                     █████╗ ██████╗  ██████╗██╗  ██╗██╗██╗   ██╗███████╗
                    ██╔══██╗██╔══██╗██╔════╝██║  ██║██║██║   ██║██╔════╝
                    ███████║██████╔╝██║     ███████║██║██║   ██║█████╗
                    ██╔══██║██╔══██╗██║     ██╔══██║██║╚██╗ ██╔╝██╔══╝
                    ██║  ██║██║  ██║╚██████╗██║  ██║██║ ╚████╔╝ ███████╗
                    ╚═╝  ╚═╝╚═╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝

                    Met le lien de ton site : """)
    try:
        url_du_site = choix_url
        api_url = f"https://archive.org/wayback/available?url={url_du_site}"
        response = requests.get(api_url)
        data = response.json()
        if response.ok:
            print(f"Status : {data['archived_snapshots']['closest']['status']}")
            print(f"Disponible : {data['archived_snapshots']['closest']['available']}")
            print(f"Archive : {data['archived_snapshots']['closest']['url']}")
            print(f"Timestamp : {data['archived_snapshots']['closest']['timestamp']}")
            time.sleep(5)
        else:
            print("Une erreur et survenue")
            time.sleep(3)
    except Exception as e:
        print(f"Error {e}")
        time.sleep(3)
