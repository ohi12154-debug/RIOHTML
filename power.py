# Power Series Program

x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

sum_series = 0

for i in range(n + 1):
    sum_series += x ** i

print("Sum of the power series =", sum_series)