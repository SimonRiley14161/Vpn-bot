import requests
import re

URLS = [
    "https://tmstart.me/serverstm7",
    "https://tmstart.me/Kanal45",
    "https://tmstart.me/Kanal91",
    "https://tmstart.me/kanal67",
    "https://tmstart.me/swech_servers",
    "https://tmstart.me/kaktus",
    "https://tmstart.me/OctoS",
    "https://tmstart.me/VPNShield"
]

def vpn_topla():
    butun_keyler = set()
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    for url in URLS:
        try:
            r = requests.get(url, headers=headers, timeout=15)
            if r.status_code == 200:
                bulunanlar = re.findall(r'(?:vless|vmess|ss|trojan)://[^\s<>"]+', r.text)
                butun_keyler.update(bulunanlar)
        except:
            continue
            
    with open("abone.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(list(butun_keyler)))
    
    print(f"Islem Tamam: {len(butun_keyler)} config bulundu.")

if __name__ == "__main__":
    vpn_topla()
    
