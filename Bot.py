import requests
import re

TARGET_URL = "https://t.me/s/Vipper_v2ray"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def son_operasyon():
    try:
        r = requests.get(TARGET_URL, headers=HEADERS, timeout=30)
        # Sadece vless, vmess, ss linklerini cımbızla çek
        kodlar = re.findall(r'(?:vless|vmess|ss|trojan)://[^\s<>"]+', r.text)
        
        # Dosyayı her zaman oluştur ki GitHub "dosya yok" diye hata vermesin
        with open("abone.txt", "w", encoding="utf-8") as f:
            if kodlar:
                f.write("\n".join(list(set(kodlar))))
                print(f"Basarili! {len(kodlar)} kod bulundu.")
            else:
                f.write("Su an taze kod yok, bekleniyor...")
                print("Kod bulunamadi ama dosya guncellendi.")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    son_operasyon()
    
