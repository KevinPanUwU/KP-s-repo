# Python quiz game

questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: "
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich")
)

answers = ("C", "D")

score = 0

for i in range(len(questions)):
    print(questions[i])
    for option in options[i]:
        print(option)
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    if user_answer == answers[i]:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect.\n")

print(f"Your score: {score}/{len(questions)}")