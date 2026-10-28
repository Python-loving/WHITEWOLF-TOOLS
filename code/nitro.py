import os
import string
import random
import requests
import json

def nitro():
    os.system("cls")
    webhook = input("Met ton webhook Discord : ").strip()
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
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "*/*"
        }
        for i in range(nombre):
            char = string.ascii_letters + string.digits
            result = ''.join(random.choice(char) for _ in range(16))
            url = f"https://discord.gift/{result}"
            api_url = f"https://discord.com/api/v9/entitlements/gift-codes/{result}?with_application=false&with_subscription_plan=true"

            try:
                response = requests.get(api_url, headers=headers, timeout=10)
                try:
                    data = response.json()
                except:
                    data = {}

                if response.status_code == 200 and isinstance(data, dict):
                    if data.get("message") or data.get("code"):
                        print(f"[INVALIDE] {url}")
                        continue
                    if data.get("uses") is not None and data.get("max_uses") is not None:
                        if data.get("uses") >= data.get("max_uses"):
                            print(f"[INVALIDE] {url}")
                            continue
                    if data.get("redeemed") is True:
                        print(f"[INVALIDE] {url}")
                        continue
                    print(f"[VALIDE] {url}")
                    with open("nitro.txt", "a", encoding="utf-8") as fichier:
                        fichier.write(f"{url}\n")
                    if webhook:
                        try:
                            requests.post(webhook, json={"content": url}, timeout=10)
                        except:
                            pass
                    continue

                print(f"[INVALIDE] {url}")
            except requests.RequestException:
                print(f"[INVALIDE] {url}")
    except:
        print("Ca Nas pas marché sorry :)")

if __name__ == "__main__":
    nitro()
