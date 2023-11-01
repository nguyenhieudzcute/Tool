import requests as C
import os
import time

def clear():
    os.system('clear')

clear()

print('''
\033[32;5;245m\033[1m\033[38;5;39m </> thắc mắc gì thì liên hệ admin nguyên blue nha! </>

\033[1;37m──────────────────────────────────────────────────────────── 
\033[1;35m___ADMIN___\033[1;36mNguyên blue
\033[1;31m___messenger___\033[1;33mhttps://m.me/nguyenblue2007
\033[38;5;39m___FACEBOOK___\033[1;37https://facebook.com/nguyenblue2007
\033[1;37m────────────────────────────────────────────────────────────\n''')

import urllib.request
import http.client

def check_key():
    conn = http.client.HTTPSConnection("raw.githubusercontent.com")
    conn.request("GET", "/diokn2007/Tool/main/Keytool.txt")
    key_tool = conn.getresponse().read().decode('utf-8').strip()

    if key_tool == "":
        print("Không cần nhập key. Chúc bạn ngày mới tốt lành!")
        return True

    while True:
        nhap_key = input("Vui lòng nhập key: ")
        if nhap_key == key_tool:
            print("Key chính xác. Chúc bạn ngày tốt lành!")
            return True
        else:
            print("Key sai. Vui lòng nhập lại key")

if not check_key():
    exit()


id = input('Nhập id group cần gửi: ')
while True:
    cookie = input('Nhập cookie Facebook: ')
    try:
        response = C.get(f"https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={id}&ret_cancel&source=profile", headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': cookie,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg = response.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest = response.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        os.system('clear')
        break
    except:
        print('Cookie sai!!')

clear()

message = input('Nhập nội dung tin nhắn: ')
quantity = int(input('Số lượng tin nhắn: '))
delay = float(input('Delay: '))

os.system('clear')

params = {'icm': '1'}

headers = {
    'Host': 'mbasic.facebook.com',
    'content-length': '247',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': cookie,
}

for i in range(quantity):
    data = {
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'body': message,
        'send': 'Send',
        'tids': f'cid.g.{id}',
        'wwwupp': 'C3',
        'platform_xmd': '',
        'referrer': '',
        'ctype': '',
        'cver': 'legacy',
        'csid': '366a74a7-2d30-45dd-94c2-ad47d662dcfb'
    }
    response = C.post('https://mbasic.facebook.com/messages/send/', params=params, headers=headers, data=data)
    print(f'Gửi thành công {i+1}')
    time.sleep(delay)

