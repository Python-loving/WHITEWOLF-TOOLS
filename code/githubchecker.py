import random
import os
import string
import requests
from code.colors import *
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def git():
       
        os.system("cls")
        main = int(input(f"""{BLUE}
             ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
            ██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
            ██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
            ██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
            ╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
             ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝      ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
            
            Met le nombre d'essaye a fair : """))
        os.system("cls")
        wbk = input(f"""
             ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
            ██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
            ██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
            ██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
            ╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
             ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝      ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
            
            Met ton webhook discord : """)
        
        try:
            if main >= 10:
                for i in range(main):
                    try:
                        pseudo = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
                        url = f"https://api.github.com/users/{pseudo}"
                        response = requests.get(url, headers=HEADERS, timeout=10)

                        if response.status_code == 404:
                            print(f"{GREEN}Pseudo disponible : {pseudo}{RESET}")
                            data = {
                            "content": pseudo, 
                            "username": "WhiteWolf", 
                            "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
                            }

                            requests.post(wbk, json=data)
                        elif response.status_code == 200:
                            print("Le pseudo est deja pris", pseudo)
                        else:
                            print(f"Erreur GitHub ({response.status_code})", pseudo)
                    except Exception as e:
                        print(f"Error {e}")
        except Exception as e:
            print(f"Error {e}")

if __name__ == "__main__": # ANCHOR -Retenir if __name__ == "__main__" le name de la function pour que ca le lance que quand sais lancé par le main :)
    git()