import requests, os
import socket
from time import sleep
ip=socket.gethostbyname(socket.gethostname())
th='- - - - - - - - - - - - - - - - - - - - - - - - -'
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
id=input('Nhập id người cần gửi: ')
while True:
    ck=input('Nhập cookie facebook: ')
    try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={id}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        break
    except:
        print('Cookie sai!!')
    


nd=input('Nhập nội dung: ')
so_luong=int(input('Nhập số tin nhắn muốn gửi: '))
delay=int(input('Nhập delay: '))
headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
    # Requests sorts cookies= alphabetically
    'cookie': ck,
    'origin': 'https://m.facebook.com',
    'referer': 'https://www.facebook.com',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',
}

params = {
    'icm': '1',
}

data = {
    f'ids[{id}]': id,
    'body': nd,
    'waterfall_source': 'message',
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
}
for i in range(1,so_luong+1):
    response = requests.post('https://m.facebook.com/messages/send/', params=params, headers=headers, data=data)
    print(f'gửi thành công {i}')
    sleep(delay)
