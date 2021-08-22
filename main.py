#
# NitroGen
#  
# This work is licensed under GNU
# GENERAL PUBLIC LICENSE
#

import random, string
import os

reset = "\e[0m"
red = "\e[0;31m"
green = "\e[0;32m"

try:
    os.remove("nitroCode.txt")
except Exception as e:
    print("Error " + str(e))

code = "https://discord.gift/"
code += ('').join(random.choices(string.ascii_letters + string.digits, k=16))

f = open("nitroCode.txt", "a+")
f.write(f"{code}\n")
f.close()
print(f"{code}")
