import random

ted = random.randint(1,6)#variable
ohare = random.randint(1,6)#variable

def dice():

    #Dice Roll
    print("You planted your Truffula Seeds. " + str(ted))
    print("O'hare sent bodyguards to locate and destroy the seeds. " + str(ohare))

    if ted > ohare:
        print("My name is Ted Wiggins. I speak for the trees. The trees say I won!")
    elif ted == ohare:
        print("The same amount of trees grew that seeds got destroyed. Huh.")
    else: 
        print("Let it die, let it die, let it shrivel up and, come on, who's with me, huh?")

#REPLANT
while True:
    print("Press return to plant more seeds!")
    roll = input()
    dice()
        

