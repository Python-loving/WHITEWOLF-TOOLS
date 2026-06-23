from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import time
import requests
from code.colors import *


def tlgrm():
  

    try:
        os.system("cls")
        tkn = input(f"""{BLUE}
            ████████╗███████╗██╗     ███████╗ ██████╗ ██████╗  █████╗ ███╗   ███╗
            ╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
               ██║   █████╗  ██║     █████╗  ██║  ███╗██████╔╝███████║██╔████╔██║
               ██║   ██╔══╝  ██║     ██╔══╝  ██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
               ██║   ███████╗███████╗███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
               ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
            Met le Token de ton bot telegram : """)
        os.system("cls")
        msg = input(f"""{BLUE}
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
                print(f"Error {e}")
    except Exception as e:
        print(f"Error {e}")

if __name__ == "__main__":
    tlgrm()