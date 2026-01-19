import requests
import re

# Tarayıcı gibi görünmek için "User-Agent" ekledik
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

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
    print("Operasyon basladi...")
    
    for url in URLS:
        try:
            # Zaman asimini 20 saniyeye cikardik ve HEADERS ekledik
            r = requests.get(url, headers=HEADERS, timeout=20)
            if r.status_code == 200:
                # Daha kapsamli bir arama yapalim
                bulunanlar = re.findall(r'(?:vless|vmess|ss|trojan)://[^\s<>"]+', r.text)
                if bulunanlar:
                    print(f"Buldum: {url} -> {len(bulunanlar)} adet")
                    butun_keyler.update(bulunanlar)
                else:
                    print(f"Bos: {url}")
            else:
                print(f"Hata Kodu {r.status_code}: {url}")
        except Exception as e:
            print(f"Baglanti Hatasi: {url} -> {e}")
            
    # Sonucu dosyaya zorla yazdiriyoruz
    if butun_keyler:
        with open("abone.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(list(butun_keyler)))
        print(f"Basarili! Toplam {len(butun_keyler)} config kaydedildi.")
    else:
        print("Hic config bulunamadi, dosya guncellenmedi.")

if __name__ == "__main__":
    vpn_topla()
        
