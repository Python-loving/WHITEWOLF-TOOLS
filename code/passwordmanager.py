from cryptography.fernet import Fernet
import json
import os
import time
from code.colors import *


def passwdmanage():
    
    os.system("cls")
    choix = input(f"""{green}
        ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
        ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
        ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
        ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
        ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
        ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 

        1. [Gen Key]  4. [Quit]
        2. [Add Mdps]  
        3. [List mdps]
        
        Choisis Ton option : """)
    
    try:
        if choix == "1":    
            key = Fernet.generate_key()
            with open("key.txt", "w", encoding="utf-8") as fichier:
                    fichier.write(key.decode())
    except Exception as e:
        print(f"Error {e}")
    try: 
        if choix == "2":
            os.system("cls")
            ky = input(f"""{WHITE}
                ██╗  ██╗███████╗██╗   ██╗
                ██║ ██╔╝██╔════╝╚██╗ ██╔╝
                █████╔╝ █████╗   ╚████╔╝ 
                ██╔═██╗ ██╔══╝    ╚██╔╝  
                ██║  ██╗███████╗   ██║   
                ╚═╝  ╚═╝╚══════╝   ╚═╝   
                
                Met ta key : """)
            os.system("cls")
            add = input(f"""{BLUE}
                 █████╗ ██████╗ ██████╗     ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
                ██╔══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
                ███████║██║  ██║██║  ██║    ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
                ██╔══██║██║  ██║██║  ██║    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
                ██║  ██║██████╔╝██████╔╝    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
                ╚═╝  ╚═╝╚═════╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                    
                Met Ton password a ajouté : """)
            try:
                passwd = add

                fernet = Fernet(ky.encode())

                encrypted = fernet.encrypt(passwd.encode())
                print("Chiffré : ", encrypted)

                with open("encrypted.txt", "w", encoding="utf-8") as fichier: # ANCHOR - Toujour retenur J'utilise tres peut donc forcement dificulté a refair...
                    fichier.write(encrypted.decode())
            
            except Exception as e:
                print(f"Error {e}")
    except Exception as e:
        print(f"Error {e}")

    try:    
        if choix == "3":
            os.system("cls")
            ky_list = input(f"""{RED}
                    ██╗     ██╗███████╗████████╗
                    ██║     ██║██╔════╝╚══██╔══╝
                    ██║     ██║███████╗   ██║   
                    ██║     ██║╚════██║   ██║   
                    ███████╗██║███████║   ██║   
                    ╚══════╝╚═╝╚══════╝   ╚═╝   
    
                    Met Ta key : """)
            try:
                fernet = Fernet(ky_list.encode())

                with open("encrypted.txt", "r", encoding="utf-8") as fichier: # ANCHOR - For read a fichier just using variable and using methods Read
                    contenu = fichier.read()

                decrypted = fernet.decrypt(contenu.encode()).decode()

                print("Mdps :", decrypted)
                
            except Exception as e:
                print(f"Error {e}")

    except Exception as e:
        print(f"Error {e}")

    try:
        if choix == "4":
            print("Au-Revoir Frro...")
            time.sleep(2)
    except Exception as e:
        print(f"Error {e}")

if __name__ == "__main__":
    passwdmanage()