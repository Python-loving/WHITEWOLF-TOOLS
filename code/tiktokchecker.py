import os
import time
import requests
import random
import string

def tiktok():
        red = "\033[31m"
        green = "\033[32m"
        yellow = "\033[33m"
        blue = "\033[34m"
        white = "\033[37m"
        reset = "\033[0m"

        os.system("cls")
        choix = int(input(f""" {red}

            ████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗
            ╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝
               ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝ 
               ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗ 
               ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗
               ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                               
            Met Le nombre de pseudo que tu veux cherché : """))
        os.system("cls")
        webhookdsc = input(f""" {red}
                    
            ████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗
            ╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝
               ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝ 
               ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗ 
               ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗
               ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                              
            Met ton Webhook discord : """)

        dsc = webhookdsc

        try:
            if choix >= 10:
                for i in range(choix):
                    pseudo = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
                    url = f"https://www.tiktok.com/@{pseudo}"
                    response = requests.get(url)
                    try:
                        if response.ok:
                            data = {
                            "content": pseudo, 
                            "username": "WhiteWolf", 
                            "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
                            }
                            requests.post(dsc, json=data)
                        else:
                            print("Pseudo deja pris", pseudo)
                    except Exception as e:
                        print("Error", e)
                    
            else:
                print("Faut mètre au minimume 10 Pseudo")
        except Exception as e:
            print("Error", e)

if __name__ == "__main__":
    tiktok()