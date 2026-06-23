import os
import time
import requests 

def githubbb():
    os.system("cls")
    username = input("""
     ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗ 
    ██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗
    ██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝
    ██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗
    ╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝
     ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
        Le Username github : """)
    os.system("cls")
    nom_repo = input("""
     ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗ 
    ██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗
    ██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝
    ██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗
    ╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝
     ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
        Le nom du repo : """)

    url = f"https://api.github.com/repos/{username}/{nom_repo}/commits?per_page=1"
    response = requests.get(url)
    data = response.json()
    try:
        if response.ok:
            commit_data = data[0]

            print(f"Email : {commit_data['commit']['author']['email']}")
            print(f"Name  : {commit_data['commit']['author']['name']}")
            print(f"date  : {commit_data['commit']['author']['date']}")
            print(f"Msg   : {commit_data['commit']['message']}")
            print(f"url   : {commit_data['html_url']}")
            print(f"sign  : {commit_data['commit']['verification']['signature']}")
            print(f"id    : {commit_data['sha']}")
            print(f"PDP   : {commit_data['author']['avatar_url']}")
            print(f"ABO   : {commit_data['author']['followers_url']}")
            print(f"Node  : {commit_data['node_id']}")

            time.sleep(5)
        elif not response.ok:
            print(response.status_code)
            time.sleep(5)
    except Exception as e:
        print(f"Error {e}")

if __name__ == "__main__":
    githubbb()