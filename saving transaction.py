''' function to add a saving transaction'''
def add_savings(savings_transactions,description,amount):
    savings_transactions.append({"description":description,"amount":amount})
    
def add_investment(investments_transactions,description,amount):
    investments_transactions.append({"description":description,"amount":amount}) 

def display_transactions(transactions,title):
    print(f"\n{title}:")
    for transaction in transactions:
        print(f"{transaction['description']}:${transaction['amount']:2f}")

def calculate_total(transactions):
    return sum(transaction['amount']for transaction in transactions)

savings_transactions=[]
investments_transactions=[]
while True:
    print("\nMenu")
    print("1. add Savings")
    print("2. Add Investment")
    print("3. View Savings")
    print("4. View Investments")
    print("5. View Total Savings and Investments")
    print("6. exit")

    choice=input("choose an option (1-6):")
    if choice=='1':
        description=input("enter savings description:")
        try:
           amount=float(input(f"enter amount for savings:$"))
        except ValueError:
            print("Invalid amount.please enter a number.")
            continue
        add_savings(savings_transactions,description,amount)
   
    elif choice=='2':
         description=input("enter investment description:")
         try:
            amount=float(input(f"enter amount for investment:$"))
         except ValueError:
             print("Invalid amount.please enter a number.")
             continue
         add_investment(investments_transactions,description,amount)

    elif choice=='3':
        display_transactions(savings_transactions,"Savings")

    elif choice=='4':
        display_transactions(investments_transactions,"investments")
        
    elif choice=='5':
        total_savings=calculate_total(savings_transactions)
        total_investments=calculate_total(investments_transactions)
        print(f"\nTotal Savings:${total_savings:2f}")
        print(f"\nTotal investments:${total_investments:2f}")
        print(f"combined total savings and investments:${total_savings+total_investments:2f}")
    elif choice=='6':
        print("exiting the program.goodbye!")
        break
    else:
        print("invalid choice.please choose a number between 1 and 6.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
        