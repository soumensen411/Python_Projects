#Python Bank Management System

def showBalance(balance):
    print()
    print(f"Your Balance is ${balance:0.2f}")
    print()

def diposit():
    amount = float(input("Enter an amount to be deposit: "))
    if amount < 0:
        print()
        print("That's not a valid amount")
        print()
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to be Withdrawn: "))
    if amount > balance:
        print()
        print("Insufficient Amount")
        print()
        return 0
    elif amount < 0:
        print()
        print("Amount must be greater then zero")
        print()
        return 0
    else:
        return amount
balance = 0
while True:
    print("*****************************")
    print("Welcome to the Soumen's Bank")
    print("*****************************")
    print('1. To show balance')
    print('2. For deposit ')
    print('3. For Wihdraw')
    print('4. for quit')
    choice = int(input("Enter Your Choice: ")) 
    if choice == 1:
        showBalance(balance)
    elif choice == 2:
        balance += diposit()
    elif choice == 3:
        balance -= withdraw(balance)
    elif choice == 4:
        break
    else :
        print("Invalid Choice! 💁‍♂️")
        
print("*****************************")
print("Thank you! Have a nice day.")
print("*****************************")
