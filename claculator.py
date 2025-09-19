# Python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    print(round(num1 + num2))
elif operator == "-":
    print(round(num1 - num2))
elif operator == "*":
    print(round(num1 * num2))
elif operator == "/":
    if num2 != 0:
        print(round(num1 / num2))
    else:
        print("Error: Division by zero.")
else:
    print("Invalid operator.")