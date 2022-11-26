print("Warming up...")
import os
os.system('python -m pip install --upgrade pip')
os.system('pip install requests')
os.system('pip3 install requests')
import requests
import time as t
import random
def cls():
    os.system('cls')
confirm = random.randint(1,10000)
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
phone = input('Type in receiver number:')
cls()
msg = input('Type in your message you would like to send to the receiver or type in "00" to change the receiver' + "'s number: ")
if(msg == "00"):
    while(msg == "00"):
        phone = input('Type in receiver number:')
        cls()
        msg = input('Type in your message you would like to send to the receiver or type in "00" to change the receiver' + "'s number: ")
    
    msgChange = input('Wanna change the message? (Enter for NO):')
    if(not msgChange == ""):
         msg = msgChange
else:
    msgChange = input('Wanna change the message? (Enter for NO):')
    if(not msgChange == ""):
         msg = msgChange
cls()
print('Type in', confirm, 'to confirm SENDING.')
if(confirm == int(input())):
    print("sending...")
input()