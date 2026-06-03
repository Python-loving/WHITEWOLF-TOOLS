# WhiteWolf Tools

<small>For README is ai make sorry :)</small>

Suite d’outils en ligne de commande (CLI) pour **OSINT**, **sécurité**, **Discord** et utilitaires divers. Interface en menus ASCII — lance tout depuis `main.py`.

> **Python requis** — Windows recommandé (certaines fonctions utilisent `msvcrt`, Edge, `taskkill`).

---

## Structure du projet

```
tools/
├── main.py              # Point d’entrée — menus et toute la logique interactive
├── api.py               # Clés API (ipify, apilayer, viewdns)
├── sites.py             # Plateformes pour le lookup username
├── darkweb.py           # Liens .onion par catégorie (menu Discord → Darkweb)
├── covid.py             # Module autonome (keylogger + grab IP) — build exe prévu
└── README.MD
```

---

## Arbre des commandes (`main.py`)

```
python main.py
│
├── [I] Informations ─────────► Telegram, Guns.lol (5 s puis retour)
│
├── 1. LOOKUP
│   ├── [I] Informations
│   ├── 1. IP ──────────────────► geo.ipify.org (pays, ville, ISP, VPN)
│   ├── 2. Number ──────────────► apilayer.net (pays, format, opérateur)
│   ├── 3. Username ────────────► scan multi-sites (sites.py)
│   ├── 4. Google ──────────────► ouvre la recherche dans le navigateur
│   ├── 5. DNS ─────────────────► viewdns.info (abuse contact)
│   ├── 6. Discord ─────────────► vaultcord (profil par ID)
│   ├── 7. Github ──────────────► dernier commit public (email auteur, etc.)
│   ├── 8. Leak Mail ───────────► leakcheck.io → result.json
│   ├── 9. Archive Web ───────────► archive.org → (Affiche les archive des site etc.)
│   └── 10. Quit
│
├── 2. SECURITY
│   ├── [I] Informations
│   ├── 1. PROXY (VPN) ─────────► Edge + proxy HTTP (durée min. 10 s)
│   ├── 2. Gen Password ────────► mot de passe aléatoire (min. 10 car.)
│   ├── 3. Status Website ──────► temps de réponse HTTP (ms)
│   ├── 4. Scraper ─────────────► en-têtes HTTP → result.txt
│   └── 5. Quit
│
├── 3. DISCORD
│   ├── [I] Informations
│   ├── 1. Nitro Gen ───────────► codes gift aléatoires → nitro.txt si valide
│   ├── 2. Spaming Webhook ─────► POST en boucle (toutes les 5 s)
│   ├── 3. Darkweb ─────────────► affiche les liens (darkweb.py)
│   ├── 4. Token BruteForce ────► génère un token factice depuis un ID
│   ├── 5. Bot to id ───────────► URL d’invitation OAuth2 (permissions 8)
│   └── 6. Quit
│
├── 4. COVID (menu utilitaires)
│   ├── 1. KeyLogger ───────────► frappe clavier → webhook Discord
│   ├── 2. Grabing IP ──────────► IP publique → webhook Discord
│   └── 3. Quit
│
└── 5. Quit (accueil)
```

**Raccourci global :** `[I]` ou `[i]` sur chaque sous-menu → `show_informations()`.

---

## Détail des fonctionnalités

### Lookup (1)

| Choix | Entrée | API / source | Sortie |
|-------|--------|--------------|--------|
| IP | Adresse IP | [ipify](https://geo.ipify.org) | IP, pays, ville, ISP |
| Number | Numéro E.164 | [apilayer](http://apilayer.net) | Pays, formats, carrier |
| Username | Pseudo | 30+ sites (`sites.py`) | URLs où le profil répond 200 |
| Google | Requête | Navigateur système | Onglet Google Search |
| DNS | Domaine | [viewdns](https://api.viewdns.info) | Abuse contact |
| Discord | ID utilisateur | vaultcord.com | username, avatar, flags, clan… |
| Github | user + repo | api.github.com | email/nom/date du dernier commit |
| Leak Mail | Email | leakcheck.io | `result.json` |

**Sites username** (extrait) : GitHub, Reddit, TikTok, Instagram, X, Facebook, Twitch, Steam, GitLab, Medium, Roblox, Chess.com, Linktree, Gravatar… — liste complète dans `sites.py`.

### Security (2)

| Choix | Description |
|-------|-------------|
| PROXY (VPN) | Lance Microsoft Edge avec `--proxy-server`, vérifie l’IP via ipify, arrêt au timeout ou touche clavier |
| Gen Password | `ascii_letters` + `digits` + `punctuation`, longueur ≥ 10 |
| Status Website | `GET` sur l’URL → délai en millisecondes |
| Scraper | `HEAD` → affiche et enregistre les headers dans `result.txt` |

### Discord (3)

| Choix | Description | Fichier généré |
|-------|-------------|----------------|
| Nitro Gen | Teste `https://discord.gift/{16 chars}` en boucle | `nitro.txt` |
| Spaming Webhook | Envoie `{ "content": message }` en POST | — |
| Darkweb | Liste par catégorie (moteurs, marchés, wikis…) | — |
| Token BruteForce | `base64(user_id).random.random` (démo, non fonctionnel réel) | — |
| Bot to id | Lien `oauth2/authorize` admin (perm 8) | — |

**Catégories Darkweb** (`darkweb.py`) : Search Engine, Bitcoin Anonymity, DDoS, Market, Cooks, Torrents, Social Media, Wikis, Government, Communities, Educational.

### Covid (4)

| Choix | Description |
|-------|-------------|
| KeyLogger | `pynput` → chaque touche postée sur un webhook |
| Grabing IP | IP via `checkip.amazonaws.com` → webhook |

> Le fichier `covid.py` reprend la même logique en **script autonome** (IP d’abord, puis keylogger) — prévu pour une future version `.exe`.

---

## Installation

```bash
cd tools
pip install requests pynput
python main.py
```

| Package | Usage |
|---------|--------|
| `requests` | Toutes les requêtes HTTP |
| `pynput` | KeyLogger (menu Covid + `covid.py`) |

Modules standard : `os`, `time`, `json`, `webbrowser`, `msvcrt`, `tempfile`, `subprocess`, `random`, `string`, `base64`.

---

## Configuration API (`api.py`)

Certaines commandes **Lookup** nécessitent des clés dans `api.py` :

| Variable | Service | Utilisé pour |
|----------|---------|--------------|
| `api_ip` | [geo.ipify.org](https://geo.ipify.org) | Lookup IP |
| `api_number` | [apilayer.net](http://apilayer.net) | Lookup téléphone |
| `api_dns` | [api.viewdns.info](https://api.viewdns.info) | Lookup DNS / abuse |

Remplace les valeurs par **tes propres clés** — ne commite jamais de secrets en public.

Les autres lookups (Discord, Github, Leak Mail, Google) n’utilisent pas `api.py`.

---

## Fichiers générés à l’exécution

| Fichier | Créé par |
|---------|----------|
| `result.json` | Lookup → Leak Mail |
| `result.txt` | Security → Scraper |
| `nitro.txt` | Discord → Nitro Gen (codes potentiellement valides) |

---

## Liens & crédits

- **Telegram** — https://t.me/whitewolf_tools  
- **Guns.lol** — https://guns.lol/xqldev  

---

## Avertissement

Utilise ces outils uniquement sur des systèmes et des données **dont tu as l’autorisation**. Les fonctions type keylogger, spam webhook ou génération de tokens peuvent violer les lois et les conditions d’utilisation des services concernés.

---

*Love My friends :)* — *Don’t wait, just do it :)*
