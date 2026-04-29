import json
print("------ STUDENT MANAGEMENT SYSTEM------")
# students = {}

def save_data():
    with open("student.json","w") as f:
        json.dump(students,f)
    
def load_data():
    global students
    try:
        with open("student.json","r") as f:
            students = json.load(f)
    except:
        students = {}
        
def add_Student():
    name = input("Enter Your Name: ")
    try:
        marks = int(input("Enter your Marks: "))
        students[name]=marks
        print(f"{name} added successfully.!") 
    except ValueError:
        print("Marks must be in number")
        
def view_Students():
    if not students:
        print("There is a no student yet")
    else:
        for name,marks in students.items():
            print(f"{name}:{marks}")
            
def view_Result():
    name = input("Enter student name: ")
    if name in students:
        mark = students[name]
        print(f"{name}: {mark}")
        print(f"Gread: {calculate_grade(mark)}")
    else:
        print("Student not Found!")
        
def calculate_grade(mark):
    if mark>=80:
        return "A+"
    elif mark>=70 and mark<80:
        return "A" 
    elif mark>=60 and mark<70:
        return "A-" 
    elif mark>=50 and mark<60:
        return "B+" 
    elif mark>=40 and mark<50:
        return "B-" 
    elif mark<40:
        return "Fail" 
    
while True:
    load_data()
    print("1- Add New Student")
    print("2- View Students")
    print("3- View Result")
    print("4- Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("invalid Input")
        continue
    # add students
    if choice == 1:
           add_Student()
           save_data()
    # view students
    elif choice == 2:
        view_Students()
    # view results 
    elif choice == 3:
        view_Result()
    # Exit
    elif choice == 4:
        print("Ending...")
        break
    else:
        print(f"In-valid Entry")