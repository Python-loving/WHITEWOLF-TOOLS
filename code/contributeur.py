import time
import requests
import os

def contributeur():
    url = "https://api.github.com/repos/python-loving/whitewolf-tools/contributors"
    response = requests.get(url)

    if response.status_code == 200:
        os.system("cls")
        contributors = response.json()

        for contributor in contributors:
            print(f"https://github.com/{contributor["login"]}")
            time.sleep(0.5)
        time.sleep(5)
    else:
        print(response.status_code)
        time.sleep(5)

if __name__ == "__main__":
    contributeur()