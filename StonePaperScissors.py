from random import randint
random_num= randint(0,2)
player=input("enter your move: ").lower()
if random_num==0:
    computer="stone"
elif(random_num==1):
    computer="paper"
else:
    computer="scissors"
print("computer is",computer)
if(player==computer):
    print("It's a tie")
elif(player=="stone" and computer=="scissors"):
    print("player wins")
elif(computer=="stone" and player=="scissors"):
    print("computer wins")
elif(player=="paper" and computer=="stone"):
    print("player wins")
elif(computer=="paper" and player=="stone"):
    print("computer wins")
elif(player=="scissors" and computer=="paper"):
    print("player wins")
elif(computer=="scissors" and player=="paper"):
    print("computer wins")
else:
    print("wrong input by the player")


