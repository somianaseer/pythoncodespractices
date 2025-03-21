def calculate_bmi(weight,height):
    """calculate bodymass index(BMI)."""
    return weight/(height**2)

def calculate_simple_interest(principal,rate,time):
    """calculate simple interest"""
    return(principal*rate*time)/100

def calculate_monthly_expenses(expenses):
    """calculte total monthly expenses"""
    return sum(expenses)

calculator_dict={
    "BMI":calculate_bmi,
    "simple interest":calculate_simple_interest,
    "monthly expenses":calculate_monthly_expenses
    }
def main():
    while True:
        print("\ndaily life calculator menu:")
        print("1. calculate BMI")
        print("2. calculate simple interest")
        print("3. calculte monthly expenses")
        print("4. exit")
        choice=input("enter your choice(1-4):")
        if choice=='1':
            weight=float(input("enter your weight(kg):"))
            height=float(input("enter your height(m):"))
            bmi=calculator_dict["BMI"](weight,height)
            print(f"your BMI is:{bmi:.2f}")
        elif choice=='2':
            principal=float(input("enter your principal amount:"))
            rate=float(input("enter your annual interest rate(in%):"))
            time=float(input("enter the time period(in years):"))
            interest=calculator_dict["simple interest"](principal,rate,time)
            print(f"the simple interest is:{interest:.2f}") 
        elif choice=='3': 
            num_expens=int(input("how many expenses do you want to enter?"))
            expenses=[]
            for _ in range(num_expens):
                expense=float(input("enter an expenses:"))
                expenses.append(expense)
                total_expenses=calculator_dict["monthly expenses"](expenses)
                print(f"your total monthly expenses are: {total_expenses:.2f}")
        elif choice=='4':
            print("exiting the calculator")
            break
        else:
            print("invalid choice.please select a number between 1 and 4.")
if __name__=="__main__": 
    main()               