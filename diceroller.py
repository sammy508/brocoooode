
import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u25CF \u2514 \u2518")
# output ● ┌ ─ ┐ │ ●  ┘└

dice_art = {
    1:(
        "┌──────┐",
        "│      │",
        "│   ●  │",
        "│      │",
        "└──────┘"
    ),
    2: (
        "┌──────┐",
        "│   ●  │",
        "│      │",
        "│   ●  │",
        "└──────┘"
    ),

    3: (
        "┌──────┐",
        "│   ●  │",
        "│   ●  │",
        "│   ●  │",
        "└──────┘"
    ),
    4: (
        "┌──────┐",
        "│ ●  ● │",
        "│      │",
        "│ ●  ● │",
        "└──────┘"
    ),
    5: (
        "┌──────┐",
        "│ ●  ● │",
        "│   ●  │",
        "│ ●  ● │",
        "└──────┘"
    ),
    6: (
        "┌──────┐",
        "│ ●  ● │",
        "│ ●  ● │",
        "│ ●  ● │",
        "└──────┘"
    ),
}

dice = []

total = 0
num_of_dice = int(input ("enter num if dice : "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))


# it prints boxes in vertical

for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)

print()
print("for printing it on horizontal line \n")

for line in range(5):   # lines of tuples to make box
    for die in dice:    # num of dices enterd  and sorted into list 
        print(dice_art.get(die)[line], end= " ")
    print()

for die in dice : 
    total+= die
print(f"Total : {total}")


# error xa hai herna parne