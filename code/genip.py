import os
import time
import subprocess
import random
import string
import requests
from code.colors import *


def ip():
       

        try:
            os.system("cls")
            gen = int(input(f"""{YELLOW}
                 ██████╗ ███████╗███╗   ██╗    ██╗██████╗ 
                ██╔════╝ ██╔════╝████╗  ██║    ██║██╔══██╗
                ██║  ███╗█████╗  ██╔██╗ ██║    ██║██████╔╝
                ██║   ██║██╔══╝  ██║╚██╗██║    ██║██╔═══╝ 
                ╚██████╔╝███████╗██║ ╚████║    ██║██║     
                 ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝╚═╝     
                
                Met le nombre d'ip que tu veux gen : """))
            os.system("cls")
            wbk = input(f"""{YELLOW}
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
                        print(f"Error {e}")
            else:
                print("Error")

        except Exception as e:
            print(f"Error {e}")

if __name__ == "__main__":
    ip()