# Compound Interest Calculator

principle = float(input("Enter the principle amount: "))
while principle <= 0:
    print("Principle can't be less than or equal to zero")
    principle = float(input("Enter the principle amount: "))

rate = float(input("Enter the interest rate: "))
while rate <= 0:
    print("Interest rate can't be less than or equal to zero")
    rate = float(input("Enter the interest rate: "))

time = int(input("Enter the time in years: "))
while time <= 0:
    print("Time can't be less than or equal to zero")
    time = int(input("Enter the time in years: "))

# Compound Interest formula: A = P * (1 + r/100) ** t
amount = principle * (1 + rate / 100) ** time
compound_interest = amount - principle

print(f"Principle: {principle}")
print(f"Rate: {rate}")
print(f"Time: {time}")
print(f"Compound Interest: {round(compound_interest, 2)}")
print(f"Total Amount: {round(amount, 2)}")