bikes={
 "1":{"type":"mountain bike","rentperhour":5,"is_availabel":True,"rented_by":"None"},
 "2":{"type":"road bike","rentperhour":8,"is_availabel":True,"rented_by":"None"},
 "3":{"type":"hybrid bike","rentperhour":3,"is_availabel":True,"rented_by":"None"}
 }

total_earnings=0
def display_bikes():
    print("availabel bikes")
    for bike_id, bike_info in bikes.items():
        if bike_info["is_availabel"]:
           print(f"bikes_id:{bike_id},type:{bike_info['type']},rentperhour:{bike_info['rentperhour']}")
           
def add_bike():
    global bikes
    new_id=str(len(bikes)+1)  
    bike_type=input("enter bike type")
    while True:
        try:
            rent_per_hour=int(input("enter rent per hour:"))
            if rent_per_hour<=0:
                print("please enter a valid rent amount")
            else:
                break
        except ValueError: 
           print("invalid input.please enter a valid number")
    bikes[new_id]={"type":bike_type,"rent_per_hour":rent_per_hour,"is_availabel":True,"rented_by":None} 
    print(f"bike {new_id}({bike_type}) added successfully")    
    
def remove_bike():
    global bikes
    bike_id=input("enter bike id to remove")
    if bike_id in bikes:
        if bikes[bike_id]["is_availabel"]:
            del bikes[bike_id]
            print(f"bike {bike_id} removed successfully")
        else:
            print(f"bike{bike_id}is currently rented and cannot be removed")
    else:
        print("invalid bike id")         
    
def rent_bikes(bike_id,customer_name,hours):
    global total_earnings
    if bike_id in bikes and bikes[bike_id]["is_availabel"]:
        bikes[bike_id]["is_availabel"] = False
        bikes[bike_id]["rented_by"]=customer_name
        rent_cost=calculate_rent(bike_id,hours)
        total_earnings += rent_cost
        print(f"Total Rent:${rent_cost}")
        
        while True:
           recieve= float(input("enter amount to pay for rent "))
           if recieve==rent_cost:
               return f"bike{bike_id} rented successfully to {customer_name}.Total Rent:${rent_cost}"       
         
           else:
                print("invalid input.type equal amount")
    else:
        return f"bike {bike_id}is not availabel"

def return_bike(bike_id): 
    if bike_id in bikes and not bikes[bike_id]["is_availabel"]:
        bikes[bike_id]["is_availabel"]=True
        bikes[bike_id]["rented_by"]=None
        penalty_bike()
        print( f"bike{bike_id} returned successfully.It is now availabel for rent.")
        display_bikes()
    else:
        return f"bike{bike_id} is already availabel."
    
    
def calculate_rent(bike_id,hours):
    if bike_id in bikes:
        rent_per_hour=bikes[bike_id]["rentperhour"]
        global total_rent
        total_rent= rent_per_hour*hours
        if hours < 12:
           discount=0.5
           total_rent *= (1-discount)
           print("🎉🎉🎉🎉🎉short Rental Discount Applied(5 % off)🎉🎉🎉🎉")
        elif hours > 12 and hours <= 24:
             discount=0.10
             total_rent *= (1-discount)
             print("🎉🎉🎉🎉Short Rental Discount Applied!(10 % off)🎉🎉🎉🎉")
        elif hours >=24 and hours<=36:
             discount=0.15
             total_rent *= (1-discount)
             print("🎉🎉🎉🎉Short Rental Discount Applied!(15 % off)🎉🎉🎉🎉")
        elif hours >=37:
             discount=0.25
             total_rent *= (1-discount)
             print("🎉🎉🎉🎉Long Rental Discount Applied!(25 % off)🎉🎉🎉🎉")
    return round (total_rent,2)
    return None

def view_total_earnings():
    """view total earning from bike rental"""
    print(f"\nTotal Earnings:${total_earnings}")

def cancel_reservation():
    bike_id=input("enter your id to cancel reservation")
    if bike_id in bikes and not bikes[bike_id]["is_availabel"]:
        bikes[bike_id]["is_availabel"]=True
        customer_name=bikes[bike_id]["rented_by"]
        bikes[bike_id]["rented_by"]=None
        print(f"reservationfor bike{bike_id} (rented by {customer_name})has been canceled successfully")
    else:
        print("Invalid bike ID or bike is not currently reserved")
        
def penalty_bike():
        return_hour= int(input("enter hours after you return a bike"))
        if hours>=return_hour:
            print("No penalty charges")
        else:
            penalty=total_rent+total_rent*0.01
            print(f"penalty charges are{penalty}")

def main():
    while True:
        print("\n😊😊😊😊😊 Welcome to Bike rental system😊😊😊😊😊")
        print(" \t\t\t\t 1.Display availabel bike")
        print("\t\t\t\t 2.Rent a Bike")
        print("\t\t\t\t 3.Return Bike")
        print("\t\t\t\t 4.View Total Earnings")
        print("\t\t\t\t 5.Add a New Bike")
        print("\t\t\t\t 6.Remove a Bike")
        print("\t\t\t\t 7.Cancel a Reservation")
        print("\t\t\t\t 8.Exit")
        choice=input("\n\t\t\t  Enter your choice")
        if choice=='1':
            display_bikes()
        elif choice=='2':
            bike_id=input("enter bike id to rent:")
            while True:
               customer_name=str(input("enter your name:"))
               if customer_name.isalpha():
                   break
               else:
                    print("invalid input.type string pleaze")
            
            while True:
                try:
                     global hours
                     hours=int(input("enter number of hours to rent:"))
                     
                     if hours<=0:
                        print("Invalid input.please enter a positive integer.")
                     else:
                        break
                except ValueError:
                    print("Invalid input.please enter a positive integer.")
            print(rent_bikes(bike_id, customer_name, hours))
        elif choice=='3':
            bike_id=input("enter bike id to return")
            (return_bike(bike_id))
            display_bikes()
        elif choice=='4':
            view_total_earnings()
        elif choice=='5':
            add_bike()
        elif choice=='6':
            remove_bike()
        elif choice=='7':
            cancel_reservation()
        elif choice=='8':
            print("Exiting bike rental system.Goodbye")
            break
        else:
            print("invalid choice. please try again" )

if __name__=="__main__":
    main()            
            
            
            
            
            
            