workouts=[]
def show_menu():
    print("\nWorkout Tracker")
    print("1. Log workout")
    print("2. View workouts")
    print("3. exit")

def log_workout():
    workout=input("enter the workout activity:")
    duration=float(input("enter the duration in minutes:"))
    workouts.append({"activity":workout,"duration":duration})
    print(f"logged{workout} for {duration} minutes.")

def view_workouts():
    print("\nworkouts:")
    for workout in workouts:
        print(f"{workout['activity']}:{workout['duration']}minutes")
while True:
    show_menu()
    choice=input("enter your choice:")
    if choice=='1':
        log_workout()
    elif choice=='2':
        view_workouts()
    elif choice=='3':
        break
    else:
        print("invalid choice.please try again.")        

