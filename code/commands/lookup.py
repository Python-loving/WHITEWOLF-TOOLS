import os
import time
import requests
import webbrowser
import json
from colorama import Fore
from api import api_ip, api_number, api_dns
from sites import sites as site_list
from code.tiktokchecker import tiktok
from code.githubchecker import git
from code.discordchecker import main as discord_checker
from code.ipscanner import ip as ipscanner
from code.letsenscript import domaine
from code.robloxsearch import roblox
from code.ai import ai
from code.checking import holehe
from code.commands.utils import show_informations


def run_lookup():
    while True:
        os.system("cls")
        choix2 = input(f"""{Fore.CYAN}
                            ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗
                            ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
                            ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
                            ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝
                            ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║
                            ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝
                    [I]. Informations

                            1. [IP]          4. [Google]      7. [Github]      10. [4C Tiktok]  13. [IP Scanner]   16. [AI]
                            2. [Number]      5. [Dns]         8. [Leak Mail]   11. [4C Github]  14. [SSL / TLS]    17. [Holehe]
                            3. [Username]    6. [DISCORD]     9. [Archive Web] 12. [Github]     15. [Roblox]       18. [Quit]

                            Fais ton choix : """).lower()

        if choix2 == "1":
            os.system("cls")
            choixip = input(f"""{Fore.CYAN}
                    ██╗██████╗
                    ██║██╔══██╗
                    ██║██████╔╝
                    ██║██╔═══╝
                    ██║██║
                    ╚═╝╚═╝

        Choisis L'ip Que tu veux lookup : """)
            try:
                myreq = requests.get(
                    f"https://geo.ipify.org/api/v2/country,city,vpn?apiKey={api_ip}&ipAddress={choixip}"
                )
                data = myreq.json()
                print(f"IP: {data['ip']}")
                print(f"Pays: {data['location']['country']}")
                print(f"Ville: {data['location']['city']}")
                print(f"ISP: {data['isp']}")
                time.sleep(2)
                print("Vous allez ètre ramener a l'accueil")
                time.sleep(2)
            except Exception as e:
                print(f"Error {e}")

        elif choix2 == "2":
            os.system("cls")
            choixnumber = input(f"""{Fore.CYAN}
            ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗
            ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
            ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
            ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
            ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
            ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

        Choisis Le numéro de téléphone que tu veux lookup : """)
            try:
                myreq2 = requests.get(
                    f"http://apilayer.net/api/validate?access_key={api_number}&number={choixnumber}"
                )
                data2 = myreq2.json()
                print(f"Country: {data2['country_name']}")
                print(f"Format: {data2['local_format']}")
                print(f"international_format: {data2['international_format']}")
                print(f"Carrier: {data2['carrier']}")
                time.sleep(2)
                print("")
                print("Retour A l'accueil dans 2s")
                time.sleep(2)
            except Exception as e:
                print(f"Error {e}")

        elif choix2 == "3":
            os.system("cls")
            username = input(f"""{Fore.CYAN}
            ██╗   ██╗███████╗███████╗██████╗ ███╗   ██╗ █████╗ ███╗   ███╗███████╗
            ██║   ██║██╔════╝██╔════╝██╔══██╗████╗  ██║██╔══██╗████╗ ████║██╔════╝
            ██║   ██║███████╗█████╗  ██████╔╝██╔██╗ ██║███████║██╔████╔██║█████╗
            ██║   ██║╚════██║██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝
            ╚██████╔╝███████║███████╗██║  ██║██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
             ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

            Choisis le username a lookup : """)
            try:
                for site, url in site_list.items():
                    full_url = url.format(username)
                    r = requests.get(full_url, timeout=5)
                    if r.status_code == 200:
                        print(f"Trouvé sur {site} : {full_url}")
                    else:
                        print(f"Rien Trouvé sur {site}")
            except Exception as e:
                print(f"Error {e}")

        elif choix2 == "4":
            os.system("cls")
            search_google = input(f"""{Fore.CYAN}
                 ██████╗  ██████╗  ██████╗  ██████╗ ██╗     ███████╗    ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
                ██╔════╝ ██╔═══██╗██╔═══██╗██╔════╝ ██║     ██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
                ██║  ███╗██║   ██║██║   ██║██║  ███╗██║     █████╗      ███████╗█████╗  ███████║██████╔╝██║     ███████║
                ██║   ██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝      ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
                ╚██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗    ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
                 ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

                Fais ta recherche google : """)
            try:
                url = "https://www.google.com/search?q=" + search_google
                webbrowser.open(url)
            except Exception as e:
                print(f"Error {e}")

        elif choix2 == "5":
            os.system("cls")
            dns = input(f"""{Fore.CYAN}
                ██████╗ ███╗   ██╗███████╗    ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗
                ██╔══██╗████╗  ██║██╔════╝    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
                ██║  ██║██╔██╗ ██║███████╗    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
                ██║  ██║██║╚██╗██║╚════██║    ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝
                ██████╔╝██║ ╚████║███████║    ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║
                ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝
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
                    print("Tu vas ètre renvoyer a l'accueil dans 2s")
                    time.sleep(2)
                else:
                    print(f"Error: {response.status_code}, {response.text}")
                    time.sleep(2)
            except Exception as e:
                print(f"Error {e}")

        elif choix2 == "6":
            os.system("cls")
            lookup = input(f"""{Fore.CYAN}
                        ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗
                        ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
                        ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
                        ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
                        ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
                        ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝

                        Choisis L'id Du gars que tu veux lookup : """)
            url = f"https://api.vaultcord.com/webhooks/public-lookup/{lookup}"
            try:
                headers = {"User-Agent": "Mozilla/5.0"}
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

        elif choix2 == "7":
            os.system("cls")
            username = input(f"""{Fore.CYAN}
             ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗
            ██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗
            ██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝
            ██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗
            ╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝
             ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝
                Le Username github : """)
            os.system("cls")
            nom_repo = input(f"""{Fore.CYAN}
             ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗
            ██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗
            ██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝
            ██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗
            ╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝
             ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝
                Le nom du repo : """)
            url = f"https://api.github.com/repos/{username}/{nom_repo}/commits?per_page=1"
            response = requests.get(url)
            data = response.json()
            try:
                if response.ok:
                    commit_data = data[0]
                    print(f"Email : {commit_data['commit']['author']['email']}")
                    print(f"Name  : {commit_data['commit']['author']['name']}")
                    print(f"date  : {commit_data['commit']['author']['date']}")
                    print(f"Msg   : {commit_data['commit']['message']}")
                    print(f"url   : {commit_data['html_url']}")
                    print(f"sign  : {commit_data['commit']['verification']['signature']}")
                    print(f"id    : {commit_data['sha']}")
                    print(f"PDP   : {commit_data['author']['avatar_url']}")
                    print(f"ABO   : {commit_data['author']['followers_url']}")
                    print(f"Node  : {commit_data['node_id']}")
                    time.sleep(5)
                else:
                    print(response.status_code)
                    time.sleep(5)
            except Exception as e:
                print(f"Error {e}")

        elif choix2 == "8":
            os.system("cls")
            choix_mail = input(f"""{Fore.CYAN}
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
                    print("Tout les données sont dans result.json")
                    with open("result.json", "w", encoding="utf-8") as fichier:
                        json.dump(data, fichier, ensure_ascii=False, indent=4)
                    time.sleep(5)
                else:
                    print("Aucun Resultat ou bug", response.status_code)
                    time.sleep(5)
            except Exception as e:
                print(f"Error {e}")

        elif choix2 == "9":
            os.system("cls")
            choix_url = input(f"""{Fore.CYAN}
                     █████╗ ██████╗  ██████╗██╗  ██╗██╗██╗   ██╗███████╗
                    ██╔══██╗██╔══██╗██╔════╝██║  ██║██║██║   ██║██╔════╝
                    ███████║██████╔╝██║     ███████║██║██║   ██║█████╗
                    ██╔══██║██╔══██╗██║     ██╔══██║██║╚██╗ ██╔╝██╔══╝
                    ██║  ██║██║  ██║╚██████╗██║  ██║██║ ╚████╔╝ ███████╗
                    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝

                    Met le lien de ton site : """)
            try:
                api_url = f"https://archive.org/wayback/available?url={choix_url}"
                response = requests.get(api_url)
                data = response.json()
                if response.ok:
                    print(f"Status : {data['archived_snapshots']['closest']['status']}")
                    print(f"Disponible : {data['archived_snapshots']['closest']['available']}")
                    print(f"Archive : {data['archived_snapshots']['closest']['url']}")
                    print(f"Timestamp : {data['archived_snapshots']['closest']['timestamp']}")
                    time.sleep(5)
                else:
                    print("Une erreur est survenue")
                    time.sleep(3)
            except Exception as e:
                print(f"Error {e}")
                time.sleep(3)

        elif choix2 == "10":
            tiktok()

        elif choix2 == "11":
            git()

        elif choix2 == "12":
            discord_checker()

        elif choix2 == "13":
            ipscanner()

        elif choix2 == "14":
            domaine()

        elif choix2 == "15":
            roblox()

        elif choix2 == "16":
            ai()

        elif choix2 == "17":
            holehe()

        elif choix2 == "i":
            show_informations()

        elif choix2 == "18":
            break
