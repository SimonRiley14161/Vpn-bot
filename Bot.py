import requests
import re

# Taranacak kanal linkleri
URLS = [
    "https://tmstart.me/serverstm7"
]

def vpn_topla():
    butun_keyler = []
    for url in URLS:
        try:
            # GitHub sunucusu yurt dışında olduğu için siteye erişir
            r = requests.get(url, timeout=15)
            # vless, vmess, trojan ve ss linklerini bulur
            bulunanlar = re.findall(r'(vless|vmess|trojan|ss)://[^\s<"\'&]+', r.text)
            butun_keyler.extend(bulunanlar)
        except:
            continue
    
    # Tekrar edenleri temizle
    temiz_liste = list(set(butun_keyler))
    
    # Dosyaya kaydet
    with open("abonelik.txt", "w") as f:
        f.write("\n".join(temiz_liste))

if __name__ == "__main__":
    vpn_topla()
