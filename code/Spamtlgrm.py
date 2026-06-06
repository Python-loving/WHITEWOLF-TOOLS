from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import time
import requests


def tlgrm():
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    white = "\033[37m"
    reset = "\033[0m"

    try:
        os.system("cls")
        tkn = input(f"""{blue}
            ████████╗███████╗██╗     ███████╗ ██████╗ ██████╗  █████╗ ███╗   ███╗
            ╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
               ██║   █████╗  ██║     █████╗  ██║  ███╗██████╔╝███████║██╔████╔██║
               ██║   ██╔══╝  ██║     ██╔══╝  ██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
               ██║   ███████╗███████╗███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
               ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
            Met le Token de ton bot telegram : """)
        os.system("cls")
        msg = input(f"""{blue}
            ████████╗███████╗██╗     ███████╗ ██████╗ ██████╗  █████╗ ███╗   ███╗
            ╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
               ██║   █████╗  ██║     █████╗  ██║  ███╗██████╔╝███████║██╔████╔██║
               ██║   ██╔══╝  ██║     ██╔══╝  ██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
               ██║   ███████╗███████╗███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
               ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
            Met le Message a Spam : """)

        try:
            while True:
                async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
                    for i in range(98):
                        await update.message.reply_text(msg)
                    
                app = Application.builder().token(tkn).build()

                app.add_handler(CommandHandler("start", start))

                app.run_polling()

        except Exception as e:
                print("Error", e)
    except Exception as e:
        print("Error", e)

if __name__ == "__main__":
    tlgrm()