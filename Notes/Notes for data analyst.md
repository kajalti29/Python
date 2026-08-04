<!-- What is Python? -->
Python is a high-level, interpreted, easy-to-read programming language.
It is widely used in Data Analytics, Data Science, Machine Learning, automation and Web Development

As a Data Analyst, I use Python to clean, analyze, manipulate, and visualize data using libraries like Pandas, NumPy, and Matplotlib

<!-- Features in python -->
* Easy to learn
* Interpreted language (Line-by-line execute hoti hai)
* Object-oriented (OOP support)
* Cross-platform (window, Linux, mac sab me chalta hai)
* Big libraries 


<!-- 2. Why is Python used in Data Analytics? -->
Python is used in Data Analytics because it makes data cleaning, data manipulation, analysis, and visualization easier. It has powerful libraries such as Pandas, NumPy, Matplotlib, and Seaborn.

<!-- 3. What are the advantages of Python? -->
The main advantages of Python are:

Easy to learn and understand 
Simple and readable syntax
Open-source and free
Large number of libraries
Useful for data analysis and visualization


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

<!-- 5. What are the different data types in Python? -->
Common Python data types are:

int → Integer numbers
float → Decimal numbers
str → Text/String
bool → True or False
list → Ordered and changeable collection
tuple → Ordered and unchangeable collection
dict → Key-value pairs
set → Unordered collection of unique values

<!-- 6. Difference between int, float, str, and bool -->
Interview Answer:
"int stores whole numbers, float stores decimal numbers, str stores text, and bool stores either True or False."

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

<!-- 8. What is the difference between = and ==? -->
= is the assignment operator. It is used to assign a value to a variable.
== is the comparison operator. It is used to checks whether two values are equal.

Example:
age = 22
Here, = assigns 22 to age.

age == 22
This checks whether age is equal to 22. The result will be True.
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
A string is a sequence of characters enclosed in quotes.
<!-- 
name = "Kajalti"

print(name)
print(type(name)) -->

Output

Kajalti
<class 'str'>

<!-- Topic 2: String Indexing -->
text = "Python"
print(text[0])
print(text[2])
print(text[5])

Output
P
t
n

<!-- Negative Indexing -->
Python
P   y   t   h   o   n
-6 -5 -4 -3 -2 -1
<!-- 
text = "Python"
print(text[-1])
print(text[-2]) -->

Output 
n
o


<!-- 4. String Methods ⭐⭐⭐⭐ -->
(a) Upper()
<!-- 
name = "kajalti"
print(name.upper()) -->

(b) Lower()
<!-- 
name = "KAJALTI"
print(name.lower()) -->

(c) Title()
<!-- 
text = "data analyst"
print(text.title()) -->

(d) Capitalize()
<!-- 
text = "python"
print(text.capitalize()) -->

5. Split() ⭐⭐⭐⭐
<!-- 
text = "Python SQL Excel"
print(text.split()) -->
O/p
['Python', 'SQL', 'Excel']

6. Join() ⭐⭐⭐⭐
<!-- 
fruits = ["Apple", "Mango", "Banana"]
print(" ".join(fruits)) -->


----------------------------------------------------------------------------------------------------------
1. List:- A list is used to store multiple values in a single variable.
A list is ordered and changeable (mutable).

* Create a List
Lists are created using square brackets [].  

<!-- list_name = [value1, value2, value3] --> 

Example 
<!-- 
sales = [50000, 30000, 45000, 60000]
print(sales) -->

Output:
[50000, 30000, 45000, 60000]

*Indexing:-
Indexing is used to access a specific value from a list.
Python indexing starts from 0.
Index      0         1         2
          Indore    Bhopal    Ujjain
<!-- 
cities = ["Indore", "Bhopal", "Ujjain"]
print(cities[0])
print(cities[1])       -->

Output:
Indore
Bhopal

*Negative Indexing:-
Negative indexing starts from the end.
<!-- 
cities = ["Indore", "Bhopal", "Ujjain"]
print(cities[-1]) -->

Ujjain


*Slicing :- Slicing is used to access multiple values from a list.
Syntax:- 
list[start:stop]

<!-- 
sales = [10000, 20000, 30000, 40000, 50000]
print(sales[1:4]) -->

Output:
[20000, 30000, 40000]
The stop index is not included.

* append():- The append() method is used to add an item at the end of a list.
<!-- 
cities = ["Indore", "Bhopal"]
cities.append("Ujjain")
print(cities) -->

insert():- The insert() method is used to add an item at a specific position.
<!-- 
cities = ["Indore", "Ujjain"]
cities.insert(1, "Bhopal")
print(cities) -->

* pop():-
The pop() method is used to remove an item using its index.
<!-- 
cities = ["Indore", "Bhopal", "Ujjain"]
cities.pop(1)
print(cities) -->

* remove() :- The remove() method is used to remove a specific value from a list.
<!-- 
cities = ["Indore", "Bhopal", "Ujjain"]
cities.remove("Bhopal")
print(cities) -->


* sort() :- The sort() method is used to sort list values.
<!-- Ascending Order -->
<!-- 
sales = [50000, 20000, 40000, 10000]
sales.sort()
print(sales) -->

Output:
[10000, 20000, 40000, 50000]
---------------------------------------------------
2. Tuple
A tuple is used to store multiple values in a single variable.
A tuple is ordered but unchangeable (immutable).

<!-- Create a Tuple -->
Tuples are created using parentheses ().
<!-- 
cities = ("Indore", "Bhopal", "Ujjain")
print(cities) -->

Output:
('Indore', 'Bhopal', 'Ujjain')
---------------------------------------------------
11. Sets ⭐⭐⭐⭐
 A set is used to store unique values.
A set automatically removes duplicate values.
<!-- 
numbers = {1, 2, 2, 3, 4, 4}
print(numbers) -->

Output

{1, 2, 3, 4}
---------------------------------------------------------
12. Dictionaries ⭐⭐⭐⭐⭐
A dictionary is a collection of data stored in key-value pairs.
<!-- 
employee = {
    "name": "Kajalti",
    "age": 22,
    "salary": 25000
}

print(employee) -->
--------------------------------------------------------------------------------------------------------
<!-- 4. Difference between List, Tuple, Set, and Dictionary. -->
| Feature     | List      | Tuple     | Set         | Dictionary     |
| ----------- | --------- | --------- | ----------- | -------------- |
| Syntax      | `[]`      | `()`      | `{}`        | `{key: value}` |
| Ordered     | Yes       | Yes       | No          | Yes*           |
| Mutable     | Yes       | No        | Yes         | Yes            |
| Duplicates  | Allowed   | Allowed   | Not allowed | Keys: No       |
| Data Access | Index     | Index     | No indexing | Key            |
| Example     | `[1,2,3]` | `(1,2,3)` | `{1,2,3}`   | `{"a":1}`      |

<!-- 5. What is Indexing? -->
Indexing means accessing an individual element from a sequence using its position.
Python indexing starts from 0.
<!-- 
sales = [1000, 2000, 3000]
print(sales[0]) -->

<!-- 6. What is Slicing? -->
Slicing means extracting a specific portion of a sequence.

Syntax:
list[start:stop]
<!-- 
sales = [1000, 2000, 3000, 4000, 5000]
print(sales[1:4]) -->

Output:
[2000, 3000, 4000]
The stop index is not included.

7. What is a Mutable and Immutable Data Type?
<!-- Mutable: -->
A data type whose value can be changed after creation.

Examples:
List
Dictionary
Set
sales = [1000, 2000]
sales[0] = 1500

<!-- Immutable: -->
A data type whose value cannot be changed after creation.

Examples:
Integer
Float
String
Tuple
Boolean
name = "Kajal

<!-- 8. What is a For Loop? -->
<!-- 10. Difference between For and While Loop -->
Used to repeat code a fixed number of times.
Runs while the condition is True.    


<!-- 11. What are break, continue, and pass? -->
<!-- break -->
Stops the loop completely.

for i in range(5):
    if i == 3:
        break
    print(i)

<!-- continue -->
Skips the current iteration.

for i in range(5):
    if i == 3:
        continue
    print(i)

<!-- 12. What is a Function?     -->
A function is a reusable block of code that performs a specific task.

<!-- How do you create a Function in Python? -->
We create a function using the def keyword.
<!-- 
def calculate_total(a, b):
    return a + b
result = calculate_total(100, 200)
print(result)
 -->

Output:
300
Here, calculate_total() is a function

<!-- 14. What are Function Arguments? -->
Arguments are the actual values that we pass to a function when we call it.
<!-- 
def calculate_total(a, b):
    return a + b
calculate_total(100, 200) -->


<!-- 15. Difference between Parameter and Argument -->
Parameter:
A variable defined in the function definition.

Argument:
The actual value passed to the function when calling it.
<!-- 
def greet(name):    # name is a parameter
    print(name)

greet("Kajal")      # "Kajal" is an argument -->


<!-- 16. What is a Lambda Function? -->
A lambda function is a small anonymous function written in a single line using the lambda keyword.
<!-- 
square = lambda x: x * x
print(square(5)) -->

Output:
25

<!-- 17. What is List Comprehension? -->