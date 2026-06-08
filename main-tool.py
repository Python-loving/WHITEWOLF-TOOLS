from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import subprocess

window = tk.Tk()
window.title("WHITEWOLF-TOOLS")
window.geometry("1200x560")
window.minsize(1200, 560)
window.iconbitmap("icon-tool.ico")
window.configure(bg="black")

hautgauche_frame = Frame(window, bg="black")
hautgauche_frame.grid(row=0, column=0, sticky="nw")

gauche_frame = Frame(window, bg="black")
gauche_frame.place(x=100, rely=0.5, anchor="w")

bg_label = tk.Label(window, bg="black")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

droite_frame = Frame(window, bg="black")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=0)

droite_frame.grid(row=0, column=1, sticky="ne")


gif = Image.open("back.gif")
frames = []

try:
    while True:
        frames.append(ImageTk.PhotoImage(gif.copy()))
        gif.seek(len(frames))
except Exception as e:
    print(f"ERROR {e}")
    pass

frame_index = 0

def animate():
    global frame_index

    bg_label.config(image=frames[frame_index])

    frame_index = (frame_index + 1) % len(frames)

    window.after(1, animate)


animate()

texte_complet = f"""
            ██╗    ██╗██╗  ██╗██╗████████╗███████╗██╗    ██╗ ██████╗ ██╗     ███████╗
            ██║    ██║██║  ██║██║╚══██╔══╝██╔════╝██║    ██║██╔═══██╗██║     ██╔════╝
            ██║ █╗ ██║███████║██║   ██║   █████╗  ██║ █╗ ██║██║   ██║██║     █████╗  
            ██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██║███╗██║██║   ██║██║     ██╔══╝  
            ╚███╔███╔╝██║  ██║██║   ██║   ███████╗╚███╔███╔╝╚██████╔╝███████╗██║     
             ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝    """

titre = tk.Label(hautgauche_frame, text=texte_complet, bg="black", fg="white", font=("Courier New", 7, "bold"))

titre.pack()

index = 0
suppression = False


def animation():
    global index, suppression 

    if not suppression:
        index += 1
        titre.config(text=texte_complet[:index])

        if index >= len(texte_complet):
            window.after(1500, commencer_suppression)
            return

    else:
        index -= 1
        titre.config(text=texte_complet[:index])

        if index <= 0:
            suppression = False

    window.after(1, animation)


def commencer_suppression():
    global suppression
    suppression = True
    animation()

animation()

def click():
    subprocess.Popen("start cmd /k python main.py", shell=True)

investigation = Button(gauche_frame, text="INVESTIGUER", font=("Orbitron", 14, "bold"), fg="white", bg="#111111", activebackground="#222222", activeforeground="white", relief="flat", bd=0, padx=20, pady=10, cursor="hand2", command=click)


credits = Label(droite_frame, text="© xql.dev  |  light UI build", bg="black", fg="#bdbdbd", font=("Courier New", 8))

credits.pack(side="right", anchor="se", padx=10, pady=8)


investigation.pack(pady=10)

hautgauche_frame.lift()

gauche_frame.lift()

droite_frame.lift()

window.mainloop()