import random
import os
import string
import requests
from code.colors import *

def main():
       

        os.system("cls")
        quatre_lettre = input(f""" {GREEN}
           
            ▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄     ██▓███    ██████ ▓█████  █    ██ ▓█████▄  ▒█████  
            ▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌   ▓██░  ██▒▒██    ▒ ▓█   ▀  ██  ▓██▒▒██▀ ██▌▒██▒  ██▒
            ░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ▓██░ ██▓▒░ ▓██▄   ▒███   ▓██  ▒██░░██   █▌▒██░  ██▒
            ░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ▒██▄█▓▒ ▒  ▒   ██▒▒▓█  ▄ ▓▓█  ░██░░▓█▄   ▌▒██   ██░
            ░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓    ▒██▒ ░  ░▒██████▒▒░▒████▒▒▒█████▓ ░▒████▓ ░ ████▓▒░
            ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒    ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░░░ ▒░ ░░▒▓▒ ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ 
            ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒    ░▒ ░     ░ ░▒  ░ ░ ░ ░  ░░░▒░ ░ ░  ░ ▒  ▒   ░ ▒ ▒░ 
            ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░    ░░       ░  ░  ░     ░    ░░░ ░ ░  ░ ░  ░ ░ ░ ░ ▒  
            ░     ░        ░  ░ ░          ░ ░     ░        ░                      ░     ░  ░   ░        ░        ░ ░  
            ░                   ░                           ░                                            ░               
        
            Met le nombre de pseudo que tu veux trouvé : """)
        os.system("cls")
        webhook = input(f""" {BLUE}
           
            ▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄     ██▓███    ██████ ▓█████  █    ██ ▓█████▄  ▒█████  
            ▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌   ▓██░  ██▒▒██    ▒ ▓█   ▀  ██  ▓██▒▒██▀ ██▌▒██▒  ██▒
            ░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ▓██░ ██▓▒░ ▓██▄   ▒███   ▓██  ▒██░░██   █▌▒██░  ██▒
            ░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ▒██▄█▓▒ ▒  ▒   ██▒▒▓█  ▄ ▓▓█  ░██░░▓█▄   ▌▒██   ██░
            ░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓    ▒██▒ ░  ░▒██████▒▒░▒████▒▒▒█████▓ ░▒████▓ ░ ████▓▒░
            ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒    ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░░░ ▒░ ░░▒▓▒ ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ 
            ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒    ░▒ ░     ░ ░▒  ░ ░ ░ ░  ░░░▒░ ░ ░  ░ ▒  ▒   ░ ▒ ▒░ 
            ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░    ░░       ░  ░  ░     ░    ░░░ ░ ░  ░ ░  ░ ░ ░ ░ ▒  
            ░     ░        ░  ░ ░          ░ ░     ░        ░                      ░     ░  ░   ░        ░        ░ ░  
            ░                   ░                           ░                                            ░               
        
            Met le Webhook ou ca envoie : """)
        
        psd = quatre_lettre
        wbk = webhook
        
        try:
            nombre = int(psd)              
            for i in range(nombre):
                gen = ''.join(random.choices(string.digits + string.ascii_lowercase, k=4))
                
                url = "https://discord.com/api/v9/unique-username/username-attempt-unauthed"
                
                payload = {"username": gen}
                
                response = requests.post(url, json=payload, timeout=10)
                
                data = response.json()
                
                if response.status_code == 200:
                    if data.get("taken") == False: 
                        data_to_send = {
                            "content": f"**PSEUDO DISPONIBLE !** `{gen}`\n{data}",
                            "username": "WhiteWolf", 
                            "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
                        }
                        requests.post(wbk, json=data_to_send)
                        print(f"Trv env : {gen}")
                    else:
                        print(f"Pris : {gen}")
                else:
                    print("Le pseudo ne marché pas passont a un autre", gen)
        except Exception as e:
            print(f"Error {e}")

if __name__ == "__main__":
    main()