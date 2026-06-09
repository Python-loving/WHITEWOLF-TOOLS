import questionary
import os
import subprocess
import random
import socket

def test(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)

    try:
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

def ip():
    os.system("cls")
    choix = questionary.select(
        "Fais Ton choix",
        [
            "Port scanner",
            "Quit"
        ]
    ).ask()

    if choix == "Port scanner":
        os.system("cls")
        main = input("""
            ██ ██████      ███████  ██████  █████  ███    ██ ███    ██ ███████ ██████  
            ██ ██   ██     ██      ██      ██   ██ ████   ██ ████   ██ ██      ██   ██ 
            ██ ██████      ███████ ██      ███████ ██ ██  ██ ██ ██  ██ █████   ██████  
            ██ ██               ██ ██      ██   ██ ██  ██ ██ ██  ██ ██ ██      ██   ██ 
            ██ ██          ███████  ██████ ██   ██ ██   ████ ██   ████ ███████ ██   ██ 

            Met L'ip que tu veux vérifié : """)

        print("Scanning...")

        for p in range(1, 65536):  
            if test(main, p):
                print(f"Port open : {p}")


if __name__ == "__main__":
    ip()