print("===== File Handling Operations =====")

# Create and write to a file
file = open("sample.txt", "w")
file.write("Hello!\n")
file.write("Welcome to Python File Handling.\n")
file.write("This is a sample text file.")
file.close()

print("Data written successfully.\n")

# Read the file
file = open("sample.txt", "r")
print("File Contents:")
print(file.read())
file.close()

# Append new data
file = open("sample.txt", "a")
file.write("\nThis line is added using append mode.")
file.close()

print("\nData appended successfully.\n")

# Read the updated file
file = open("sample.txt", "r")
print("Updated File Contents:")
print(file.read())
file.close()