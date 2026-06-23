import os
import time
import requests

def webstatus():
    os.system("cls")
    try:
        site = input("""
            ██╗    ██╗███████╗██████╗     ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗
            ██║    ██║██╔════╝██╔══██╗    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝
            ██║ █╗ ██║█████╗  ██████╔╝    ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗
            ██║███╗██║██╔══╝  ██╔══██╗    ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║
            ╚███╔███╔╝███████╗██████╔╝    ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║
             ╚══╝╚══╝ ╚══════╝╚═════╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝
            
            Choisis l'url du site que tu veux check : """)
    except ValueError as e:
        print(f"Error {e}")

    url = site
    response = requests.get(url)
    try:
        if response.status_code == 200:
            print(f"Le site répond en : {response.time} ")
            time.sleep(2)
        else:
            print(f"Le site ne répond pas {response.status_code}")
            time.sleep(2)
    except Exception as e:
        print(f"Error {e}")

if __name__ == "__main__":
    webstatus()


# OLD LOGIC

# def webstatus():
#     os.system("cls")
#     try:
#         site = input("""
#             ██╗    ██╗███████╗██████╗     ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗
#             ██║    ██║██╔════╝██╔══██╗    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝
#             ██║ █╗ ██║█████╗  ██████╔╝    ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗
#             ██║███╗██║██╔══╝  ██╔══██╗    ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║
#             ╚███╔███╔╝███████╗██████╔╝    ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║
#              ╚══╝╚══╝ ╚══════╝╚═════╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝
            
#             Choisis l'url du site que tu veux check : """)
#     except ValueError as e:
#         print(f"Error {e}")
        
#     url = site
#     response = requests.get(url)
#     try:
#         if response.ok:
#             print(f"Le site a répondu en : {response.elapsed.total_seconds() * 1000:.2f} ms")
#             time.sleep(3)
#         else:
#             print("Le site na pas répondu présents")
#             time.sleep(3)
#     except Exception as e:
#         print(f"Error {e}")