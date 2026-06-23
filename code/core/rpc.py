import time
from pypresence import Presence, DiscordNotFound


def start_rpc():
    try:
        rpc = Presence("1441226984024965221")
        rpc.connect()

        rpc.update(
            state="White Wolf",
            details="Best Tools",
            large_image="tools",
            large_text="by xql",
            buttons=[
                {
                    "label": "Repository",
                    "url": "https://github.com/Python-loving/WHITEWOLF-TOOLS"
                },
                {
                    "label": "Telegram",
                    "url": "https://t.me/whitewolf_tools"
                }
            ]
        )

        while True:
            time.sleep(15)

    except DiscordNotFound:
        return
