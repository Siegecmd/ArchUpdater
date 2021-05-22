import random #random gen
import os #OS ID
import time #for sleep
from halo import Halo #loading
## Question
l1 = ["yes", "no"]
for x in range(1):
    update = random.randint(0, 1) # 0 = y 1 = n
    print("\033[1;31;01mIs it time to update?\r")

with Halo(text='Loading', spinner='dots'):
## Output
    print("\033[1;32;01m\n")
time.sleep(2)
print(l1[update])
time.sleep(5)
## if yes -> force update lol
if update == 0:
	os.system("sudo pacman -Syu")
else:
	print("it's your lucky day.")
	exit()