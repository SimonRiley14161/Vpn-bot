import requests
import re

# Start Messenger'ın web servisi bazen botlara karşı hassas olabilir, o yüzden sağlam bir kafa (headers) takıyoruz.
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

# Senin Start Messenger kanallarının asıl linkleri
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

def start_messenger_avi():
    bulunan_kodlar = set()
    print("Start Messenger kanalları taranıyor...")

    for url in URLS:
        try:
            # Botu doğrudan bu kanalın web sayfasına gönderiyoruz
            r = requests.get(url, headers=HEADERS, timeout=20)
            if r.status_code == 200:
                # Kanaldaki vless, vmess, ss gibi kodları ayıklıyoruz
                pattern = r'(?:vless|vmess|ss|trojan)://[^\s<>"]+'
                bulunanlar = re.findall(pattern, r.text)
                
                if bulunanlar:
                    print(f"Buldum! {url} adresinden {len(bulunanlar)} config çekildi.")
                    bulunan_kodlar.update(bulunanlar)
                else:
                    print(f"Kod bulunamadı: {url}")
        except Exception as e:
            print(f"Bağlantı kesildi: {url} -> {e}")

    # Sonucu dosyaya yazıyoruz
    if bulunan_kodlar:
        with open("abone.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(list(bulunan_kodlar)))
        print(f"Operasyon Tamam! {len(bulunan_kodlar)} adet VPN kodu kaydedildi.")
    else:
        with open("abone.txt", "w", encoding="utf-8") as f:
            f.write("SISTEM BAGLANDI: Start Messenger kanalinda su an yeni kod yok.")

if __name__ == "__main__":
    start_messenger_avi()
    
