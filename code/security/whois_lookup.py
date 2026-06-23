import os
import time
from code.colors import RED


def whois_lookup():
    try:
        import whois
    except ImportError:
        print("Error: 'python-whois' package is required for whois lookup.")
        print("Install it with: pip install python-whois")
        time.sleep(5)
        return

    try:
        site = input(f""" {RED}
                    ██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗
                    ██║    ██║██║  ██║██╔═══██╗██║██╔════╝
                    ██║ █╗ ██║███████║██║   ██║██║███████╗
                    ██║███╗██║██╔══██║██║   ██║██║╚════██║
                    ╚███╔███╔╝██║  ██║╚██████╔╝██║███████║
                    ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝

                    Met le lien de ton site : """)
    except ValueError as e:
        print(f"Error {e}")
        return

    try:
        data = whois.whois(site)
        print(f"Domaine : {data.domain_name}")
        print(f"Registrar : {data.registrar}")
        print(f"Création : {data.creation_date}")
        print(f"Expiration : {data.expiration_date}")
        print(f"DNS : {data.name_servers}")
    except Exception as e:
        print(f"Error {e}")
