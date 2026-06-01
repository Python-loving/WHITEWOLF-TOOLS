import os
import time
import requests
import webbrowser
from api import api_ip, api_number, api_dns

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
        choix2 = input("""
                            ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
                            ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
                            ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
                            ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
                            ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
                            ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                                        

            1. [IP]          4. [Google]
            2. [Number]      5. [Dns]
            3. [Username]    6. [Retour Menu]
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
            sites = {
                "GitHub": "https://github.com/{}",
                "Reddit": "https://reddit.com/user/{}",
                "TikTok": "https://www.tiktok.com/@{}",
                "Instagram": "https://www.instagram.com/{}/",
                "X": "https://x.com/{}",
                "Facebook": "https://www.facebook.com/{}",
                "Pinterest": "https://www.pinterest.com/{}/",
                "Twitch": "https://www.twitch.tv/{}",
                "Steam": "https://steamcommunity.com/id/{}",
                "GitLab": "https://gitlab.com/{}",
                "Bitbucket": "https://bitbucket.org/{}",
                "SoundCloud": "https://soundcloud.com/{}",
                "Vimeo": "https://vimeo.com/{}",
                "DeviantArt": "https://www.deviantart.com/{}",
                "Medium": "https://medium.com/@{}",
                "Patreon": "https://www.patreon.com/{}",
                "Roblox": "https://www.roblox.com/user.aspx?username={}",
                "Kik": "https://kik.me/{}",
                "Pastebin": "https://pastebin.com/u/{}",
                "Replit": "https://replit.com/@{}",
                "DockerHub": "https://hub.docker.com/u/{}",
                "Keybase": "https://keybase.io/{}",
                "Codecademy": "https://www.codecademy.com/profiles/{}",
                "TradingView": "https://www.tradingview.com/u/{}",
                "Chess.com": "https://www.chess.com/member/{}",
                "Lichess": "https://lichess.org/@/{}",
                "BuyMeACoffee": "https://www.buymeacoffee.com/{}",
                "Linktree": "https://linktr.ee/{}",
                "AboutMe": "https://about.me/{}",
                "Gravatar": "https://gravatar.com/{}",
            }
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
        elif choix2 == "6":
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