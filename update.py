import random
import time
## Question
l1 = ["yes", "no"]
for x in range(1):
    rand = random.randint(0, 1)
    print("\033[1;31;01mIs it time for a pacman -Syu?\r")
## "calculating"
    time.sleep(5)
## Output
    print("\033[1;32;01m\n")
    print(l1[rand])

## if yes -> force update lol
