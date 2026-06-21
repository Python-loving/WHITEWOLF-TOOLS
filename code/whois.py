from code.colors import *  

def whois():
    try:
        whois = input(f""" {RED}
            ██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗
            ██║    ██║██║  ██║██╔═══██╗██║██╔════╝
            ██║ █╗ ██║███████║██║   ██║██║███████╗
            ██║███╗██║██╔══██║██║   ██║██║╚════██║
            ╚███╔███╔╝██║  ██║╚██████╔╝██║███████║
            ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝
            
            Met le lien de ton site : """)
    except ValueError as e:
        print(f"Error {e}")
    
    try:
        data = whois.whois(whois)
        print(f"Domaine : {data.domain_name}")
        print(f"Registrar : {data.registrar}")
        print(f"Création : {data.creation_date}")
        print(f"Expiration : {data.expiration_date}")
        print(f"DNS : {data.name_servers}")
    except Exception as e:
        print(f"Error {e}")

if __name__ == "__main__":
    whois()