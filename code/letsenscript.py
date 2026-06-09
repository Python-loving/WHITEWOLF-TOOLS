import ssl
import socket
import os

def domaine():
    try:
        os.system("cls")
        main = input("""
            ███████ ███████ ██              ██     ████████ ██      ███████ 
            ██      ██      ██             ██         ██    ██      ██      
            ███████ ███████ ██            ██          ██    ██      ███████ 
                 ██      ██ ██           ██           ██    ██           ██ 
            ███████ ███████ ███████     ██            ██    ███████ ███████ 
            
            Met Ton domaine : """)
        
        try:
            context = ssl.create_default_context()
            with socket.create_connection((main, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=main) as tls:
                    print(tls.version())

        except Exception as e:
            print(f"Error {e}")
    except ValueError as e:
        print(f"Error {e}")

if __name__ == "__main__":
    domaine()