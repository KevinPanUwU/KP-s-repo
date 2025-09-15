age = int(input())
 
if (age >= 18) and (age <= 65):
    print("You are eligible to work.")
elif age < 18:
    print("You are not eligible to work.")
else:
    print("You are eligible to retire.")