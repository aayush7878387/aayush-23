# program to  print table of any number
base = int(input("enter any number"))

for i in range(1, 11):
    result = base * i
    print(f"{base} x {i} = {result}")


# sum of 2 num
a = float(input("enter your first number"))
b = float(input("enter your second number"))

sum = (a + b)
print("your_sum_is = ", sum)


# reverse a string . write a one-liner to reverse the string "developer"using slicing

print("developer"[::-1])

# [::-1] is a slicing techniquw where first two colons mean from start to end and -1 means go backwards
# Output: 'repoleved'


# program to find the square of a number
num = float(input("enter a number:"))


square = num ** 2

print("square of your", num, "is:", square)


# program to calculate simple interest
principle = int(input("enter your pinciple"))
rate = int(input("eter your rate of interest (in %)"))
time = int(input("enter your time (in years)"))

simple_interest = (principle * rate * time) / 100
print("simple interest =", simple_interest)

# program to find the remainder of a number when divided by 2
number = int(input("enter your number"))

remainder = number % 2

print("remainder =", remainder)

# checking the type of variable whether it's int, float or str
assigned_variable = input("enter anything: ")
print("you entered:", assigned_variable)
print("type of assigned_variable is:", type(assigned_variable))

# program to compare two numbers using comparison operator
a = 34
b = 80

if a > b:
    print(f"{a} is greater than {b}")

else:
    print(f"{a} is not greater than {b}")

# program to print the user's name followed by good afternoon
name = input("enter your name:")

print(f"{name} good afternoon")

# program to calculate the average of two numbers
first_number = float(input("enter your first number:"))
second_number = float(input("ener your second number:"))
average = (first_number + second_number) / 2

print("agerage is:", average)
