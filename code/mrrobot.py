import os
import time
import requests
import webbrowser

def robot():
    
    while True:
        try:
            webbrowser.open("https://www.youtube.com/shorts/3xXdTHlPdwE")
        except Exception as e:
            print(f"Error {e}")
            
if __name__ == "__main__":
    robot()
            
        