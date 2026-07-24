print("===== My Jungle Explorer =====")
print("Welcome to the Jungle Adventure!")

print("\nYou are standing at the entrance of a jungle.")
print("Choose a path:")
print("1. Left Path")
print("2. Right Path")

choice1 = input("Enter your choice (1/2): ")

if choice1 == "1":
    print("\nYou found a beautiful river.")
    print("What do you want to do?")
    print("1. Cross the river")
    print("2. Follow the river")

    choice2 = input("Enter your choice (1/2): ")

    if choice2 == "1":
        print("\nYou safely crossed the river and found a hidden treasure! ")
    elif choice2 == "2":
        print("\nYou followed the river and discovered a peaceful waterfall. ")
    else:
        print("\nInvalid choice!")

elif choice1 == "2":
    print("\nYou met a wild tiger!")
    print("What do you want to do?")
    print("1. Climb a tree")
    print("2. Run away")

    choice2 = input("Enter your choice (1/2): ")

    if choice2 == "1":
        print("\nGreat! You climbed the tree and stayed safe. ")
    elif choice2 == "2":
        print("\nYou escaped safely and returned home. ")
    else:
        print("\nInvalid choice!")

else:
    print("\nInvalid choice!")

print("\nThanks for playing My Jungle Explorer! ")