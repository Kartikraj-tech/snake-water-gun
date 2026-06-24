import random
'''
1 for snake
-1 for water 
0 for gun
'''

computer = random.choice([1,-1,0])
youStr = input("Enter your choice : ").lower() # we are taking the input from user in form of snake, water, gun
youDict = {"snake":1,
           "water":-1,
           "gun":0} # assingming key-value for game using dictionary

if youStr not in youDict:
    print("invalid choice")
    exit()

you = youDict[youStr] # assigning the user value from youStr to dictionary and assign to you

reversedDict = {1:"snake",
                -1:"water",
                0:"gun"}
print(f"you choose {reversedDict[you]} \n computer choose {reversedDict[computer]}")

if(computer==you):
    print("draw")
else:
    if(computer==-1 and you==1):
        print("you win")
    elif(computer==-1 and you==0):
        print("you lose")
    elif(computer==1 and you==-1):
        print("you lose")
    elif(computer==1 and you==0):
        print("you win")
    elif(computer==0 and you==1):
        print("you lose")
    elif(computer==0 and you==-1):
        print("you win")

    else:
        print("something went wrong")