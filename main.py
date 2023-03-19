import random
import time
import os
import requests
import colorama 
from colorama import Fore

colorama.init()

def slowtype(txt):
   for x in txt:
     print(x,end="",flush =True)
     time.sleep(0.08)

os.system('TITLE Rinck#0001 » Rinck-Nitro-Generator - Release 2.0.0')

print(f"""{Fore.LIGHTBLUE_EX}██████╗ ██╗███╗   ██╗ ██████╗██╗  ██╗ ██╗ ██╗  ██████╗  ██████╗  ██████╗  ██╗
██╔══██╗██║████╗  ██║██╔════╝██║ ██╔╝████████╗██╔═████╗██╔═████╗██╔═████╗███║
██████╔╝██║██╔██╗ ██║██║     █████╔╝ ╚██╔═██╔╝██║██╔██║██║██╔██║██║██╔██║╚██║
██╔══██╗██║██║╚██╗██║██║     ██╔═██╗ ████████╗████╔╝██║████╔╝██║████╔╝██║ ██║
██║  ██║██║██║ ╚████║╚██████╗██║  ██╗╚██╔═██╔╝╚██████╔╝╚██████╔╝╚██████╔╝ ██║
╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═════╝  ╚═════╝  ╚═════╝  ╚═╝{Fore.RESET}""")
time.sleep(2)

slowtype('Connecting to the servers...\n');
time.sleep(1)



characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9']

while True:
    Nitro = ''

    for i in range(16):
        Nitro = f"{Nitro}{random.choice(characters)}"

    print(f"https://discord.gift/{Nitro}") 
    time.sleep(.05)

    with open("./Codes/codes.txt", "a+") as codesF:

        codesF.write(f"https://discord.gift/{Nitro}\n")

        codesF.close()
