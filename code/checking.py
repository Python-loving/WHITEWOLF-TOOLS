from holehe.core import get_functions, import_submodules
import trio
import httpx
from code.colors import *
import os
import time

def holehe():
    os.system("cls")
    email = input(f"""{GREEN}
        ██  ██ ▄████▄ ██     ██████ ██  ██ ██████ 
        ██████ ██  ██ ██     ██▄▄   ██████ ██▄▄   
        ██  ██ ▀████▀ ██████ ██▄▄▄▄ ██  ██ ██▄▄▄▄ 
                                                
        Met un mail a cherché : """)

    module = import_submodules("holehe.modules")
    websites = get_functions(module)

    out = []

    async def main():
        async with httpx.AsyncClient(timeout=15) as client:
            for website in websites:
                try:
                    await website(email, client, out)
                except:
                    continue

    trio.run(main)

    for result in out:
        if result.get("exists") is True:
            print(f"{result['name']} -> Compte trouvé")

if __name__ == "__main__":
    holehe()