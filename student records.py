"""
Write a program that uses a dictionary to store student records, where each key
is a unique roll number and the value is an other dictionary containing the 
student's name, course, and marks. The program provides a menu-driven 
interface for users to interact with the system.
"""
def display_menu():
    print("\nStudent Record")
    print("1.add student record ")
    print("2. view student record")
    print("3. update student record")
    print("4. delete student record")
    print("5. view all record")
    print("6. exit")

def add_student(record):
    roll_number=input("enter the roll number:")
    if roll_number in record:
        print("roll number already exits")
        return
    name =input("enter student name ")
    course=input("enter student course")
    marks=float(input("enter student marks"))
    record[roll_number]={"name":name,"course":course,"marks":marks}
    print("student record added successfully")
 
def view_student(record):
    roll_number=input("enter roll number to view:")
    if roll_number in record:
        print("\nStudent Record")
        for key, value in record[roll_number].items():
            print(f"{key.capitalize()}:{value}")
    else:
        print("no record found for the given roll number")

def update_student(record):
    roll_number=input("enter roll number to update")
    if roll_number in record:
        print("\ncurrent record")
        for key, value in record[roll_number].items():
            print(f"{key.capitalize()}:{value}") 
        print("\nenter new details (leave blank to keep curent value):") 
        name=input("enter student name") or record[roll_number]["name"]
        course=input("enter student course") or record [roll_number]["name"]
        marks=input("enter student marks")
        if marks:
            marks=float(marks)
        else:
            marks=record[roll_number]["marks"]
        record[roll_number]={"name":name,"course":course,"marks":marks}
    else:
        print("no record found for the given roll number")

def delet_student(record):
    roll_number=input("enter roll number to delet")
    if roll_number in record:
        del record[roll_number]
        print("student record deleted successfully") 
    else:
        print("no record found for the given roll number")
        
def view_all_record(record):
    if not record:
        print("no student record found")
        return
    print("\nall student record")
    for roll_number,details in record.items():
        print(f"roll number:{roll_number}")
        for key,value in details.item():
            print(f"{key.capitalize()}:{value}")
            
def main():
    student_record={}
    while True:
        display_menu()
        choice=input("enter your choice(1-6):")
        if choice=='1':
            add_student(student_record)
        elif choice=='2':
            view_student(student_record)
        elif choice=='3':
            update_student(student_record)
        elif choice=='4':
            delet_student(student_record)
        elif choice=='5':
            view_all_record(student_record)
        elif choice=='6': 
            print("exiting the program.Goodbye")
            break
        else:
            print("invalid choice.please try again")

if __name__=="__main__":
    main()            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    