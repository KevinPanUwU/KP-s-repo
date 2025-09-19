import random

dice_art = {
    1: (
        "┌─────┐",
        "│     │",
        "│  ●  │",
        "│     │",
        "└─────┘"
    ),
    2: (
        "┌─────┐",
        "│ ●   │",
        "│     │",
        "│   ● │",
        "└─────┘"
    ),
    3: (
        "┌─────┐",
        "│ ●   │",
        "│  ●  │",
        "│   ● │",
        "└─────┘"
    ),
    4: (
        "┌─────┐",
        "│ ● ● │",
        "│     │",
        "│ ● ● │",
        "└─────┘"
    ),
    5: (
        "┌─────┐",
        "│ ● ● │",
        "│  ●  │",
        "│ ● ● │",
        "└─────┘"
    ),
    6: (
        "┌─────┐",
        "│ ● ● │",
        "│ ● ● │",
        "│ ● ● │",
        "└─────┘"
    )
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    roll = random.randint(1, 6)
    dice.append(roll)
    total += roll

print("\nYour rolls:")
for line in range(5):
    for roll in dice:
        print(dice_art[roll][line], end=" ")
    print()

print(f"Total: {total}")