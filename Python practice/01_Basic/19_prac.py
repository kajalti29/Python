# Let‘s Practice
#  WAP to check if a number entered by the user is odd or even.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")



#  WAP to check if a number is a multiple of 7 or not.
num = int(input("Enter a number: "))
if num % 7 == 0:
    print(num, "is a multiple of 7.")
else:
    print(num, "is not a multiple of 7.")


#  WAP to find the greatest of 3 numbers entered by the user.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    greatest = num1
elif (num2 >= num1) and (num2 >= num3):
    greatest = num2
else:
    greatest = num3
print("The greatest number is:", greatest)
