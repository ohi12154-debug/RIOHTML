import random

dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

print(" Dice Rolling Simulator ")

while True:
    input("\nPress Enter to roll the dice...")

    number = random.randint(1, 6)

    print(f"\nYou rolled: {number}")
    print(f"Dice Face: {dice_faces[number]}")

    again = input("\nRoll again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing! ")
        break
