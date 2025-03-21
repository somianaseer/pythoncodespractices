def calculate_bmi(weight,height):
    return weight /(height**2)

def calculate_simple_interest(principal,rate,time):
    return (principal*rate*time)

def calculate_monthly_expenses(expenses):
    return sum(expenses)

calculator_dict={
        "BMI":calculate_bmi,
        "SimpleInterest":calculate_simple_interest,
        "MonthlyExpenses":calculate_monthly_expenses
        }

def main():
    while True:
        print("\nDaily Life Calculator Menu")
        print("1. Calculate BMI")
        print("2. Calculate Simple Intrest")
        print("3. Calculate Monthly Expenses")
        print("4. Exit")
        choice=input("Enter your choice(1-4)")
        
        if choice=='1':
            weight=float(input("Enter your weight(kg)"))
            height=float(input("Enter your height(m)"))
            bmi=calculator_dict["BMI"](weight,height)
            print(f"your bmi is:{bmi:.2f}")
            
        elif choice=='2':
            principal=float(input("Enter the principal amount"))
            rate=float(input("Enter the annual interest rate(in %):"))
            time=float(input("Enter the time period (in year): "))
            interest=calculator_dict['SimpleInterest'](principal,rate,time)
            print(f"the simple interest is: {interest:.2f}")
            
        elif choice=='3':
            num_expenses=int(input("How many expenses do you want to enter?"))
            expenses=[]
            for _ in range(num_expenses):
                expense=float(input("Enter an expense"))
                expenses.append(expense)
            total_expenses=calculator_dict["MonthlyExpenses"](expenses)
            print(f"Your total monthly expenses are:{total_expenses:.2f}")
            
        elif choice=='4':
            print("Exiting the calculator.")
            break
        
        else:
            print("Invalid choice.please select a number between 1 and 4.")

if __name__=="__main__":
    main() 
          
            
                
                
                
                
                
                
                
                
                
