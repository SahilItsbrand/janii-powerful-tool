# coding: utf-8

# Banaya By: Janii Bhai (Teri Demand, Mera Upgrade)
# Purpose: Powerful random phone data generator aur API tester – countries add kiye!
# Disclaimer: Educational only, no illegal use!

import os, sys, time, random, threading, json, requests
from multiprocessing.pool import ThreadPool

# Terminal saaf
os.system('clear' if os.name == 'posix' else 'cls')

__author__ = 'Janii Bhai'
__copyright__ = 'Dil Se Upgrade, Copyright 2025'

CorrectKey = 'janii420'

loop = 'true'
while loop == 'true':
    key = input('\033[1;91m🔥 TOOL KEY DALO……=>> :\033[1;93m ')
    if key == CorrectKey:
        print('\033[1;92m✅ Login Successful, Janii Bhai!')
        time.sleep(1)
        os.system('xdg-open https://youtube.com/@janii420' if os.name == 'posix' else 'start https://youtube.com/@janii420')
        os.system('clear' if os.name == 'posix' else 'cls')
        loop = 'false'
    else:
        print('\033[1;93m❌ Wrong Key, Try Again!')
        os.system('xdg-open https://youtube.com/@janii420' if os.name == 'posix' else 'start https://youtube.com/@janii420')
        os.system('clear' if os.name == 'posix' else 'cls')

# Zyada powerful: 100,000 numbers!
if os.path.exists('.numbers.txt'):
    os.remove('.numbers.txt')

for _ in range(100000):
    nmbr = random.randint(1000000, 9999999)  # 7 digits, can adjust per country
    with open('.numbers.txt', 'a') as f:
        f.write(str(nmbr) + '\n')

try:
    import requests
except ImportError:
    os.system('pip install requests')

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'
}

def jalan(text):
    for char in text + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

def tik():
    dots = ['   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for dot in dots:
        print(f'\r\033[1;96m🔥 Loading Powerful Mode{dot}', end='')
        sys.stdout.flush()
        time.sleep(0.3)

logo = """
\033[1;94m========================================
       JANII BHAI KA POWERFUL DATA TOOL
========================================
 Author   : Janii Bhai
 Version  : 2.0 (Global Edition)
 Youtube  : youtube.com/@janii420
========================================
"""

logo1 = """
\033[1;94mCOUNTRY CHUNO AUR PREFIXES
\033[1;96m[1] Pakistan \033[1;97m +92300-349 (Jazz:00-09, Zong:10-19, Warid:20-29, Ufone:30-39, Telenor:40-49)
\033[1;96m[2] India    \033[1;97m +917, +918, +919 (Common mobile starts)
\033[1;96m[3] UK       \033[1;97m +4474, +4475, +4477, +4478, +4479
\033[1;96m[4] USA      \033[1;97m +1201, +1202, +1305, +1310, +1408 (Common area codes)
\033[1;96m[5] Japan    \033[1;97m +8170, +8180, +8190
\033[1;96m[6] Singapore\033[1;97m +658, +659
\033[1;96m[7] Custom   \033[1;97m Apna Code Daal (+country_prefix)
"""

hit = []
miss = []

def menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(logo)
    print(47 * '-')
    jalan('\033[1;96m[1] Start Powerful Number Testing/Cloning')
    jalan('\033[1;96m[0] Exit Tool')
    print(47 * '-')
    action()

def action():
    global hit, miss
    choice = input('\033[1;96mOption: ')
    
    if choice == '1':
        tik()
        os.system('clear' if os.name == 'posix' else 'cls')
        print(logo)
        print(logo1)
        country_choice = input('\033[1;97mCountry Number Daal (1-7): ')
        
        if country_choice == '1':  # Pakistan
            country_prefix = '+92'
            k = '3'
            c = input('\033[1;97mPrefix Code (00-49): ')
        elif country_choice == '2':  # India
            country_prefix = '+91'
            k = ''
            c = input('\033[1;97mPrefix (7,8,9): ')
        elif country_choice == '3':  # UK
            country_prefix = '+44'
            k = ''
            c = input('\033[1;97mPrefix (74,75,77,78,79): ')
        elif country_choice == '4':  # USA
            country_prefix = '+1'
            k = ''
            c = input('\033[1;97mArea Code (201,202,305,310,408): ')
        elif country_choice == '5':  # Japan
            country_prefix = '+81'
            k = ''
            c = input('\033[1;97mPrefix (70,80,90): ')
        elif country_choice == '6':  # Singapore
            country_prefix = '+65'
            k = ''
            c = input('\033[1;97mPrefix (8,9): ')
        elif country_choice == '7':  # Custom
            country_prefix = input('\033[1;97mCustom Country Code (+xx): ')
            k = ''
            c = input('\033[1;97mCustom Prefix: ')
        else:
            print('\033[1;91m[!] Galat Choice!')
            action()
        
        idlist = '.numbers.txt'
        try:
            with open(idlist, 'r') as f:
                id = [line.strip() for line in f]
        except IOError:
            print('\033[1;91m[!] File Not Found')
            input('\n[ Back ]')
            menu()
        
        os.system('clear' if os.name == 'posix' else 'cls')
        print(logo)
        jalan('\033[1;97mTesting Shuru, Powerful Mode Mein!')
        print(47 * '-')
        jalan(f'\033[1;97mTotal IDs: \033[1;95m{len(id)}')
        print(47 * '-')

        def test_number(number):
            try:
                full_number = country_prefix + k + c + number
                # Mock API for ethical testing (replace with real if needed)
                url = f'https://api.example.com/test?phone={full_number}'
                response = requests.get(url, headers=headers, timeout=5)
                data = response.json()
                
                # Powerful: Zyada checks (mock passwords)
                passwords = [number, country_prefix.split('+')[1], '123456', 'password', 'letmein']
                for passw in passwords:
                    if random.random() > 0.95:  # Mock success for demo
                        print(f'\033[1;92m[Hit] {full_number} | Pass: {passw}')
                        with open('save/hit.txt', 'a') as f:
                            f.write(f'{full_number} | {passw}\n')
                        hit.append(full_number)
                        break
                else:
                    print(f'\033[1;91m[Miss] {full_number}')
                    with open('save/miss.txt', 'a') as f:
                        f.write(f'{full_number}\n')
                    miss.append(full_number)
            except Exception:
                pass

        os.makedirs('save', exist_ok=True)
        
        # Powerful: 50 threads!
        with ThreadPool(50) as pool:
            pool.map(test_number, id)
        
        print(48 * '-')
        print('Kaam Khatam!')
        print(f'Total Hits: {len(hit)}')
        print(f'Total Miss: {len(miss)}')
        print(47 * '-')
        jalan('Results in save/hit.txt and save/miss.txt')
        input('\n\033[1;95m[Enter for Menu]')
        menu()
    
    elif choice == '0':
        print('\033[1;91m[!] Bye!')
        sys.exit()
    
    else:
        print('\033[1;91m[!] Wrong!')
        action()

if __name__ == '__main__':
    menu()
