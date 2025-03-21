
import random
def playgame(user):
    game=["rock","paper","scissors"]
    comp=random.choice(game)
    
    if (user=="rock"):
        if (comp=="scissors"):
            print(f"user win.computer choice is {comp}")
            print("😊😊😊😊rock win😊😊😊😊")
        else:
            print(f"comp win. computer choice is {comp}")
            print("😊😊😊😊scissors win😊😊😊😊")
    
    elif (user=="paper"):
        if (comp=="rock"):
            print(f"user win.computer choice is {comp}")
            print("😍😍😍😍paper win😍😍😍😍")
        else:
            print(f"comp win.computer choice is {comp}")
            print("😍😍😍😍rock win😍😍😍😍")
    
    elif (user=="scissors"):
        if (comp=="paper"):
           print(f"user win.computer choice is {comp}")
           print("😎😎😎😎scissors win😎😎😎😎")
        else:
            print(f"comp won.computer choice is {comp}")
            print("😎😎😎😎paper win😎😎😎😎")

while True:
    print("\n welcome to our game rock,paper,scissor")
    print("1. rock")
    print("2. paper")
    print("3. scissor")
    print("4. exit")
    choice=input("enter your choice")
    if choice=='1':
       userchoice= "rock"
       playgame(userchoice)
    elif choice=='2':
        userchoice= "paper"
        playgame(userchoice)
    elif choice=='3':
        userchoice="scissor"
        playgame(userchoice)
    else:
        print("invalid syntax")
        break
        

