<!-- What is Python? -->
Python is a high-level, easy-to-read programming language used for:
Data Analysis ✅
Data Science
Machine Learning
Automation
Web Development

For a Data Analyst, Python is mainly used to:

Read Excel/CSV files
Clean data
Analyze data
Create charts
Find insights

<!-- Features in python -->
* Easy to learn
* Interpreted language (Line-by-line execute hoti hai)
* Object-oriented (OOP support)
* Cross-platform (window, Linux, mac sab me chalta hai)
* Big libraries 


<!-- Topic 2: Why Python for Data Analysts? -->
Example:
Suppose you have an Excel file with 10 lakh (1 million) rows.
Excel becomes slow.

Python can:
Read the file quickly
Remove duplicate data
Fill missing values
Calculate sales
Create charts
Generate reports
That's why companies use Python.

<!-- Q2. Why is Python popular for Data Analysis? -->
Answer: It has powerful libraries like Pandas, NumPy, and Matplotlib that make working with data fast and easy.

<!-- Topic 4: Comments -->
Comments are ignored by Python. They help explain your code.
# This is a comment
print("Hello")

<!-- Topic 5: Variables -->
A variable is a container used to store data(value) in python.
<!-- 
name = "Kajalti"
age = 22
salary = 25000

print(name)
print(age)
print(salary) -->
Output:- 
Kajalti
22
25000

<!-- Topic 6: Data Types -->
Data type define the type of data a variable can store - like number, text and true/false values etc.
| Data Type | Example         |
| --------- | --------------- |
| int       | `25`            |
| float     | `85.5`          |
| str       | `"Python"`      |
| bool      | `True`, `False` |
<!-- 
age = 22
height = 5.2
name = "Kajalti"
is_student = True

print(type(age))
print(type(height))
print(type(name))
print(type(is_student)) -->

Output:- 
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>

<!-- Topic 7: Input -->
Take input from the user
<!-- 
name = input("Enter your name: ")
print("Hello", name) -->

Numeric Input
<!-- 
age = int(input("Enter your age: "))
print(age) -->

What is Type Casting?
Type casting means converting one data type into another.

<!-- Why is it important? -->
When you use input(), Python always stores the value as a string.

Example:
age = input("Enter your age: ")
print(age)
print(type(age))

22
<class 'str'>


If you want to do calculations, you need to convert it to an integer.
<!-- 
age = int(input("Enter your age: "))

print(age)
print(type(age)) -->

Output:
22
<class 'int'>

-----------------------------------------------------------------------
<!-- Topic 8: Basic Arithmetic -->
a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)

Output
15
5
50
2.0
-----------------------------------------------------------------------------
Module 2: Control Statements
Control statements decide which code runs.

<!-- 1. if Statement -->
Runs code only if the condition is True.

Data Analyst Example
<!-- 
sales = 60000
if sales > 50000:
    print("Target Achieved") -->


<!-- 2. if-else -->
Run one code if true atherwise run another
<!-- 
marks = 35
if marks >= 40:
    print("Pass")
else:
    print("Fail") -->


<!-- 3. elif -->
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

<!-- Output -->
Grade B    

<!-- 4. Nested if -->
An if inside another if.

age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")

-------------------------------------------------------------
 5. for Loop       
 Used to repeat code a fixed number of times.
<!-- 
 for i in range(5):
    print(i) -->

Output
0  
1
2
3
4    

Print numbers 1 to 10
<!-- 
for i in range(1, 11):
    print(i) -->

6. while Loop
Runs while the condition is True.    
<!-- 
i = 1

while i <= 5:
    print(i)
    i += 1 -->

 7. break
Stops the loop immediately.   
<!-- 
for i in range(1, 11):
    if i == 6:
        break
    print(i) -->

 Output
1
2
3
4
5   

8. continue :- Skips the current iteration.

for i in range(1, 6):
 if i == 3:
     continue
       print(i)
-------------------------------------------------------------------
Module 3: Functions ⭐⭐⭐⭐⭐

<!-- What is a Function? -->
A function is a reusable block of code that performs a specific task.

Instead of writing the same code again and again, you write it once and call it whenever needed.

<!-- Why do we use Functions? -->
Without a function:

print("Welcome")
print("Welcome")
print("Welcome")

With a function:
<!-- 
def greet():
    print("Welcome")

greet()
greet()
greet() -->
Output:
Welcome
Welcome
Welcome

<!-- Q2. What is the difference between parameters and arguments? -->
Parameters are variables defined in the function.
Arguments are the actual values passed when calling the function.

Example:
<!-- 
def greet(name):   # name is a parameter
    print(name)

greet("Kajalti")   # "Kajalti" is an argument -->

Topic 4: Function with Return
Instead of printing the result, a function can return it.
<!-- 
def add(a, b):
    return a + b
result = add(10, 20)
print(result) -->

Output:

30 

<!-- Topic 7: Lambda Function ⭐⭐⭐ -->
A lambda function is a short, one-line function.

Normal Function
<!-- 
def square(x):
    return x * x -->

Lambda Function
<!-- 
square = lambda x: x * x
print(square(5)) --> 

Output
25

------------------------------------------------------------------------------------------------------------
Module 4: Strings ⭐⭐⭐⭐⭐
<!-- Why are Strings important for Data Analysts? -->

Real datasets often contain text like customer names, cities, email addresses, product names, etc. Before analysis, you need to clean and process this text.

<!-- Topic 1: What is a String? -->
A string is a sequence of characters enclosed in single (' ') or double (" ") quotes.
<!-- 
name = "Kajalti"

print(name)
print(type(name)) -->

Output

Kajalti
<class 'str'>