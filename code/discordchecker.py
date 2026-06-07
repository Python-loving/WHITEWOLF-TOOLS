import random
import os
import string
import requests

def main():
        red = "\033[31m"
        green = "\033[32m"
        yellow = "\033[33m"
        blue = "\033[34m"
        white = "\033[37m"
        reset = "\033[0m"

        os.system("cls")
        quatre_lettre = input(f""" {green}
           
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
        webhook = input(f""" {blue}
           
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
            if psd >= "10":
                try:
                    for i in range(int(psd)):
                        gen = ''.join(random.choices(string.digits + string.ascii_lowercase, k=4))
                        
                        url = "https://discord.com/api/v9/unique-username/username-attempt-unauthed"
                        
                        payload = {"username": gen}
                        
                        response = requests.post(url, json=payload, timeout=10)
                        
                        data = response.json()
                        
                        if response.status_code == 200:
                            data = {
                                "content": data, 
                                "username": "WhiteWolf", 
                                "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
                            }
                            requests.post(wbk, json=data)
                        else:
                            print("Le pseudo ne marché pas passont a un autre", gen)
                except Exception as e:
                    print("Error", e)
        except Exception as e:
            print("Error", e)
if __name__ == "__main__":
    main()