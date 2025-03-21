def main():
    num_students=int(input("Enter the number of Students"))
    global students
    students=[]
    for _ in range(num_students):
        name=input("Enter the Students name")
        while True:
            try:
                score=float(input(f"Enter the score for {name}(0-100)"))
                if 0<=score<=100:
                    break
                else:
                    print("Score must be between 0 and 100. Please try again")
            except ValueError:
                print("Invalid input.Please enter a numeric value")
        students.append((name,score))
    calculate_stats()
    menu()
def calculate_stats():
    if not students:
       print("No student availabel")
       return
    total_score=0
    global highest_score
    highest_score=-1
    global lowest_score
    lowest_score=101
    highest_student=None
    lowest_student=None
    
    for student in students:
        total_score += student[1]
        if student[1] > highest_score:
            highest_score=student[1]
            highest_student=student
        if student[1] < lowest_score:
           lowest_score=student[1]
           lowest_student=student
    average_score=total_score / len(students)
    print(f"\naverage score:{average_score:.2f}")
    print(f"highest score:{highest_score} by {highest_student[0]} with grade {get_grade(highest_student[1])}")
    print(f"lowest score:{lowest_score} by {lowest_student[0]} with grade {get_grade(lowest_student[1])}")
    
def get_grade(score):         
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'    
    elif score >= 60:
        return'D' 
    elif score >= 50:
        return 'E'    
    else:
        return 'F'
    
def search_student():
    name=input("Enter the student name to search")
    for student in students:
        if student[0].lower() == name.lower():
           print(f"{student[0]} scored {student[1]} and received grade {get_grade(student[1])}")
           return
           print("Student not found.")
            
def add_student():
    name=input("Enter the new students name:") 
    while True:
        try:
          score=float(input(f"Enter the score for {name}(0-100):"))
          if 0 <= score <=100:
              break
          else:
                    print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    students.append((name,score))
    print(f"{name} added successfully!")
                
def view_all_students():
    if not students:
       print("No student availabel.")
    else:
        print("\nList of all students:")
        for name,score in students:
            print(f"{name}:{score}(grade:{get_grade(score)}")
            
def menu():            
    while True:
        print("\nOptions:")
        print("1. Search for a student")
        print("2. Addd a new student")
        print("3. View all students")
        print("4. Exit")
        choice=input("Enter your choice:")
        if choice=='1':
           search_student()
        elif choice=='2':
            add_student()
        elif choice=='3':
            view_all_students()
        elif choice=='4':
            print("Exiting program")
            break
        else:
            print("Invalid choice.Please try again.")

if __name__ ==  "__main__":
    main()            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                    
                            
    
    
    
    
    
    
    
    
    
    
    

