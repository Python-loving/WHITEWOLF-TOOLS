from pypresence import Presence
import os
import time
from colorama import Fore

def rpc_conf():
    os.system("cls")
    id_presence = input(f"""{Fore.RED}
        █████▄  █████▄ ▄█████   ████▄  ██ ▄█████ ▄█████ ▄████▄ █████▄  ████▄  
        ██▄▄██▄ ██▄▄█▀ ██       ██  ██ ██ ▀▀▀▄▄▄ ██     ██  ██ ██▄▄██▄ ██  ██ 
        ██   ██ ██     ▀█████   ████▀  ██ █████▀ ▀█████ ▀████▀ ██   ██ ████▀  
                                                                      
        Met ton id de bot : """)
    os.system("cls")
    name = input(f"""{Fore.RED}
        █████▄  █████▄ ▄█████   ████▄  ██ ▄█████ ▄█████ ▄████▄ █████▄  ████▄  
        ██▄▄██▄ ██▄▄█▀ ██       ██  ██ ██ ▀▀▀▄▄▄ ██     ██  ██ ██▄▄██▄ ██  ██ 
        ██   ██ ██     ▀█████   ████▀  ██ █████▀ ▀█████ ▀████▀ ██   ██ ████▀  
                                                                      
        Met le nom de ton rpc : """)
    os.system("cls")
    image = input(f"""{Fore.RED}
        █████▄  █████▄ ▄█████   ████▄  ██ ▄█████ ▄█████ ▄████▄ █████▄  ████▄  
        ██▄▄██▄ ██▄▄█▀ ██       ██  ██ ██ ▀▀▀▄▄▄ ██     ██  ██ ██▄▄██▄ ██  ██ 
        ██   ██ ██     ▀█████   ████▀  ██ █████▀ ▀█████ ▀████▀ ██   ██ ████▀  
                                                                      
        Met ta grande image : """)
    os.system("cls")
    image_petite = input(f"""{Fore.RED}
        █████▄  █████▄ ▄█████   ████▄  ██ ▄█████ ▄█████ ▄████▄ █████▄  ████▄  
        ██▄▄██▄ ██▄▄█▀ ██       ██  ██ ██ ▀▀▀▄▄▄ ██     ██  ██ ██▄▄██▄ ██  ██ 
        ██   ██ ██     ▀█████   ████▀  ██ █████▀ ▀█████ ▀████▀ ██   ██ ████▀  
                                                                      
        Met ta petite image : """)
    os.system("cls")
    name_button1 = input(f"""{Fore.RED}
        █████▄  █████▄ ▄█████   ████▄  ██ ▄█████ ▄█████ ▄████▄ █████▄  ████▄  
        ██▄▄██▄ ██▄▄█▀ ██       ██  ██ ██ ▀▀▀▄▄▄ ██     ██  ██ ██▄▄██▄ ██  ██ 
        ██   ██ ██     ▀█████   ████▀  ██ █████▀ ▀█████ ▀████▀ ██   ██ ████▀  
                                                                      
        Met ton premier nom de bouton : """)
    os.system("cls")
    name_button2 = input(f"""{Fore.RED}
        █████▄  █████▄ ▄█████   ████▄  ██ ▄█████ ▄█████ ▄████▄ █████▄  ████▄  
        ██▄▄██▄ ██▄▄█▀ ██       ██  ██ ██ ▀▀▀▄▄▄ ██     ██  ██ ██▄▄██▄ ██  ██ 
        ██   ██ ██     ▀█████   ████▀  ██ █████▀ ▀█████ ▀████▀ ██   ██ ████▀  
                                                                      
        Met ton deuxième nom de bouton : """)
    os.system("cls")
    lien_button1 = input(f"""{Fore.RED}
        █████▄  █████▄ ▄█████   ████▄  ██ ▄█████ ▄█████ ▄████▄ █████▄  ████▄  
        ██▄▄██▄ ██▄▄█▀ ██       ██  ██ ██ ▀▀▀▄▄▄ ██     ██  ██ ██▄▄██▄ ██  ██ 
        ██   ██ ██     ▀█████   ████▀  ██ █████▀ ▀█████ ▀████▀ ██   ██ ████▀  
                                                                      
        Met ton lien du premier button : """)
    os.system("cls")
    lien_button2 = input(f"""{Fore.RED}
        █████▄  █████▄ ▄█████   ████▄  ██ ▄█████ ▄█████ ▄████▄ █████▄  ████▄  
        ██▄▄██▄ ██▄▄█▀ ██       ██  ██ ██ ▀▀▀▄▄▄ ██     ██  ██ ██▄▄██▄ ██  ██ 
        ██   ██ ██     ▀█████   ████▀  ██ █████▀ ▀█████ ▀████▀ ██   ██ ████▀  
                                                                      
        Met ton lien du deuxieme button : """)
    try:
        rpc = Presence(id_presence)
        rpc.connect()

        rpc.update(
            state=name,
            large_image=image,
            small_image=image_petite,
            start=time.time(),
            buttons=[
                {"label": name_button1, "url": lien_button1},
                {"label": name_button2, "url": lien_button2}
            ]
        )

        while True:
            time.sleep(15)
    except Exception as e:
        print(f"Error {e}")

if __name__ == "__main__":
    rpc_conf()