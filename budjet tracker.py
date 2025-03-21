# budjet tracker
expenses=[]
def show_menu():
    print("\nbudjet tracker")
    print("1. add expenses")
    print("2. view expenses")
    print("3. view total expenses")
    print("4. exit") 
    
def add_expense():
    item=input("enter the expense item:")
    cost=float(input("enter the cost:")) 
    expenses.append({"item":item, "cost":cost})
    print(f"added {item} with cost {cost}.")

def view_expenses():
    print("\nexpenses:")
    for x in expenses:
        print(f"{x ['item']}: ${x ['cost']}")
        
def view_total_expenses():
    total=sum(expense['cost']for expense in expenses) 
    print(f"\ntotal expenses:${total}") 

while True:
    show_menu()
    choice=input("enter your choice:")
    if choice=='1':
        add_expense() 
    elif choice=='2':
        view_expenses()
    elif choice=='3':
        view_total_expenses()       
    elif choice=='4':
         break
    else:
        print("invalid choice.please try again")
        
        