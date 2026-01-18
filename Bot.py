import requests
import re

# SENİN KANALLARIN
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
    
    for url in URLS:
        try:
            # Sayfayı indir
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                # vless, vmess, ss ve trojan kodlarını ayıkla
                bulunanlar = re.findall(r'(?:vless|vmess|ss|trojan)://[^\s<>"]+', r.text)
                for k in bulunanlar:
                    butun_keyler.add(k)
        except:
            continue
            
    # Sonuçları abonelik.txt dosyasına yaz
    with open("abonelik.txt", "w") as f:
        f.write("\n".join(butun_keyler))
    
    print(f"Bitti! {len(butun_keyler)} tane VPN bulundu.")

if __name__ == "__main__":
    vpn_topla()
    
