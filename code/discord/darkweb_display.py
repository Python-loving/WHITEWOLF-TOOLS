import os
import time
from darkweb import links


def darkweb_display():
    os.system("cls")
    print("""
                ██████╗  █████╗ ██████╗ ██╗  ██╗    ██╗    ██╗███████╗██████╗
                ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██║    ██║██╔════╝██╔══██╗
                ██║  ██║███████║██████╔╝█████╔╝     ██║ █╗ ██║█████╗  ██████╔╝
                ██║   ██║██╔══██║██╔══██╗██╔═██╗     ██║███╗██║██╔══╝  ██╔══██╗
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
