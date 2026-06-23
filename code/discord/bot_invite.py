import os
import time


def bot_invite():
    os.system("cls")
    id_bot = int(input("""
                ██╗███╗   ██╗██╗   ██╗██╗████████╗
                ██║████╗  ██║██║   ██║██║╚══██╔══╝
                ██║██╔██╗ ██║██║   ██║██║   ██║
                ██║██║╚██╗██║╚██╗ ██╔╝██║   ██║
                ██║██║ ╚████║ ╚████╔╝ ██║   ██║
                ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝

                Met L'id de ton bot : """))
    try:
        id = id_bot
        print(f"https://discord.com/oauth2/authorize?client_id={id}&permissions=8&integration_type=0&scope=bot")
        time.sleep(5)
    except ValueError:
        print("Problème...")
        time.sleep(5)
