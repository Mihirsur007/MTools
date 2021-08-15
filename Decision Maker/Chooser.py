import random
from time import sleep

print("\n")
print("Welcome to decision maker")
sleep(2)
print("\n")
print("Use this tool to help you with your decision making")
sleep(2)
print("\n")
print("Here are the commands you can use:")
sleep(1)
print("1: Yes or No: type Y")
sleep(1)
print("2: Dice Roll: type Dice")
sleep(1)
print("3: Random Number (1 to 1000): type Random")

Get = input(">> ")
if Get == "Y":
    random = random.randint(0,2)
    
    if random == 1:
        print("\n")
        print("yes")
        print("\n")
    else:
        print("\n")
        print("no")
        print("\n")

if Get == "Dice":
    random = random.randint(0,6)
    print("\n")
    print("The number on the dice is: ")
    print("\n")
    print(random)
    print("\n")

if Get == "Random":
    random = random.randint(0,1000)
    print("\n")
    print(random)
    print("\n")
    

