# Python Banking Program

def show_balance(balance):
    print("********************")
    print(f"Your balance is ${balance:.2f}")
    print("********************")

def deposit():
    print("********************")
    amount = float(input("Enter an amount to be deposited: "))
    print("********************")
    if amount < 0:
        print("********************")
        print("That's not a valid amount")
        print("********************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("********************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("********************")
    if amount < 0 or amount > balance:
        print("********************")
        print("That's not a valid amount")
        print("********************")
        return 0
    else:
        return amount

def main():
    balance = 0.0
    while True:
        print("\n1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            print("Thank you for using the banking program!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()