import random
import time
import os

os.system('TITLE Rinck#0001 » Rinck-Nitro-Generator')

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9']

while True:
    randomNitro = ''

    for i in range(16):
        randomNitro = f"{randomNitro}{random.choice(characters)}"

    print(f"Rinck » https://discord.gift/{randomNitro}") 
    time.sleep(0.001)

    with open("./Codes/codes.txt", "a+") as codesF:

        codesF.write(f"Rinck#0001 » https://discord.gift/{randomNitro}\n")

        codesF.close()
