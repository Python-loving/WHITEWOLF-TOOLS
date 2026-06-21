import os
import requests
import time
from sites import sites

def fulluser_name():
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

if __name__ == "__main__":
    fulluser_name()