import requests
import os
import time
from colorama import Fore

def tokenchecker():
    os.system("cls")
    token = input(f"""{LIGHTMAGENTA_EX}
      ██████ ▄████▄ ██ ▄█▀ ██████ ███  ██   ▄█████ ██  ██ ██████ ▄█████ ██ ▄█▀ ██████ █████▄  
        ██   ██  ██ ████   ██▄▄   ██ ▀▄██   ██     ██████ ██▄▄   ██     ████   ██▄▄   ██▄▄██▄ 
        ██   ▀████▀ ██ ▀█▄ ██▄▄▄▄ ██   ██   ▀█████ ██  ██ ██▄▄▄▄ ▀█████ ██ ▀█▄ ██▄▄▄▄ ██   ██ 
                                                                                        
      Met le token que tu veux check : """)
    
    headers = {
    "Authorization": token,
    "Content-Type": "application/json"
    }

    data = {}  

    response = requests.get("https://discord.com/api/v10/users/@me", headers=headers)

    try:
    
        if response.status_code == 200:
            user = response.json()
    
            print("Username                :", user.get("username"))
            print("Pseudo affichage        :", user.get("global_name"))
            print("Email                   :", user.get("email"))
            print("Téléphone               :", user.get("phone"))         
            print("Email vérifiée          :", user.get("verified"))
            print("Nitro (moyen de paiement) :", user.get("premium_type"))  
            
            print("\nAutres infos :")
            print("ID                      :", user.get("id"))
            print("Avatar                  :", user.get("avatar"))
    
        else:
            print("Error", response.text)
    except Exception as e:
        print(f"Error {e}")
if __name__ == "__main__":
    tokenchecker()