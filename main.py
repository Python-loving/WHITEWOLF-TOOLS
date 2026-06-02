import os
import time
import requests
import webbrowser
import json
from api import api_ip, api_number, api_dns
from sites import sites

# FIXME - Add Gestions Error i d'ont have time sry ;p


while True:
    os.system("cls")
    choix = input(f"""
            ██╗    ██╗██╗  ██╗██╗████████╗███████╗██╗    ██╗ ██████╗ ██╗     ███████╗
            ██║    ██║██║  ██║██║╚══██╔══╝██╔════╝██║    ██║██╔═══██╗██║     ██╔════╝
            ██║ █╗ ██║███████║██║   ██║   █████╗  ██║ █╗ ██║██║   ██║██║     █████╗  
            ██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██║███╗██║██║   ██║██║     ██╔══╝  
            ╚███╔███╔╝██║  ██║██║   ██║   ███████╗╚███╔███╔╝╚██████╔╝███████╗██║     
            ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝     

            1. [Lookup]
            2. [Quit]

            Fais ton choix : """)
        
    if  choix == "1":
        os.system("cls")
        choix2 = input(f"""
                            ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
                            ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
                            ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
                            ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
                            ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
                            ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                                        

                            1. [IP]          4. [Google]      7. [Github]
                            2. [Number]      5. [Dns]         8. [Leak Mail]
                            3. [Username]    6. [DISCORD]     9. [Quit]
                            
                            Fais ton choix : """)
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
            for site, url in sites.items():
                full_url = url.format(username)
                r = requests.get(full_url)
                if r.status_code == 200:
                    print(f"Trouvé sur {site} : {full_url}")
                else:
                    print(f"Rien Trouvé sur {site}")
        elif choix2 == "4":
            search_google = input("""
                 ██████╗  ██████╗  ██████╗  ██████╗ ██╗     ███████╗    ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
                ██╔════╝ ██╔═══██╗██╔═══██╗██╔════╝ ██║     ██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
                ██║  ███╗██║   ██║██║   ██║██║  ███╗██║     █████╗      ███████╗█████╗  ███████║██████╔╝██║     ███████║
                ██║   ██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝      ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
                ╚██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗    ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
                 ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                     
                Fais ta recherche google : """)
            query = f"{search_google}"
            url = "https://www.google.com/search?q=" + query

            webbrowser.open(url)
        # on definie le lookup des dns
        elif choix2 == "5":
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
        # Ici on crée le DISCORD LOOKUP
        # Help ai for lookup :)
        elif choix2 == "6":
            lookup = input("""
                        ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
                        ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
                        ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
                        ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
                        ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
                        ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                        
                        Choisis L'id Du gars que tu veux lookup : """)

            url = f"https://api.vaultcord.com/webhooks/public-self/{lookup}"

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

                        clan = data.get("clan", {})
                        print(f"Guild ID : {clan.get('identity_guild_id')}")
                        print(f"Tag : {clan.get('tag')}")

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
            ██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝
            ██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗
            ╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝
             ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
                Le nom du repo : """)

            url = f"https://api.github.com/repos/{username}/{nom_repo}/commits?per_page=1"
            response = requests.get(url)
            data = response.json()

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
            url = f"https://leakcheck.io/api/public?check={choix_mail}" # ANCHOR - utilisé fstring Javais oubliez... A retenir 
            response = requests.get(url)
            data = response.json()
            if response.ok:
                print("Tout les données sont dasn result.json") # ANCHOR - ajouts a des fichier en type json a retenir pas fais souvent...
                time.sleep(5)
                with open("result.json", "w", encoding="utf-8") as fichier:
                    json.dump(data, fichier, ensure_ascii=False, indent=4)
            else:
                print("Aucun Resultas ou bug", response.status_codes)
                time.sleep(5)

            
        elif choix2 == "9":
            print("Tu va quitté le tools")
            time.sleep(2)
            print("Au-Revoir :)")
            time.sleep(2)
            break
            
    # Ici on a mis le quit si la personne a lancé sans fair expres
    elif choix == "2":
        print("Au-Revoir a bientot l'amis")
        time.sleep(2)
        break
