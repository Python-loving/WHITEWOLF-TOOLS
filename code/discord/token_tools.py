import os
import base64
import string
import random
import time


def token_bruteforce():
    os.system("cls")
    id = input("""
                ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
                ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
                   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
                   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
                   ██║   ╚██████╔╝██║  ██╗███████╗██║  ╚████║
                   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝

                    Met L'id du gars : """)
    try:
        user_id = id
        part1 = base64.b64encode(user_id.encode()).decode()
        part2 = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        part3 = ''.join(random.choices(string.ascii_letters + string.digits, k=18))
        token = f"{part1}.{part2}.{part3}"
        print(f"\nToken : \n {token}")
        time.sleep(2)
    except:
        print("Ca na pas marché")
        time.sleep(2)
