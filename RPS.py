import random 
print("ROCK PAPER SCISSOR GAME!") 
game=["rock","paper","scissor"]
a=int(input("Choose{1.Rock,2.Paper,3.Scissor}:"))
if(a==1):
 print("Rock")
if(a==2):
 print("Paper")
if(a==3):
 print("Scissor")

b=random.choice(game)
print("computer choice:",b)
if(game[a-1]==b):
 print("its a draw")
elif(a==3 and b=="paper"):
 print("you won!!!!")
elif(a==1 and b=="scissor"):
 print("you won!!!!")
elif(a==2 and b=="rock"):
 print("you won!!!!")
else:
 print("you lost")