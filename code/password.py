import os
import random
import string
import time


def password():
    os.system("cls")
    try:
        password = input("""
        ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
        ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
        ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
        ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
        ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
        ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 

        Choisis le nombre de lettre & Chifre : """)
    except ValueError as e:
        print(f"Choisis un nombre valide {e}")

    try:
        password = int(password)

        if password >= 10:
            chars = string.ascii_letters + string.digits + string.punctuation

            result = ''.join(random.choice(chars) for _ in range(password))

            print("Password :", result)
            time.sleep(5)
        else:
            print("Min 10 char")
            time.sleep(5)
    except Exception as e:
        print(f"Error {e}")
        time.sleep(5)
    
if __name__ == "__main__":
    password()