from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv("account_lz.env")
USER = os.getenv("USER")
PAWD = os.getenv("PAWD")
WMAC = os.getenv("WMAC")
ACIP = os.getenv("ACIP")
print(USER, PAWD,WMAC, ACIP)
URL1 = (
    f"http://10.10.8.162:801/eportal/portal/login?callback=dr1004&login_method=1&"
    f"user_account=%2C0%2C{USER}&user_password={PAWD}&wlan_user_ip=180.85.217.79&"
    f"wlan_user_ipv6=&wlan_user_mac={WMAC}&wlan_ac_ip={ACIP}&wlan_ac_name=&"
    f"jsVersion=4.2.2&terminal_type=0&lang=zh-cn&v=1127&lang=zh"
)


response = requests.get(URL1)


print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {response.text}")
