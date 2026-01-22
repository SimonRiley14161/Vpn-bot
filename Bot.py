import requests
import re
from datetime import datetime

# Hedef kanal ve ayarlar
TARGET_URL = "https://t.me/s/Vipper_v2ray"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def son_gun_avi():
    bulunan_kodlar = []
    print(f"{TARGET_URL} taranıyor... Sandman için son operasyon.")

    try:
        r = requests.get(TARGET_URL, headers=HEADERS, timeout=20)
        if r.status_code == 200:
            # Telegram'ın web görünümündeki her bir mesaj bloğunu ayırıyoruz
            mesajlar = re.findall(r'<div class="tgme_widget_message_text[^>]*>(.*?)</div>', r.text, re.DOTALL)
            
            for mesaj in mesajlar:
                # vless, vmess, ss, trojan kodlarını ara
                linkler = re.findall(r'(?:vless|vmess|ss|trojan)://[^\s<>"]+', mesaj)
                if linkler:
                    bulunan_kodlar.extend(linkler)
            
            # Tekrar edenleri temizle
            bulunan_kodlar = list(set(bulunan_kodlar))
            
            if bulunan_kodlar:
                with open("abone.txt", "w", encoding="utf-8") as f:
                    f.write("\n".join(bulunan_kodlar))
                print(f"Başarılı! {len(bulunan_kodlar)} adet taze config toplandı.")
            else:
                print("Maalesef, son mesajlarda uygun formatta kod bulunamadı.")
                with open("abone.txt", "w", encoding="utf-8") as f:
                    f.write("Sandman: Kanalda son 1 gün içinde config bulunamadı.")
        else:
            print(f"Kanala erişilemedi. Hata kodu: {r.status_code}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    son_gun_avi()
            
