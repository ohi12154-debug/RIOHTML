print("===== My Shopping List Manager =====")

shopping_list = []

while True:
    print("\nMenu")
    print("1. Add Item")
    print("2. View Shopping List")
    print("3. Remove Item")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(item, "has been added to your shopping list.")

    elif choice == "2":
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            print("\nYour Shopping List:")
            for i in range(len(shopping_list)):
                print(i + 1, ".", shopping_list[i])

    elif choice == "3":
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(item, "has been removed from your shopping list.")
            else:
                print("Item not found.")

    elif choice == "4":
        print("Thank you for using My Shopping List Manager!")
        break

    else:
        print("Invalid choice! Please try again.")