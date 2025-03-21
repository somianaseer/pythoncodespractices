import random
def play_game():
    num=int(input("enter a number between(1-10)"))
    comp=random.randrange(1,10)
    if comp==num:
        print("👍👍👍👍👍👍congratulation you won👍👍👍👍👍")
    elif comp<num:
        print("*********😢😢😢😢😢you loss the game*********")
        print(f"your number is greater,computer genrated number is   {comp}")
    else:
        print("*********😢😢😢😢😢you loss the game**********")
        print(f"your number is less:computer genrated number is   {comp}")

while True:
    print("\nWelcome to random number")
    print("1. play game")
    print("2. quit game")
    choice=input("enter your choice")
    if choice=='1':
        play_game()
    elif choice=='2':
       print("are you sure you want to quit ")
       print("😃😃😃😃game ended😃😃😃😃😃")
       break
    else:
        print("invalid choice")
        
    
        

