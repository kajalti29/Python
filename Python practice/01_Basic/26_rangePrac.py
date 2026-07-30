#  Print numbers from 1 to 100. 
for i in range(1, 101):
    print(i)

 # Print the multiplication table of a number n. 
# n = int(input("Enter a number to print its multiplication table: "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
