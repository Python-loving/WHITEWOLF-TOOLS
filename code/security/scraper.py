import os
import time
import requests


def http_scraper():
    os.system("cls")
    page = input("""
                ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗
                ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
                ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
                ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
                ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
                ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝

                Met le lien du site : """)

    response = requests.head(page)
    try:
        if response.ok:
            print("header du site :\n")
            with open("result.txt", "w", encoding="utf-8") as fichier:
                for key, value in response.headers.items():
                    print(f"{key} : {value}")
                    fichier.write(f"{key}, ; {value}\n")
            time.sleep(5)
        else:
            print("Ca marche pas")
    except ValueError:
        print("Error input")
