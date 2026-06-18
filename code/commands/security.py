import os
import time
import requests
import tempfile
import subprocess
import msvcrt
import random
import string
import whois as whois_module
from colorama import Fore
from code.genip import ip as genip
from code.Spamtlgrm import tlgrm
from code.passwordmanager import passwdmanage
from code.challange.firstchallange import osint
from code.challange.pentestchallange import main as pentest
from code.webcamcapt import webcam
from code.commands.utils import show_informations


def run_security():
    while True:
        os.system("cls")
        choix3 = input(f"""{Fore.GREEN}
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

        Fais ton choix : """).lower()

        if choix3 == "1":
            os.system("cls")
            vpn = input(f"""{Fore.GREEN}
            ██╗   ██╗██████╗ ███╗   ██╗
            ██║   ██║██╔══██╗████╗  ██║
            ██║   ██║██████╔╝██╔██╗ ██║
            ╚██╗ ██╔╝██╔═══╝ ██║╚██╗██║
             ╚████╔╝ ██║     ██║ ╚████║
              ╚═══╝  ╚═╝     ╚═╝  ╚═══╝

            Choisis Le temps que tu a besoin : """)
            os.system("cls")
            prx = input(f"""{Fore.GREEN}
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
                    r = requests.get("https://api.ipify.org?format=json", proxies=proxies, timeout=5)
                    print("Proxy OK :", r.json())
                except Exception:
                    print("Proxy invalide ou mort")
                    continue

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
                password = input(f"""{Fore.GREEN}
                ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗
                ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
                ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
                ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
                ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
                ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝

                Choisis le nombre de lettres & chiffres : """)
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
                site = input(f"""{Fore.GREEN}
                    ██╗    ██╗███████╗██████╗     ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗
                    ██║    ██║██╔════╝██╔══██╗    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝
                    ██║ █╗ ██║█████╗  ██████╔╝    ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗
                    ██║███╗██║██╔══╝  ██╔══██╗    ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║
                    ╚███╔███╔╝███████╗██████╔╝    ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║
                    ╚══╝╚══╝ ╚══════╝╚═════╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝

                    Choisis l'url du site que tu veux check : """)
                response = requests.get(site)
                if response.ok:
                    print(f"Le site a répondu en : {response.elapsed.total_seconds() * 1000:.2f} ms")
                    time.sleep(3)
                else:
                    print("Le site na pas répondu")
                    time.sleep(3)
            except Exception as e:
                print(f"Error {e}")

        elif choix3 == "4":
            os.system("cls")
            page = input(f"""{Fore.GREEN}
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
                    print("Header du site :\n")
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
            os.system("cls")
            domain_input = input(f"""{Fore.GREEN}
                    ██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗
                    ██║    ██║██║  ██║██╔═══██╗██║██╔════╝
                    ██║ █╗ ██║███████║██║   ██║██║███████╗
                    ██║███╗██║██╔══██║██║   ██║██║╚════██║
                    ╚███╔███╔╝██║  ██║╚██████╔╝██║███████║
                    ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝

                    Met le lien de ton site : """)
            try:
                data = whois_module.whois(domain_input)
                print(f"Domaine : {data.domain_name}")
                print(f"Registrar : {data.registrar}")
                print(f"Création : {data.creation_date}")
                print(f"Expiration : {data.expiration_date}")
                print(f"DNS : {data.name_servers}")
            except Exception as e:
                print(f"Error {e}")

        elif choix3 == "6":
            genip()

        elif choix3 == "7":
            tlgrm()

        elif choix3 == "8":
            passwdmanage()

        elif choix3 == "9":
            osint()

        elif choix3 == "10":
            pentest()

        elif choix3 == "11":
            webcam()

        elif choix3 == "i":
            show_informations()

        elif choix3 == "12":
            break
