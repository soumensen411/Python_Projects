#============= Python Calculator =============

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter 1st number "))
num2 = float(input("Enter 2nd number "))
if(operator == '+'):
    print(f'{num1} + {num2} = {round(num1 +num2 , 3)}')
elif operator == '-':
    print(f'{num1} - {num2} = {round( num1 - num2,3)}')
elif operator == '*':
    print(f'{num1} * {num2} = {round( num1 * num2,3)}')
elif operator == '/':
    if num2 == 0:
        print(f"Impossibe to divide {num1} by zero")
    else:
        print(f'{num1} / {num2} = {round( num1 / num2,3)}')
else:
    print("Enter an valid operator") 