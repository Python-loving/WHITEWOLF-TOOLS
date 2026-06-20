# Is not finish and not testing sory my account discord is Rate Limiting juste waiting my unrate and testing nuker :)

# ANCHOR - White WOLF :)


import os
import time
import random
import requests
import discord
from code.colors import *

def nuker():
   

    os.system("cls")
    token = input(f"""{BLUE}
            ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
            ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
            ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
            ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
            ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
            ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
            
            Met le token de ton bot : """)

    os.system("cls")
    server_id = input(f"""{BLUE}
            ██╗██████╗ 
            ██║██╔══██╗
            ██║██║  ██║
            ██║██║  ██║
            ██║██████╔╝
            ╚═╝╚═════╝ 
            
            Met l'id du server : """)

    TOKEN = token
    GUILD_ID = server_id

    intents = discord.Intents.default()
    intents.members = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"Connecté en tant que {client.user}")

        guild = client.get_guild(GUILD_ID)

        member_ids = []

        for member in guild.members:
            member_ids.append(member.id)
        
        print(member_ids)

        await client.close()

    @client.event
    async def on_ready():
        for user_id in member_ids:
            try:
                user = await client.fetch_user(user_id)
                await guild.ban(user, reason="Ban by white Wolf")
                print(f"Banni : {user}")
            except Exception as e:
                print(f"Error {e}")
            
            await client.close()

    client.run(TOKEN)

if __name__ == "__main__":
    nuker()