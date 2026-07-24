print("===== Smart Notes Organizer =====")

while True:
    print("\nMenu")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        note = input("Enter your note: ")

        file = open("notes.txt", "a")
        file.write(note + "\n")
        file.close()

        print("Note saved successfully!")

    elif choice == "2":
        try:
            file = open("notes.txt", "r")
            print("\n----- Your Notes -----")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("No notes found.")

    elif choice == "3":
        print("Thank you for using Smart Notes Organizer!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")