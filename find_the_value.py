# Find the Value Project

print("=== Find the Value ===")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    value = a + b
    print("Value =", value)

elif choice == "2":
    value = a - b
    print("Value =", value)

elif choice == "3":
    value = a * b
    print("Value =", value)

elif choice == "4":
    if b != 0:
        value = a / b
        print("Value =", value)
    else:
        print("Division by zero is not possible.")

else:
    print("Invalid choice!")