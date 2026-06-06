from cryptography.fernet import Fernet
import json
import os
import time


def passwdmanage():
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    white = "\033[37m"
    reset = "\033[0m"
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
        print("Error", e)
    try: 
        if choix == "2":
            os.system("cls")
            ky = input(f"""{white}
                ██╗  ██╗███████╗██╗   ██╗
                ██║ ██╔╝██╔════╝╚██╗ ██╔╝
                █████╔╝ █████╗   ╚████╔╝ 
                ██╔═██╗ ██╔══╝    ╚██╔╝  
                ██║  ██╗███████╗   ██║   
                ╚═╝  ╚═╝╚══════╝   ╚═╝   
                
                Met ta key : """)
            os.system("cls")
            add = input(f"""{blue}
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
                print("Error", e)
    except Exception as e:
        print("Error", e)

    try:    
        if choix == "3":
            os.system("cls")
            ky_list = input(f"""{red}
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
                print("Error", e)

    except Exception as e:
        print("Error", e)

    try:
        if choix == "4":
            print("Au-Revoir Frro...")
            time.sleep(2)
    except Exception as e:
        print("Error", e)

if __name__ == "__main__":
    passwdmanage()