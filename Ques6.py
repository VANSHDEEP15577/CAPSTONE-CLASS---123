import random
number=random.randint(2000,2010)
print("WHAT IS THE PASSWORD OF THIS DEVICE?[HINT=IT IS BETWEEN 2000 TO 2010]")
chance=0
while chance < 3:
    guess=int(input("ENTER THE PASSWORD:"))
    if guess == number:
        print("DEVICE UNLOCKED")
        break
    else:
        print("WRONG PASSWORD")
    chance += 1
if not chance < 3:
    print("THE PHONE IS LOCKED BECAUSE OF UNSUCCESSFUL ATTEMPTS")