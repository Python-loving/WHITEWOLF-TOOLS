import os
import time
import string
import random
import requests

def nitro():
    os.system("cls")
    nombre = input("""
        ███╗   ██╗██╗████████╗██████╗  ██████╗ 
        ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗
        ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║
        ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║
        ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝
        ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ 
        Met le nombre de fois que tu veux essayé : """)
    try:
        nombre = int(nombre)
        for i in range(nombre):
            char = string.ascii_letters + string.digits
            result = ''.join(random.choice(char) for _ in range(16))
            response = requests.get(f"https://discord.gift/{result}")

            if response.ok:
                with open("nitro.txt", "a", encoding="utf-8") as fichier:
                    fichier.write(f"https://discord.gift/{result}\n")
    except:
        print("Ca Nas pas marché sorry :)")

if __name__ == "__main__":
    nitro()