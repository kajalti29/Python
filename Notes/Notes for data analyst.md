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