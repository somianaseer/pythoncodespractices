reminders=[]
def show_menu():
    print("\nReminder App")
    print("1. add reminder")
    print("2. view reminder")
    print("3. exit" )
    
def add_reminder(): 
    task=input("enter the task to be reminded:")
    time=input("enter the time for the reminder (e.g.,14:00):")
    reminders.append({"task":task,"time":time})
    print(f"added reminder for{task} at {time}.")

def view_reminder(): 
    print("\nreminders:")
    for reminder in reminders:
        print(f"{reminder['time']}: {reminder['task']}")
        
while True:
    show_menu()
    choice=input("enter your choice:")
    if choice=='1':
        add_reminder()
    elif choice=='2':
        view_reminder()
    elif choice=='3':
        break
    else:
        print("invalid choice.please try again") 
        