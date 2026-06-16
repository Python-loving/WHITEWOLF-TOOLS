from tkinter import *
import os
import requests
import time

def error():
    while True:
        window = Tk()
        window.title("Error")
        window.resizable(False, False)
        window.attributes('-topmost', True)
        #window.iconbitmap("error.ico") # Si tu veux mètre un icon mais pour le covid sais mieu de pas en mètre au moin on empacte pas l'image avec pyinstaller
        window.geometry("200x70")
        window.config(background="white")

        window_title = Label(window, text="Error 400", background="white", height="30", width="30")
        window_title.pack(expand=True)

        window.mainloop()
if __name__ == "__main__":
    error()