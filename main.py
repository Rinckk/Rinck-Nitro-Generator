import random
import time
import os
import colorama 
from colorama import Fore

colorama.init()

os.system('TITLE Rinck#0001 » Rinck-Nitro-Generator')

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9']

while True:
    Nitro = ''

    for i in range(16):
        Nitro = f"{Nitro}{random.choice(characters)}"

    print(f"{Fore.RED}[INVALID]{Fore.RESET} » https://discord.gift/{Nitro}") 
    time.sleep(0.001)

    with open("./Codes/codes.txt", "a+") as codesF:

        codesF.write(f"Rinck#0001 » https://discord.gift/{Nitro}\n")

        codesF.close()
