print("===== Create a Slam Book =====")

slam_book = []

while True:
    print("\nMenu")
    print("1. Add a Friend")
    print("2. View Slam Book")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print("\nEnter Friend Details")
        name = input("Name: ")
        age = input("Age: ")
        favorite_color = input("Favorite Color: ")
        favorite_food = input("Favorite Food: ")
        hobby = input("Hobby: ")
        dream_job = input("Dream Job: ")

        friend = {
            "Name": name,
            "Age": age,
            "Favorite Color": favorite_color,
            "Favorite Food": favorite_food,
            "Hobby": hobby,
            "Dream Job": dream_job
        }

        slam_book.append(friend)
        print("Friend added successfully!")

    elif choice == "2":
        if len(slam_book) == 0:
            print("The slam book is empty.")
        else:
            print("\n===== Slam Book =====")
            for i in range(len(slam_book)):
                print("\nFriend", i + 1)
                print("Name           :", slam_book[i]["Name"])
                print("Age            :", slam_book[i]["Age"])
                print("Favorite Color :", slam_book[i]["Favorite Color"])
                print("Favorite Food  :", slam_book[i]["Favorite Food"])
                print("Hobby          :", slam_book[i]["Hobby"])
                print("Dream Job      :", slam_book[i]["Dream Job"])

    elif choice == "3":
        print("Thank you for using Create a Slam Book!")
        break

    else:
        print("Invalid choice! Please try again.")