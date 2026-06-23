import os
import time
from code.colors import *
import requests

def ip_reputation():
    os.system("cls")
    ip = input(f"""
    ██ █████▄   █████▄  ██████ █████▄ ██  ██ ██████ ▄████▄ ██████ ██ ▄████▄ ███  ██ 
    ██ ██▄▄█▀   ██▄▄██▄ ██▄▄   ██▄▄█▀ ██  ██   ██   ██▄▄██   ██   ██ ██  ██ ██ ▀▄██ 
    ██ ██       ██   ██ ██▄▄▄▄ ██     ▀████▀   ██   ██  ██   ██   ██ ▀████▀ ██   ██ 
                                                                                
    Met l'ip a vérifié : """)

    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,city,isp,org,as,proxy,hosting"

    response = requests.get(url)

    if response.status_code == 200:
        try:
            os.system("cls")
            data = response.json()
            print(f"{MAGENTA}")
            os.system("cls")
            print(f"""
            IP Lookup Result :
            Pays : {data['country']} ({data['countryCode']})
            Ville : {data['city']}
            ISP : {data['isp']}
            Org : {data['org']}
            AS : {data['as']}
            Proxy : {data['proxy']}
            Hosting : {data['hosting']}
            """)
            time.sleep(5)
        except Exception as e:
            print(f"Error {e}")
    else:
        print(f"Error", response.status_code)
        os.system("cls")

if __name__ == "__main__":
    ip_reputation()