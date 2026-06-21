from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
from code.colors import *
import random
import string
import time   
import os

def randomusername(lenght=8):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(lenght))

def instaautomation():
    os.system("cls")
    USERNAME = input(f"""{MAGENTA}
    ██  ██ ▄█████ ██████ █████▄  ███  ██ ▄████▄ ██▄  ▄██ ██████ 
    ██  ██ ▀▀▀▄▄▄ ██▄▄   ██▄▄██▄ ██ ▀▄██ ██▄▄██ ██ ▀▀ ██ ██▄▄   
    ▀████▀ █████▀ ██▄▄▄▄ ██   ██ ██   ██ ██  ██ ██    ██ ██▄▄▄▄ 
                                                            
    Met ton username instagram : """)
    os.system("cls")
    PASSWORD = input(f"""{MAGENTA}
    █████▄ ▄████▄ ▄█████ ▄█████ ██     ██ ▄████▄ █████▄  ████▄  
    ██▄▄█▀ ██▄▄██ ▀▀▀▄▄▄ ▀▀▀▄▄▄ ██ ▄█▄ ██ ██  ██ ██▄▄██▄ ██  ██ 
    ██     ██  ██ █████▀ █████▀  ▀██▀██▀  ▀████▀ ██   ██ ████▀  
                                                            
    Met ton password instagram : """)
    os.system("cls")
    defa = input(f"""
    ████▄ ██████ ▄████▄   ▄█████ ▄████▄ ████▄  ██████ 
     ▄██▀ ██▄▄   ██▄▄██   ██     ██  ██ ██  ██ ██▄▄   
    ███▄▄ ██     ██  ██   ▀█████ ▀████▀ ████▀  ██▄▄▄▄ 
                                                  
    Met ton 2fa code instagram si vous avez pas metez "2" : """)

    if defa == "2":
        cl = Client()
        cl.login(USERNAME, PASSWORD)
        cl.dump_settings("session.json")
        while True:
            username = randomusername(7)                    
            user_id = cl.user_id_from_username(username)    
            medias = cl.user_medias(user_id, 5)

            for media in medias:                            
                cl.media_like(media.pk)
                cl.media_comment(media.pk, "Tres uhq")
                print(f"Envoyer :)")
            time.sleep(15)                                  

    else:
        cl = Client()
        cl.login(USERNAME, PASSWORD, verification_code=defa)
        cl.dump_settings("session.json")
        while True:
            username = randomusername(7)                  
            user_id = cl.user_id_from_username(username)    
            medias = cl.user_medias(user_id, 5)

            for media in medias:                           
                cl.media_like(media.pk)
                cl.media_comment(media.pk, "Tres uhq")
                print(f"Envoyer :)")
            time.sleep(15)                                  

if __name__ == "__main__":
    instaautomation()