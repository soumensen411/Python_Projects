# Weight converter
weight = float(input("Enter your weight: "))
unit = input("Enter unit (kg/lbs) : ")
if(unit == 'kg'):
    weight = weight * 2.20462
    print(f"Your weight is {weight:.2f} lbs")
elif unit == 'lbs':
    weight = weight / 2.20462
    print(f"Your weight is {weight:.2f} kg")
else:
    print("Enter a valid unit.")
    