import requests
import re

# SENİN VERDİĞİN TÜM KANALLAR
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
            r = requests.get(url, timeout=15)
            # 1. Normal kodları bul (vless, vmess vb.)
            bulunanlar = re.findall(r'(?:vless|vmess|ss|trojan)://[^\s<>"]+', r.text)
            for k in bulunanlar:
                butun_keyler.add(k)
            
            # 2. GİZLİ ABONELİK LİNKLERİNİ BUL (Happcrypt avcısı)
            # Mesajların içinde .txt ile biten veya /sub/ içeren linkleri arar
            gizli_linkler = re.findall(r'https?://[^\s<>"]+(?:\.txt|/sub/[^\s<>"]+)', r.text)
            for link in gizli_linkler:
                if "SimonRiley14161" in link: continue # Kendi linkini atla
                try:
                    sub_r = requests.get(link, timeout=10)
                    sub_keyler = re.findall(r'(?:vless|vmess|ss|trojan)://[^\s<>"]+', sub_r.text)
                    for sk in sub_keyler:
                        butun_keyler.add(sk)
                except:
                    continue
        except:
            continue
            
    # Dosyaya kaydet
    with open("abonelik.txt", "w") as f:
        f.write("\n".join(butun_keyler))

if __name__ == "__main__":
    vpn_topla()
        
