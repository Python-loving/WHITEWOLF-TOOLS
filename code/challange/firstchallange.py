import os
import time

def osint():
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    white = "\033[37m"
    reset = "\033[0m"
    os.system("cls")

    ville_loc = "sète"
    office_loc = "archipel de thau"
    date_loc = "08/07/2025"

    vie = 0
    try:
        print(f"""
             ██████╗ ███████╗██╗███╗   ██╗████████╗
            ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
            ██║   ██║███████╗██║██╔██╗ ██║   ██║   
            ██║   ██║╚════██║██║██║╚██╗██║   ██║   
            ╚██████╔╝███████║██║██║ ╚████║   ██║   
             ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
    """)

        print(f"""{blue}
        Un message anonyme a été intercepté sur un forum maritime. Il ne contient qu’une seule phrase :

        “Là où la lumière rouge veille sur les navires blancs, la vérité est enfouie sous les pavés.”

        Aucune localisation n’est donnée, seulement une image jointe.

        Ton objectif est simple : identifier le lieu exact et comprendre ce que cache ce message.

        Indices visibles :

        * Un phare en pierre cylindrique avec une lanterne rouge dominant une jetée
        * Un grand ferry blanc et jaune à quai dans le port
        * Des grues industrielles en arrière-plan indiquant une zone portuaire commerciale active
        * Une digue courbe pavée formant un môle protégeant le bassin
        * Une mer méditerranéenne calme, typique d’un grand port du sud
        * Une présence humaine très faible malgré un lieu touristique habituel

        Message crypté :

        * “môle” + “lumière rouge” fait référence à un phare de jetée portuaire
        * La structure correspond à un phare situé au bout d’un môle dans un grand port méditerranéen

        Hypothèse :
        Le lieu recherché se situe dans un port du sud de la France, identifiable par son activité commerciale, ses ferries et son architecture portuaire spécifique.

        Un détail intrigue :
        Sous les pavés circulaires autour du phare, certaines irrégularités suggèrent un marquage ou une cache dissimulée.

        Consignes :

        * Vous devez trouvé la ville
        * Vous devez trouvé l'Office de tourisme qui propose des visite 
        * Vous devez trouvé quand la photo a etais posté

        Fin du message.

        L'iamge pour le challange ce trouve dans le dossier code/challange/osint.png :)
        """)
        time.sleep(10)
        ville = input(f"""{red}
            ██╗   ██╗██╗██╗     ██╗     ███████╗
            ██║   ██║██║██║     ██║     ██╔════╝
            ██║   ██║██║██║     ██║     █████╗  
            ╚██╗ ██╔╝██║██║     ██║     ██╔══╝  
             ╚████╔╝ ██║███████╗███████╗███████╗
              ╚═══╝  ╚═╝╚══════╝╚══════╝╚══════╝
            
            Met le nom de la ville (En Minuscule) : """)
        try:
            if ville == ville_loc:
                vie += 1
                print("Tu a gagné", "Tu a actuelement", vie, "Point")
            else:
                print("Non Recommence")
        except Exception as e:
            print(f"Error {e}")

        office = input(f"""{blue}
             ██████╗ ███████╗███████╗██╗ ██████╗███████╗
            ██╔═══██╗██╔════╝██╔════╝██║██╔════╝██╔════╝
            ██║   ██║█████╗  █████╗  ██║██║     █████╗  
            ██║   ██║██╔══╝  ██╔══╝  ██║██║     ██╔══╝  
            ╚██████╔╝██║     ██║     ██║╚██████╗███████╗
             ╚═════╝ ╚═╝     ╚═╝     ╚═╝ ╚═════╝╚══════╝
            
            Met Le nom de l'Office de tourisme qui propose les visite (En miniscule (Ne Mais pas le  - Destination Méditerranée)) : """)
        try: 
            if office == office_loc:
                vie += 1
                print("Tu a gagné", "Tu a actuelement", vie, "Point")
            else:
                print("Ce n'est pas ca recommence...")
        except Exception as e:
            print(f"Error {e}")

        date = input(f"""
            ██████╗  █████╗ ████████╗███████╗
            ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
            ██║  ██║███████║   ██║   █████╗  
            ██║  ██║██╔══██║   ██║   ██╔══╝  
            ██████╔╝██║  ██║   ██║   ███████╗
            ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
            
            Met la date du poste de la photo Format:(01/01/2026) : """)
        try:
            if date == date_loc:
                vie += 1
                print("Tu a gagné", "Tu a actuelement", vie, "Point")
            else:
                print("Tu a perdu recommence")
        
        except Exception as e:
            print(f"Error {e}")
    
    except Exception as e:
        print(f"Error {e}")

if __name__ == "__main__":
    osint()