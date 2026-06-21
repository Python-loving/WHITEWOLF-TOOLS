import os
import requests
import subprocess
import tempfile
import time
import msvcrt


def vpn():
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

if __name__ == "__main__":
    vpn()