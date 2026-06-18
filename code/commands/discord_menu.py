import os
import time
import requests
import random
import string
import base64
from colorama import Fore
from darkweb import links
from code.discordchecker import main as discord_checker
from code.rpc import rpc_conf
from code.tokencheck import tokenchecker
from code.commands.utils import show_informations


def run_discord():
    while True:
        os.system("cls")
        discord = input(f"""{Fore.MAGENTA}
            ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗
            ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
            ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
            ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
            ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
            ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝
        [I]. Informations

            1. [Nitro Gen]       4. [Token BruteForce]  7. [rpc_conf]
            2. [Spaming Webhook] 5. [Bot to id]         8. [Token check]
            3. [Darkweb]         6. [4c Checker]        9. [Quit]

            Choisis : """).lower()

        if discord == "1":
            os.system("cls")
            nombre = input(f"""{Fore.MAGENTA}
                ███╗   ██╗██╗████████╗██████╗  ██████╗
                ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗
                ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║
                ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║
                ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝
                ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝
                Met le nombre de fois que tu veux essayé : """)
            try:
                nombre = int(nombre)
                for i in range(nombre):
                    char = string.ascii_letters + string.digits
                    result = ''.join(random.choice(char) for _ in range(16))
                    response = requests.get(f"https://discord.gift/{result}")
                    if response.ok:
                        with open("nitro.txt", "a", encoding="utf-8") as fichier:
                            fichier.write(f"https://discord.gift/{result}\n")
            except Exception:
                print("Ca Nas pas marché sorry :)")

        elif discord == "2":
            os.system("cls")
            message = input(f"""{Fore.MAGENTA}
                ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
                ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
                ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝
                ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗
                ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
                ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                Choisis Le message a spam : """)
            os.system("cls")
            url = input(f"""{Fore.MAGENTA}
                ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
                ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
                ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝
                ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗
                ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
                ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                Choisis L'url  : """)
            response = requests.get(url)
            if response.ok:
                try:
                    while True:
                        data = {"content": message}
                        r = requests.post(url, json=data)
                        print(r.status_code, r.text)
                        time.sleep(5)
                except Exception as e:
                    print("Ca nas pas marché", e)
                    time.sleep(5)

        elif discord == "3":
            os.system("cls")
            print(f"""{Fore.MAGENTA}
                ██████╗  █████╗ ██████╗ ██╗  ██╗    ██╗    ██╗███████╗██████╗
                ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██║    ██║██╔════╝██╔══██╗
                ██║  ██║███████║██████╔╝█████╔╝     ██║ █╗ ██║█████╗  ██████╔╝
                ██║  ██║██╔══██║██╔══██╗██╔═██╗     ██║███╗██║██╔══╝  ██╔══██╗
                ██████╔╝██║  ██║██║  ██║██║  ██╗    ╚███╔███╔╝███████╗██████╔╝
                ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚══════╝╚═════╝
                """)
            try:
                for category, content in links.items():
                    print(f"\n--- {category} ---")
                    for name, url in content.items():
                        if isinstance(url, dict):
                            print(f"\n  [{name}]")
                            for sub_name, sub_url in url.items():
                                print(f"   - {sub_name} : {sub_url}")
                        else:
                            print(f"  - {name} : {url}")
            except Exception as e:
                print(f"Error {e}")
            time.sleep(10)

        elif discord == "4":
            os.system("cls")
            user_id = input(f"""{Fore.MAGENTA}
                ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
                ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
                   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
                   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
                   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
                   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝

                    Met L'id du gars : """)
            try:
                part1 = base64.b64encode(user_id.encode()).decode()
                part2 = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
                part3 = ''.join(random.choices(string.ascii_letters + string.digits, k=18))
                token = f"{part1}.{part2}.{part3}"
                print(f"\nToken : \n {token}")
                time.sleep(2)
            except Exception:
                print("Ca na pas marché")
                time.sleep(2)

        elif discord == "5":
            os.system("cls")
            id_bot = int(input(f"""{Fore.MAGENTA}
                ██╗███╗   ██╗██╗   ██╗██╗████████╗
                ██║████╗  ██║██║   ██║██║╚══██╔══╝
                ██║██╔██╗ ██║██║   ██║██║   ██║
                ██║██║╚██╗██║╚██╗ ██╔╝██║   ██║
                ██║██║ ╚████║ ╚████╔╝ ██║   ██║
                ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝

                Met L'id de ton bot : """))
            try:
                print(f"https://discord.com/oauth2/authorize?client_id={id_bot}&permissions=8&integration_type=0&scope=bot")
                time.sleep(5)
            except ValueError:
                print("Problème...")
                time.sleep(5)

        elif discord == "6":
            discord_checker()

        elif discord == "7":
            rpc_conf()

        elif discord == "8":
            tokenchecker()

        elif discord == "i":
            show_informations()

        elif discord == "9":
            break
