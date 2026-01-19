import requests
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

# Senin seçtiğin o 8 kanal (Web arayüzü üzerinden tarayacağız)
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

def vpn_supur():
    butun_bulunanlar = set()
    print("Süpürme operasyonu başladı...")
    
    for url in URLS:
        try:
            # Kanala gidip tüm metni çekiyoruz
            r = requests.get(url, headers=HEADERS, timeout=15)
            if r.status_code == 200:
                # Regex ile vless, vmess, ss, trojan ne varsa ayıklıyoruz
                pattern = r'(?:vless|vmess|ss|trojan)://[^\s<>"]+'
                linkler = re.findall(pattern, r.text)
                
                if linkler:
                    print(f"Buldum! {url} -> {len(linkler)} tane.")
                    butun_bulunanlar.update(linkler)
                else:
                    print(f"İçerik yok: {url}")
        except Exception as e:
            print(f"Bağlantı sorunu: {url} -> {e}")

    # Eğer 1 tane bile bir şey bulduysan dosyaya yaz
    if butun_bulunanlar:
        with open("abone.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(list(butun_supur))) # Set'i listeye çevirip alt alta yaz
        print(f"Tamamdır! Toplam {len(butun_bulunanlar)} config ile abone.txt dolduruldu.")
    else:
        # Eğer hiçbir şey bulamazsa dosyayı silme, içine hata yaz ki anlayalım
        with open("abone.txt", "w", encoding="utf-8") as f:
            f.write("BOT CALISTI AMA LINK BULAMADI. KANALLARI KONTROL ET.")

if __name__ == "__main__":
    vpn_supur()
        
