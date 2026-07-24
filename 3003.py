print("===== My Ocean World =====")
print("Welcome to the Ocean Adventure! ")

print("\nYou are in a submarine exploring the deep ocean.")
print("Choose where you want to go:")
print("1. Coral Reef")
print("2. Deep Sea")

choice1 = input("Enter your choice (1/2): ")

if choice1 == "1":
    print("\nYou reached a colorful coral reef filled with fish. ")
    print("What would you like to do?")
    print("1. Watch the fish")
    print("2. Collect a seashell")

    choice2 = input("Enter your choice (1/2): ")

    if choice2 == "1":
        print("\nYou enjoyed watching beautiful tropical fish! ")
    elif choice2 == "2":
        print("\nYou found a rare seashell! ")
    else:
        print("\nInvalid choice!")

elif choice1 == "2":
    print("\nYou entered the mysterious deep sea. ")
    print("What would you like to do?")
    print("1. Explore a shipwreck")
    print("2. Observe glowing jellyfish")

    choice2 = input("Enter your choice (1/2): ")

    if choice2 == "1":
        print("\nYou discovered an old treasure chest inside the shipwreck! ")
    elif choice2 == "2":
        print("\nThe glowing jellyfish created a beautiful light show! ")
    else:
        print("\nInvalid choice!")

else:
    print("\nInvalid choice!")

print("\nThank you for playing My Ocean World! ")