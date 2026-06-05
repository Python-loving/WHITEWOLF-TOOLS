import os
import time
import subprocess
import random
import string
import requests


def ip():
        red = "\033[31m"
        green = "\033[32m"
        yellow = "\033[33m"
        blue = "\033[34m"
        white = "\033[37m"
        reset = "\033[0m"

        try:
            os.system("cls")
            gen = int(input(f"""{yellow}
                 ██████╗ ███████╗███╗   ██╗    ██╗██████╗ 
                ██╔════╝ ██╔════╝████╗  ██║    ██║██╔══██╗
                ██║  ███╗█████╗  ██╔██╗ ██║    ██║██████╔╝
                ██║   ██║██╔══╝  ██║╚██╗██║    ██║██╔═══╝ 
                ╚██████╔╝███████╗██║ ╚████║    ██║██║     
                 ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝╚═╝     
                
                Met le nombre d'ip que tu veux gen : """))
            os.system("cls")
            wbk = input(f"""{yellow}
                 ██████╗ ███████╗███╗   ██╗    ██╗██████╗ 
                ██╔════╝ ██╔════╝████╗  ██║    ██║██╔══██╗
                ██║  ███╗█████╗  ██╔██╗ ██║    ██║██████╔╝
                ██║   ██║██╔══╝  ██║╚██╗██║    ██║██╔═══╝ 
                ╚██████╔╝███████╗██║ ╚████║    ██║██║     
                 ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝╚═╝     
                
                Met ton webhook : """)

            if gen >= 10:
                for i in range(gen):
                    try:
                        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
                        run = subprocess.run(
                            ["ping", "-n", "1", ip],
                            capture_output=True,
                            text=True
                        )
                        if run.returncode == 0:
                            data = {
                                "content": f"IP CHECK\n{ip}", 
                                "username": "WhiteWolf", 
                                "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
                                }
                            requests.post(wbk, json=data)
                        else:
                            print("Ip invalide")
                    except Exception as e:
                        print("Error", e)
            else:
                print("Error")

        except Exception as e:
            print("Error", e)

if __name__ == "__main__":
    ip()