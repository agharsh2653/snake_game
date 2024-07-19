'''
Snake = 1
water = -1
gun = 0
'''
import random
#computer = random.randint(-1,1)
computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w":-1, "g":0}
you = youDict[youstr]
reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
     print("Its a draw ")
else:
     # if(computer ==-1 and you ==1): -2
     #      print("You Win")
     # elif(computer ==-1 and you ==0): -1
     #      print("You lose!")
     # elif(computer ==1 and you ==-1): 2
     #      print("You lose!")
     # elif(computer ==1 and you == 0): 1
     #      print("You Win!")
     # elif(computer ==0  and you ==-1):1
     #      print("You Win!")
     # elif(computer ==0  and you ==1):
     #      print("You Lose!")
     # else:
     #      print("Something went wrong!")

     if(computer-you==-1 or computer -you == 2):
          print("You Win")
     else:
          print("You Lose!")
