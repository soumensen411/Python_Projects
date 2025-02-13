# concession stand program 

menu = {
    "Chips": 20,
    "Chicken Fry": 50,
    "Burger": 80,
    "Pizza": 120,
    "Pasta": 90,
    "Sandwich": 60,
    "Soft Drink": 30,
    "Ice Cream": 40
}

cart = []
total = 0
print("-------- MENU --------")
for key,value in menu.items():
    print(f"{key:15}:{value:0.2f}")
print()
while True:
    chose = input("Enter Item (q to quit): ")
    if(chose == 'q' or chose == 'Q'):
        break
    elif menu.get(chose) is not None:
        cart.append(chose)
    else:
        print(f"{chose} isn't find in the menu")
print("---- YOUR ORDER ----")
for item in cart:
    total += menu.get(item)
    print(item,end=' ')
print()
print(f"Your total is {total}")