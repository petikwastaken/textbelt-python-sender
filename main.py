print("Warming up...")
#defining functions and updating pip to make sure that extensions that will be imported afteward will work properly
import os
os.system('python -m pip install --upgrade pip')
os.system('pip install requests')
os.system('pip3 install requests')
import requests
import time as t
import random
def cls():
    os.system('cls')
print("READY")


cls()
print("   _____ __  __  _____    _____ ______ _   _ _____  ")
print("  / ____|  \/  |/ ____|  / ____|  ____| \ | |  __ \ ")
print(" | (___ | \  / | (___   | (___ | |__  |  \| | |  | |")
print("  \___ \| |\/| |\___ \   \___ \|  __| | . ` | |  | |")
print("  ____) | |  | |____) |  ____) | |____| |\  | |__| |")
print(" |_____/|_|  |_|_____/  |_____/|______|_| \_|_____/ ")
print("")
print("")


phone = input('Type in receiver number(Ex.:+420123456789): ')
cls()

msg = input('Type in your message you would like to send to the receiver or type "00" to change the receiver' + "'s number: ")
if(msg == "00"):
    while(msg == "00"):
        phone = input('Type in receiver number: ')
        cls()
        msg = input('Type in your MESSAGE you would like to send to the receiver or type "00" to change the receiver' + "'s number: ")
    

    msgChange = input('Wanna change the message? (Enter for NO): ')
    if(not msgChange == ""):
         msg = msgChange

else:
    msgChange = input('Wanna change the message? (Enter for NO): ')
    if(not msgChange == ""):
         msg = msgChange
cls()


confirm = random.randint(1000,10000)
print('Type in', confirm, 'to confirm SENDING.')
confirmUsr = int(input())

while(not confirm == int(confirmUsr)):
    confirm = random.randint(1000,10000)
    print('Type in', confirm, 'to confirm SENDING.')
    confirmUsr = int(input())

if(confirm == int(confirmUsr)):
    print("sending...")
    resp = requests.post('https://textbelt.com/text', {
    'phone': phone,
    'message': msg,
    'key': 'textbelt',
    })
    respDebug = resp.json()
    resp = str(resp.json())
    resp = resp.split(' ')
    resp = resp[1].split(',')
    if(resp[0] == "True"):
        print("Message sent SUCCESSfully")
    else:
        print("Something went wrong...")
        print(respDebug)
input('Press ENTER to EXIT')