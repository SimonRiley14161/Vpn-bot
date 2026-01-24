import requests
import re
import base64

URL = "https://t.me/s/Vipper_v2ray"
HEADERS = {"User-Agent": "Mozilla/5.0"}

r = requests.get(URL, headers=HEADERS, timeout=20)
html = r.text

configs = re.findall(
    r'(vmess|vless|trojan|ss)://[a-zA-Z0-9+/=._%-]+',
    html
)

configs = list(set(configs))

if not configs:
    exit()

joined = "\n".join(configs)
sub = base64.b64encode(joined.encode()).decode()

with open("sub.txt", "w") as f:
    f.write(sub)
