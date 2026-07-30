# ✅ What is Recursion?
# Recursion ek programming technique hai jisme ek function khud ko call karta hai.
# Iska use complex problems ko chhote-chhote sub-problems me todne ke liye kiya jata hai.
# Recursion do parts me hota hai:
# 1. Base Case: Ye condition hoti hai jisme recursion stop ho jataa hai.
# 2. Recursive Case: Ye part hota hai jisme function khud ko call karta hai with modified arguments.


# Jab ek function khud ko hi dubara call kare, isko recursion kehte hain.
def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Case
    else:
        return n * factorial(n - 1)
# Testing the factorial function
num = 5 
print(f"The factorial of {num} is {factorial(num)}")  # Output: The factorial of 5 is 120