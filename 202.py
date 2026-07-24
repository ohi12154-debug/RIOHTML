print("===== Welcome to the Python Quiz =====")

score = 0

# Question 1
answer = input("1. What is the capital of Bangladesh?\n")
if answer.lower() == "dhaka":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Dhaka.\n")

# Question 2
answer = input("2. How many days are there in a week?\n")
if answer == "7":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 7.\n")

# Question 3
answer = input("3. Which keyword is used to display output in Python?\n")
if answer.lower() == "print":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is print.\n")

# Question 4
answer = input("4. What is 8 × 5?\n")
if answer == "40":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is 40.\n")

# Question 5
answer = input("5. Which planet is known as the Red Planet?\n")
if answer.lower() == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Mars.\n")

# Final Result
print("===== Quiz Finished =====")
print("Your Score:", score, "/5")

if score == 5:
    print("Excellent! You got all answers correct! ")
elif score >= 3:
    print("Good Job! ")
else:
    print("Keep Practicing! ")