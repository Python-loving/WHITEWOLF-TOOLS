import os
import requests


def username_lookup(sites_dict):
    os.system("cls")
    username = input("""
            ██╗   ██╗███████╗███████╗██████╗ ███╗   ██╗ █████╗ ███╗   ███╗███████╗
            ██║   ██║██╔════╝██╔════╝██╔══██╗████╗  ██║██╔══██╗████╗ ████║██╔════╝
            ██║   ██║███████╗█████╗  ██████╔╝██╔██╗ ██║███████║██╔████╔██║█████╗
            ██║   ██║╚════██║██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝
            ╚██████╔╝███████║███████╗██║  ██║██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
             ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

            Choisis le username a lookup : """)
    try:
        for site, url in sites_dict.items():
            full_url = url.format(username)
            r = requests.get(full_url)
            if r.status_code == 200:
                print(f"Trouvé sur {site} : {full_url}")
            else:
                print(f"Rien Trouvé sur {site}")
    except Exception as e:
        print(f"Error {e}")
