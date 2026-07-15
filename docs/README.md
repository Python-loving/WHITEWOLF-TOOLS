# 🐺 WhiteWolf Tools

<p align="center">
  <img src="https://i.postimg.cc/NFLR2rCM/image.png" alt="WhiteWolf Logo" width="200" />
</p>

<p align="center">
  <a href="https://github.com/Python-loving/WHITEWOLF-TOOLS/stargazers"><img src="https://img.shields.io/github/stars/Python-loving/WHITEWOLF-TOOLS?style=for-the-badge&color=yellow" alt="Stars"></a>
  <a href="https://github.com/Python-loving/WHITEWOLF-TOOLS/network/members"><img src="https://img.shields.io/github/forks/Python-loving/WHITEWOLF-TOOLS?style=for-the-badge&color=blue" alt="Forks"></a>
  <a href="https://github.com/Python-loving/WHITEWOLF-TOOLS/issues"><img src="https://img.shields.io/github/issues/Python-loving/WHITEWOLF-TOOLS?style=for-the-badge&color=red" alt="Issues"></a>
  <img src="https://img.shields.io/badge/OS-Windows-blue?style=for-the-badge&logo=windows" alt="OS Windows">
  <img src="https://img.shields.io/badge/Made%20With-Python-3776AB?style=for-the-badge&logo=python" alt="Made With Python">
</p>

---

## 📖 Présentation

**WhiteWolf Tools** est une suite d'outils en ligne de commande (CLI) polyvalente et complète conçue pour l'**OSINT**, la **sécurité**, l'**automatisation** et la gestion de **Discord**. Dotée d'une interface en menus ASCII élégante et entièrement interactive, elle rassemble de nombreux scripts de recherche d'informations et d'utilitaires dans un point d'entrée unique : `main.py`.

> [!WARNING]
> **Recommandation Système** : Windows est fortement recommandé en raison de dépendances système spécifiques comme `msvcrt` (lecture clavier native), Microsoft Edge, `mss` (captures d'écran Windows), OpenCV et des commandes de gestion de processus (`taskkill`). Python 3 est requis.

---

## 🛠️ Structure du Projet

```
WHITEWOLF-TOOLS/
├── main.py                        # Menu principal et point d'entrée de l'application
├── api.py                         # Clés d'API (ipify, apilayer, viewdns) — Ignoré par Git
├── sites.py                       # Base de données d'URLs pour le lookup username
├── darkweb.py                     # Annuaire catégorisé de liens .onion (Darkweb)
├── covid.py                       # Code source du chargeur autonome (voir section Covid)
├── scanner.py                     # Extracteur autonome de jetons Discord (Browsers & Apps)
├── builder.py                     # Compilateur et obfuscateur de covid.py (via PyArmor & PyInstaller)
├── Icon.ico                       # Icône Windows utilisée pour la compilation
├── Virus-explain.md               # Documentation explicative dédiée au module Covid/Stealer
├── SECURITY.md                    # Avertissements légaux et politique de responsabilité
├── requirements.txt               # Dépendances requises du projet
├── image/
│   └── whitewolf.png              # Logo du projet
└── code/                          # Scripts fonctionnels unitaires
    ├── discordchecker.py          # Vérification de pseudos Discord à 4 caractères
    ├── tiktokchecker.py           # Vérification de pseudos TikTok à 4 caractères
    ├── githubchecker.py           # Vérification de pseudos GitHub à 4 caractères
    ├── ipscanner.py               # Scanner de ports TCP local (1–65535) via sockets
    ├── nukerdiscord.py            # Script d'administration/destruction de serveur Discord (WIP)
    ├── mrrobot.py                 # Script thématique interactif Mr. Robot
    ├── genip.py                   # Générateur et rapporteur d'IP aléatoires
    ├── Spamtlgrm.py               # Outil de spam automatisé via bot Telegram
    ├── passwordmanager.py         # Table de coffre-fort chiffrée (algorithme Fernet/AES)
    ├── letsenscript.py            # Outil de détection de version SSL/TLS
    ├── robloxsearch.py            # Lookup d'utilisateurs Roblox par ID via API
    ├── ai.py                      # Assistant virtuel propulsé par l'API Groq (OpenAI Client)
    ├── checking.py                # Scanner de comptes par e-mail (outil Holehe)
    ├── rpc.py                     # Configuration du Discord Rich Presence (RPC)
    ├── tokencheck.py              # Analyseur de jetons (tokens) Discord
    ├── embedsender.py             # Expéditeur d'embeds personnalisés sur webhook Discord
    ├── colors.py                  # Palettes de couleurs ANSI pour la CLI
    ├── ipreputation.py            # Évaluation de la réputation de sécurité d'une IP
    ├── autofollowinsta.py         # Script d'interaction robotisée Instagram (instagrapi)
    ├── ip.py                      # Lookup d'IP détaillé (localisation, FAI)
    ├── number.py                  # Lookup d'informations sur un numéro de téléphone
    ├── username.py                # Moteur de recherche de pseudonyme multi-sites
    ├── googlesearching.py         # Script d'assistance de recherche Google
    ├── dnslookup.py               # Outil de lookup d'abuse par nom de domaine
    ├── discord.py                 # Lookup de profils public Discord par identifiant
    ├── github.py                  # Info-collecteur de dépôts et profils GitHub
    ├── leak.py                    # Scanner de fuites de données de courriels (leakcheck.io)
    ├── archive.org                # Recherche de snapshots Wayback Machine
    ├── vpn.py                     # Gestionnaire de proxy Edge et isolation
    ├── password.py                # Générateur de mots de passe forts configurables
    ├── webstatus.py               # Mesure de latence et de code de réponse HTTP
    ├── scraper.py                 # Extraction des en-têtes HTTP bruts
    ├── whois.py                   # Analyseur complet WHOIS de nom de domaine
    ├── nitro.py                   # Générateur de liens de cadeaux Discord Nitro
    ├── webhookspaming.py          # Bombardement HTTP sur webhook Discord
    ├── idtotoken.py               # Outil générateur d'ébauches de tokens Discord par ID
    ├── invitbot.py                # Module d'invitation rapide de bots Discord administrateur
    ├── kylog.py                   # Enregistreur de touches clavier autonome
    ├── grabip.py                  # Récupérateur d'IP publique par service externe
    ├── screener.py                # Capture d'écran programmée
    ├── contributeur.py            # Récupérateur dynamique de contributeurs GitHub
    └── challange/                 # Répertoire des défis ludiques intégrés
        ├── firstchallange.py      # Défi OSINT axé géographie et observation
        ├── pentestchallange.py    # Défi d'introduction au Pentest d'applications web
        └── osint.png              # Image support pour le challenge OSINT
```

---

## 🗺️ Arbre des Commandes Interactif

Ci-dessous, la cartographie complète de l'interface utilisateur de `main.py` :

```
python main.py
│
├── [I] Informations ────────► Affiche les liens de contact (5s puis retour)
│
├── 1. [Lookup]
│   ├── [I] Informations
│   ├── 1.  [IP] ───────────────► Diagnostic d'IP (geo.ipify.org)
│   ├── 2.  [Number] ───────────► Informations de téléphones (apilayer.net)
│   ├── 3.  [Username] ─────────► Recherche de pseudo multi-sites (sites.py)
│   ├── 4.  [Google] ───────────► Automatisation de recherche Google
│   ├── 5.  [Dns] ──────────────► Abuse domain lookup (viewdns.info)
│   ├── 6.  [DISCORD] ──────────► Recherche d'utilisateur par ID (Vaultcord)
│   ├── 7.  [Github] ───────────► Statut & dernier commit public d'un profil/repo
│   ├── 8.  [Leak Mail] ────────► Vérification de piratage de mail (leakcheck.io)
│   ├── 9.  [Archive Web] ──────► Snapshots d'un domaine ou URL (archive.org)
│   ├── 10. [4C Tiktok] ────────► Moteur d'acquisition de pseudos TikTok @4carac
│   ├── 11. [4C Github] ────────► Recherche massive de pseudos GitHub libres
│   ├── 12. [IP Scanner] ───────► Analyseur de ports réseau ouverts (1-65535)
│   ├── 13. [SSL / TLS] ────────► Diagnostic de version cryptographique SSL/TLS
│   ├── 14. [Roblox] ───────────► Collecteur d'informations de joueur par ID
│   ├── 15. [AI] ───────────────► Assistant de discussion basé sur l'IA Groq
│   ├── 16. [Holehe] ───────────► Détection multi-sites de création de compte e-mail
│   └── 17. [Quit]
│
├── 2. [Sécurity]
│   ├── [I] Informations
│   ├── 1.  [PROXY(VPN)] ───────► Tunnel proxy Edge isolé (10s minimum)
│   ├── 2.  [Gen Password] ─────► Générateur de chaînes de mots de passe robustes
│   ├── 3.  [Status Website] ───► Vérification de code d'état HTTP et latence
│   ├── 4.  [Scraper] ──────────► Extraction d'en-têtes HTTP (result.txt)
│   ├── 5.  [Whois] ────────────► Données de registre WHOIS
│   ├── 6.  [Gen IP] ───────────► Émetteur d'IP aléatoires vers webhook
│   ├── 7.  [Spam Telegram] ────► Bot spammer de chat Telegram via API
│   ├── 8.  [Passwd Manager] ───► Coffre-fort de mots de passe durci (Fernet AES)
│   ├── 9.  [Osint] ────────────► Défi de géolocalisation OSINT (carte & heure)
│   ├── 10. [Pentest Web] ──────► Challenge d'introduction à la sécurité web
│   ├── 11. [Webcam] ───────────► Capture d'image caméra locale et dump webhook
│   ├── 12. [Ip reput] ─────────► Score de risques et de malveillance d'IP
│   └── 13. [Quit]
│
├── 3. [Discord]
│   ├── [I] Informations
│   ├── 1.  [Nitro Gen] ────────► Générateur brut de codes Nitro (nitro.txt)
│   ├── 2.  [Spaming Webhook] ──► Flot de requêtes HTTP sur webhook toutes les 5s
│   ├── 3.  [Darkweb] ──────────► Annuaire thématique de liens onion
│   ├── 4.  [Token BruteForce] ─► Générateur d'échantillons de tokens par ID
│   ├── 5.  [Bot to id] ────────► URL d'invitation de bot Administrateur (Scope 8)
│   ├── 6.  [4c Checker] ───────► Analyse de disponibilité de pseudos 4c Discord
│   ├── 7.  [rpc_conf] ─────────► Panneau de configuration du Rich Presence Discord
│   ├── 8.  [Token check] ──────► Inspecteur de validité et propriétaire de token
│   ├── 9.  [Webhook sender] ───► Générateur d'embeds élaborés sur webhook Discord
│   └── 10. [Quit]
│
├── 4. [Covid] (Menu Utilitaires / Trojan)
│   ├── 1.  [KeyLogger] ────────► Enregistrement clavier local vers webhook Discord
│   ├── 2.  [Grabing IP] ───────► Détection d'IP publique de la cible vers webhook
│   ├── 3.  [ScreenShot] ───────► Capture d'écran en tâche de fond vers webhook
│   ├── 4.  [Build Covid] ──────► Génération de l'exécutable obfusqué interactif
│   └── 5.  [Quit]
│
├── 5. [Automation]
│   ├── 1.  [Instagram Auto Follow] ► Automatisation d'interactions Instagram
│   └── 2.  [Quit]
│
├── 6. [Contributeur] ────────► Affichage dynamique des contributeurs du dépôt
│
└── 7. [Quit]
```

---

## 🔍 Détails Fonctionnels & Techniques

### 1. Lookup
Ensemble de scripts de recherche d'informations sur des cibles publiques ou privées.

| Nom de l'Outil | Fichier Source | Technologie / API | Rôle principal |
| :--- | :--- | :--- | :--- |
| **IP Lookup** | `code/ip.py` | [IPify](https://geo.ipify.org/) | Extraction de géolocalisation d'IP (Pays, ville, FAI, proxy/VPN). |
| **Phone Lookup** | `code/number.py` | [Apilayer](http://apilayer.net) | Obtention du pays et de l'opérateur d'un numéro international. |
| **Username Seek** | `code/username.py` | `sites.py` | Résolution de présence de pseudonymes sur plus de 30 plateformes web. |
| **DNS Lookup** | `code/dnslookup.py` | [ViewDNS](https://api.viewdns.info/) | Recherche d'adresses d'abus techniques sur un domaine. |
| **Discord Lookup**| `code/discord.py` | Vaultcord API | Lecture et extraction de données d'un profil par Identifiant Unique. |
| **GitHub Tracker** | `code/github.py` | GitHub REST API | Récupération des emails et détails du dernier commit de la cible. |
| **Email Leak** | `code/leak.py` | LeakCheck API | Identification de compromissions d'emails (enregistré en JSON). |
| **Wayback Machine**| `code/archive.py` | Wayback API | Récupération d'historiques de captures de pages web. |
| **4C Tiktok/Git** | `code/tiktokchecker.py`/`code/githubchecker.py` | Web Requests | Détection de pseudonymes disponibles à 4 lettres. |
| **IP Scanner** | `code/ipscanner.py` | Sockets (locales) | Identification des ports TCP ouverts (1 à 65535) en multi-thread. |
| **SSL/TLS Tool** | `code/letsenscript.py` | `ssl` & `socket` | Identification des versions de sécurité SSL/TLS acceptées. |
| **Roblox Lookup** | `code/robloxsearch.py`| Roblox API | Extraction de profils de jeux complexes à partir de l'ID. |
| **Holehe Lookup**  | `code/checking.py` | Holehe Engine | Scan asynchrone (trio/httpx) des comptes liés à un e-mail. |

---

### 2. Security
Défis interactifs d'apprentissage, chiffrement local et vérifications d'infrastructures.

*   **Proxy VPN (`code/vpn.py`)** : Ouvre une session Microsoft Edge sous environnement temporaire via un proxy HTTP passé en entrée. Mesure la persistance.
*   **Password Generator (`code/password.py`)** : Génère un mot de passe robuste basé sur les spécifications de sécurité standard de longueur personnalisable.
*   **Password Encrypter (`code/passwordmanager.py`)** : Coffre-fort cryptographique local utilisant la spécification **Fernet** (chiffrement symétrique AES 128 bits). Génère une clé de stockage `key.txt` et intègre un chiffrement/déchiffrement à la volée.
*   **Interactive Challenges (`code/challange/`)** :
    *   *OSINT Challenge* : Examine l'image `osint.png` pour répondre à des questions interactives (localisation, heure de prise, date exacte) et gagner des points.
    *   *Web Pentest Challenge* : Environnement ludique évaluant la capacité à détecter des failles de sécurité courantes.

---

### 3. Discord
Panoplie d'outils Discord à but de test d'intrusion, audit et notifications par webhook.

*   **Audit Webhook (`code/webhookspaming.py`, `code/embedsender.py`)** : Permet soit de bombarder un Webhook de requêtes à haute fréquence, soit de lui transmettre des enrichissements structurés (embeds) dotés d'images, de titres et de données.
*   **User Validity (`code/tokencheck.py`)** : Analyse la validité technique d'un token d'utilisateur Discord et extrait les informations associées (Pseudonyme, numéro de téléphone relié, adresse e-mail, abonnement Nitro ou non).

---

### 4. Trojan & Autostart (Covid / Stealer)
Le sous-menu **Covid** permet de configurer, tester et packager un compilateur de programmes malveillants à visée éducative.

> [!CAUTION]
> Les scripts de cette section collectent des données utilisateur sensibles en tâche de fond. Assurez-vous de mener ces audits sous un cadre strictement autorisé.

**Actions de `covid.py` au démarrage :**
1. **Extraction de Tokens Discord (`scanner.py`)** : Recherche et décryptage des jetons Discord enregistrés au sein des répertoires de navigateurs basés sur Chromium ou de l'application officielle d'arrière-plan.
2. **Reconnaissance Système** : Récupération de l'IP publique, listing récursif des fichiers utilisateur (`dir /s`) et envoi des données sur webhook.
3. **Persistance & Gofile** : Extraction et envoi de l'historique Google Chrome vers un hébergeur temporaire sécurisé (gofile.io).
4. **Keylogger & Screenshot** : Moteur asynchrone capturant continuellement les frappes de touches et l'affichage écran vers le webhook de contrôle.
5. **Builder (`builder.py`)** : Compresse, obfusque via **PyArmor** et encapsule l'entièreté de `covid.py` et ses modules dans un simple binaire Windows (`covid-exe/Tools.exe`) prêt à l'exécution.

---

## 🚀 Installation & Utilisation

### Prérequis
- Un interpréteur **Python 3.9+** fonctionnel.
- Droits Administrateurs sous Windows recommandés pour l'utilisation optimale de certains outils système.

### Procédure d'installation

```bash
# 1. Cloner le projet
git clone https://github.com/Python-loving/WHITEWOLF-TOOLS.git

# 2. Entrer dans le répertoire de travail
cd WHITEWOLF-TOOLS

# 3. Installer les dépendances tierces requises
pip install -r requirements.txt

# 4. Initialiser la structure d'API (obligatoire pour les scripts d'API)
python -c "import os; open('api.py', 'w').write('api_ip = \"\"\napi_number = \"\"\napi_dns = \"\"\n')"

# 5. Démarrer l'interface
python main.py
```

### Configuration des clés d'API

Le fichier `api.py` regroupe vos clés privées et ne doit pas faire l'objet de commits Git. Configurez vos jetons dans ce dernier :

```python
# api.py
api_ip = "VOTRE_CLE_GEO_IPIFY"
api_number = "VOTRE_CLE_APILAYER"
api_dns = "VOTRE_CLE_VIEWDNS"
```

---

## 🔒 Clause de Non-Responsabilité

Ce référentiel est fourni exclusivement à des fins d'éducation, de sensibilisation et d'audit de sécurité autorisé. Les auteurs et contributeurs déclinent toute responsabilité en cas d'utilisation abusive, de dommages causés par l'exécution de ces outils, ou de violation des conditions d'utilisation d'infrastructures tierces.

Veuillez consulter le document [`SECURITY.md`](SECURITY.md) pour de plus amples détails juridiques.

---

## 🤝 Équipe & Crédits
*   **Développeur Principal** : [xql](https://guns.lol/xqldev)
*   **Canal Telegram** : https://t.me/whitewolf_tools
*   **Contributeurs** : Affichés dynamiquement via l'option 6 du menu principal.

_Fait avec ❤️ par les membres de la meute WhiteWolf._
