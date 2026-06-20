import cv2
import time
from colorama import Fore
import os
import requests
from code.colors import *
def webcam():
    os.system("cls")
    webhook = input(f"""{MAGENTA}
        ██     ██ ██████ █████▄ ▄█████ ▄████▄ ██▄  ▄██   
        ██ ▄█▄ ██ ██▄▄   ██▄▄██ ██     ██▄▄██ ██ ▀▀ ██   
         ▀██▀██▀  ██▄▄▄▄ ██▄▄█▀ ▀█████ ██  ██ ██    ██   
                                                 
        Met ton webhook discord : """)
    try:
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print(f"{BLUE} Pas de cam")
            return
        else:
            print(f"{GREEN} Prise en photo")

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
            print(f"{RED} Probleme")

        cap.release()
    except Exception as e:
        print(f"Erorr {e}")

if __name__ == "__main__":
    webcam()