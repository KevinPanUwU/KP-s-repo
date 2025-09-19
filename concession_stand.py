# Concession stand program

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = []
total = 0

print("-------- MENU --------")
for item, price in menu.items():
    print(f"{item:10}: ${price:.2f}")
print("----------------------")

while True:
    choice = input("Select an item (q to quit): ").lower()
    if choice == "q":
        break
    elif choice in menu:
        cart.append(choice)
        total += menu[choice]
    else:
        print("Item not on menu. Please choose again.")

print("------ YOUR ORDER ------")
for item in cart:
    print(item, end=" ")
print(f"\nTotal is: ${total:.2f}")