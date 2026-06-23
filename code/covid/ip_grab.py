import os
import time
import requests


def grab_ip():
    os.system("cls")
    try:
        ip_grabing = input("""
                     ██████╗ ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗     ██╗██████╗
                    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝     ██║██╔══██╗
                    ██║  ███╗██████╔╝███████║██████╔╝██║██╔██╗ ██║██║  ███╗    ██║██████╔╝
                    ██║   ██║██╔══██╗██╔══██║██╔══██╗██║██║╚██╗██║██║   ██║    ██║██╔═══╝
                    ╚██████╔╝██║  ██║██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝    ██║██║
                    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝  ╚═════╝     ╚═╝╚═╝

                    Met Ton webhook (Pour tester sur des gens autre que vous allez sur le covid builder) : """)
    except ValueError as e:
        print(f"Error {e}")
        return

    webhook = ip_grabing
    try:
        ip = requests.get("https://checkip.amazonaws.com").text.strip()
        data = {
            "content": ip,
            "username": "WhiteWolf",
            "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
        }
        requests.post(webhook, json=data)
    except ValueError:
        print("Value error")
        time.sleep(3)
