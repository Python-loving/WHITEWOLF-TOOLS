import os
import time
from colorama import Fore
from openai import OpenAI
import json

def ai():
    try:
        os.system("cls")
        choix = input(f"""
            ▄████▄ █████▄ ██ 
            ██▄▄██ ██▄▄█▀ ██ 
            ██  ██ ██     ██ 
            
            Met ton api ( https://groq.com ) : """)
    except ValueError as e:
        print(f"Error {e}")

    while True:
        client = OpenAI(
            api_key=choix,
            base_url="https://api.groq.com/openai/v1",
            )

        try:
            os.system("cls")
            parle = input(f"""
                ▄████▄ ██   ▄█████ ██  ██ ▄████▄ ██████ 
                ██▄▄██ ██   ██     ██████ ██▄▄██   ██   
                ██  ██ ██   ▀█████ ██  ██ ██  ██   ██   
                                                
                Dis ce que tu veux demandé a l'ia : """)
        except ValueError as e:
            print(f"Error {e}")
        try:
            response = client.responses.create(
                input=parle,
                model="openai/gpt-oss-20b",
                )
            print(response.output_text)
            time.sleep(3)
        except Exception as e:
            print(f"Error {e}")
            time.sleep(2)

if __name__ == "__main__":
    ai()