import requests
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

# Senin seçtiğin kanalların web önizleme linkleri
URLS = [
    "https://t.me/s/serverstm7",
    "https://t.me/s/Kanal45",
    "https://t.me/s/Kanal91",
    "https://t.me/s/kanal67",
    "https://t.me/s/swech_servers",
    "https://t.me/s/kaktus",
    "https://t.me/s/OctoS",
    "https://t.me/s/VPNShield"
]

def vpn_topla():
    butun_listeler = set()
    print("Süpürme operasyonu başladı...")
    
    for url in URLS:
        try:
            # Kanala gidip tüm metni çekiyoruz
            r = requests.get(url, headers=HEADERS, timeout=15)
            if r.status_code == 200:
                # Regex ile vless, vmess, ss ne varsa ayıklıyoruz
                bulunanlar = re.findall(r'(?:vless|vmess|ss|trojan)://[^\s<>"]+', r.text)
                if bulunanlar:
                    print(f"Buldum: {url} -> {len(bulunanlar)} adet")
                    butun_listeler.update(bulunanlar)
        except:
            continue
            
    if butun_listeler:
        with open("abone.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(list(butun_listeler)))
        print(f"Başarılı! Toplam {len(butun_listeler)} config kaydedildi.")
    else:
        # Eğer hiçbir şey bulamazsa dosyayı boşaltma, içine not yaz
        with open("abone.txt", "w", encoding="utf-8") as f:
            f.write("Test Modu: Su an kanallarda taze link bulunamadi.")

if __name__ == "__main__":
    vpn_topla()
    
