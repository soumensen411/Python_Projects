import json

with open("profile.json",'r') as f:
    people = json.load(f)['contacts']
            
def add_profile(people):
    name = input("Enter Your Name: ")
    age = input("Enter Your Age: ")
    Email = input("Enter Your Email: ").lower()
    person = {
        "name":name,
        "age":age,
        "email":Email
    }
    people.append(person)
    

def display(people):
    if not people: 
        print("No profiles to display.")
        return
    for i,person in enumerate(people):
        print(i+1,".",person["name"],"|",person["age"],"|",person['email'])
        
def update_profile(people):
    display(people)
    if not people:
        return 
    
    while True:
        try:
            indx = int(input("Enter a Index Number for Update: "))
            if indx <= 0 or indx > len(people):
                print("Out of range! Please Enter a valid index.")
            else:
                break
        except ValueError:
            print("Invalid Number")
            
    person = people[indx - 1]
    new_name = input(f"New Name ({person['name']}): ")    
    new_age = input(f"New Age ({person['age']}): ")    
    new_email = input(f"New Email ({person['email']}): ").lower()    
        
    if new_name.strip():
        person['name'] = new_name
    if new_age.strip():
        person['age'] = new_age
    if new_email.strip():
        person['email'] = new_email    
    print("Profile update successfully!")
    
    
def delete_profile(people):
    display(people)
    if not people: 
        return
    
    while True:
        try:
            indx = int(input("Enter a Number to Delete: "))
            if indx <= 0 or indx > len(people):
                print("Out of range! Please Enter a valid index.")
            else:
                break
        except ValueError:
            print("Invalid Number")
            
    people.pop(indx-1)
    print("Person Deleted")
            
def search(people):
    display(people)
    search_name = input("Search for a name: ").lower()
    result = []
    for person in people:
        name = person["name"]
        if search_name in name.lower():
            result.append(person)
            
    if result:
        display(result)
    else:
        print("No matching profile found.")
    
def save_data():
    with open("profile.json", 'w') as f:
        json.dump({"contacts": people}, f, indent=4)

print("-------- PROFILE MANAGEMENT SYSTEM --------")

while True:
    print("1- Add Profile")
    print("2- Update Profile")
    print("3- Search Profile")
    print("4- Delete Profile")
    print("5- Quit")
    
    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Invalid Input! Please enter a number.")
        continue
    
    if choice == 1:
        add_profile(people)
        save_data()
        print("Entry Added Successfully!")
        
    elif choice == 2:
        update_profile(people)
        save_data()
    elif choice == 3:
        search(people)
    elif choice == 4:
        delete_profile(people)
        save_data()
    elif choice == 5:
        print("Ending ...")
        break
    else:
        print("Invalid Input")
