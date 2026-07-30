<!-- What is python ? -->
Python is a high-level, interpreted programming language known for its simple syntax and powerful capabilities. 
It is used in Web Development, Data Science, Machine Learning, Automation, Testing, AI, etc. 

<!-- Features in python -->
* Easy to learn
* Interpreted language (Line-by-line execute hoti hai)
* Object-oriented (OOP support)
* Cross-platform (window, Linux, mac sab me chalta hai)
* Big libraries 

<!-- Why do you used python?
 -->
Python is used because it is easy to learn, powerful, and supports automation, data analysis, data visualization, web development, and machine learning
----------------------------------------------------------------------------------------------------------
<!-- Variable -->
A variable is a container used to store data(value) in python.
Syntax:
variable_name = value

<!-- name = "Kajal" //string
     age = 20       //it is a integer
     marks = 92.5   //it is a float
 --> 

<!--
name = "Kajalti"
age = 22
salary = 25000 

print(name)
print(age)
print(salary)
-->
Output:

Kajalti
22
25000

<!-- Data types in python -->
Data type define the type of data a variable can store - like number, text and true/false values etc.
<!-- 
age = 22

print(age)
print(type(age)) -->

* string:-Stores textual data (inside quotes).
<!-- 
name = "Kajalti"

print(name)
print(type(name))

 -->

* Int(integer):-Stores whole numbers (positive or negative).
<!-- a = 10
    b = -5 -->

* float:- store a decimal numbers
<!-- 
salary = 25000.50

print(salary)
print(type(salary)) -->

* boolean:- Logical values → only True or False.
<!-- 
is_student = True

print(is_student)
print(type(is_student))
-->
-------------------------------------------------------------
Type Conversion 
"Converting one data type to another data type."
Integer → String
<!-- 
age = "22"
new_age = int(age)
print(new_age)
print(type(new_age)) -->


-------------------------------------------------------------------------------------------------
<!-- Operators -->
"Operators are special symbols that are used to perform operations on variables and values."
<!-- 1. Arithmetic Operators (Math ke liye) -->
a = 10
b = 3

print(a + b)   # 13 
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333 
print(a % b)   # 1
print(a ** b)  # 1000

<!-- 2. Comparison Operators (Compare karne ke liye) -->
Do values ko compare karte hain.
| Operator | Meaning          | Example          |
| -------- | ---------------- | ---------------- |
| `==`     | Equal to         | `5 == 5` → True  |
| `!=`     | Not Equal        | `5 != 3` → True  |
| `>`      | Greater Than     | `5 > 3` → True   |
| `<`      | Less Than        | `5 < 3` → False  |
| `>=`     | Greater or Equal | `5 >= 5` → True  |
| `<=`     | Less or Equal    | `5 <= 3` → False |

a = 10
b = 5

print(a == b)  # False
print(a > b)   # True

<!-- 3. Logical Operators -->
Multiple conditions ko check karte hain.
| Operator | Meaning                            |
| -------- | ---------------------------------- |
| `and`    | Dono conditions True honi chahiye  |
| `or`     | Koi ek condition True honi chahiye |
| `not`    | Result ko ulta kar deta hai        |

age = 22

print(age > 18 and age < 30)  # True
print(age < 18 or age > 20)   # True
print(not(age > 18))          # False

<!-- 4. Assignment Operators -->
x = 10   # Assign value

x += 5   # x = x + 5
print(x) # 15

x -= 3   # x = x - 3
print(x) # 12
-------------------------------------------------------------------
<!-- 🔥 TOPIC 4 — Python Input & Output -->
Input is the process of taking data from the user, while Output is the process of displaying data on the screen." 
<!-- 
name = input("Enter your name: ")
print(name) -->

<!-- Data Analyst Example -->
sales = int(input("Enter sales: "))
print("Total Sales:", sales)

<!-- 7. Comments -->
Comments code ko explain karne ke liye use hote hain.

Single Line Comment
# This is sales data

sales = 50000

Python # ke baad wale text ko execute nahi karta.
 -----------------------------------------------------------------
 <!--TOPIC 5 — Conditional Statements (if, elif, else) -->
"Conditional statements are used to check conditions and make decisions in a program.

Example: If sales are greater than or equal to 50,000 → Target Completed. Otherwise → Target Not Completed."
 
 * if statement :- Runs code only when condition is True.

 <!--
age = 18
if age >= 18;
print("You are an adult")
  -->

* if-else statement :- Runs one block if condition is true, otherwise Another block.

<!-- 
age = 15
if age >= 18;
print("adult")
else
else("Not adult") 
-->

* if-elif-else statement :- check multiple conditions.
The elif statement is used to check multiple conditions.

<!-- Jab multiple condition check karna ho  -->

marks = 85

if marks >= 90:
   print("Grade A")
elif marks >= 75:
   print("Grade B")
elif marks > 60:
   print("Grade C")
else
   print("Grade F")


<!-- Nested if (if ke andar if) -->
if statement inside another if.

<!-- 
age = 20
has_id = True

if age >= 18:
   if has_id:
      print("Entry Allowed")
   else:
      print("ID Required") 
-->

🧠 Real-life Example (Samajhne ke liye best)

<!-- 
temp = 40

if temp > 35:
    print("It's too hot")
else:
    print("Weather normal") 
    
-->

Complete Example:
<!-- 
sales = int(input("Enter Sales: "))

if sales >= 100000:
    print("Excellent")
elif sales >= 50000:
    print("Good")
elif sales >= 25000:
    print("Average")
else:
    print("Low Sales") -->
----------------------------------------------------------------------------------------------------------
🔥 TOPIC 6 — LOOPS IN PYTHON (for & while)

<!-- What is Loop? -->
loop are used to repeat a block of code multiple times.

Example: If we want to print sales data 5 times, we can use a loop instead of writing the same code again and again.

✅ 1. for Loop:- A for loop is used to repeat code for each item in a sequence.
<!-- for i in range(1, 6):
     print(i)             o/p:-range(1,6) → 1 se 5 tak
     -->


<!-- 
fruits = ["apple", "banana", "mango"]

for item in fruits:
    print(item)


for i in range(5):
    print("Hello")
 -->

names = ["Kajalti", "Riya", "Neha"]
for name in names:
    print(name)

Output:

Kajalti
Riya
Neha

✅ 2. while Loop:-Repeats code until the condition becomes False.(Jab tak condition False nahi ho jati, tab tak repeat karta hain.)

<!-- i = 1
while i <=5:
      print(i)
      i += 1
    -->

⭐ Special Loop Keywords:-
Break :- Stop the loop immediately

<!--
for i in range(1, 10):
   if i == 5:
       break
      print(i)
 -->



3. range()
The range() function is used to generate a sequence of numbers.
It is commonly used with a for loop.

Example
<!-- 
for number in range(5):
    print(number)     -->

0
1
2
3
4


range(start, stop, step)
for number in range(1, 10, 2):
    print(number)

Output:

1
3
5
7
9
Syntax
range(start, stop, step)
Value	Meaning
start	Starting number
stop	Ending limit
step	Difference between numbers


4. break
The break statement is used to stop a loop immediately.

Example
for number in range(1, 6):

    if number == 3:
        break

    print(number)

Output:

1
2

5. continue:- skip current iteration.

<!-- 
for i in range(1, 6):
    if i == 3:
        continue
    print(i) 
    -->
------------------------------------------------------------------------------
<!-- 4. Python Data Structures ⭐ -->
Python data structures are used to store and organize multiple values.
The main data structures are:
List, Tuple, Set, and Dictionary

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

Data Analyst Example
<!-- 
cities = ["Indore", "Bhopal", "Ujjain"]
print(cities) -->

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

<!-- Descending Order -->

sales.sort(reverse=True)
print(sales)

Output:
[50000, 40000, 20000, 10000]
----------------------------------------------------------------------------------------
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

<!-- Tuple Indexing  -->
Tuple indexing also starts from 0.
<!-- 
cities = ("Indore", "Bhopal", "Ujjain")
print(cities[0]) -->

Output:
Indore

<!-- Negative Indexing -->
print(cities[-1])

Output:
Ujjain

| List                | Tuple                           |
| ------------------- | ------------------------------- |
| Uses `[]`           | Uses `()`                       |
| Changeable          | Unchangeable                    |
| Mutable             | Immutable                       |
| Can add/remove data | Cannot directly add/remove data |

-----------------------------------------------------------------------------------
3. Set :- A set is used to store unique values.
A set automatically removes duplicate values.

<!-- Create a Set -->
Set are created using curly brackets {}.
<!-- 
cities = {"Indore", "Bhopal", "Indore", "Ujjain"}
print(cities) -->

* add() : The add() method is used to add a value to a set.
<!-- 
cities = {"Indore", "Bhopal"}
cities.add("Ujjain")
print(cities) -->

* remove() : 
The remove() method is used to remove a value from a set.

cities = {"Indore", "Bhopal", "Ujjain"}
cities.remove("Bhopal")
print(cities)

* Union:- Union combines all unique values from two sets. The union operator is |.
<!-- 
set1 = {"Indore", "Bhopal"}
set2 = {"Bhopal", "Ujjain"}
result = set1 | set2
print(result) -->

Indore
Bhopal
Ujjain

*Intersection:- Intersection returns common values from two sets.The intersection operator is &.
<!-- 
set1 = {"Indore", "Bhopal"}
set2 = {"Bhopal", "Ujjain"}
result = set1 & set2
print(result) -->

Output:- 
{'Bhopal'}
-------------------------------------------------------------------
4. Dictionary:- 
A dictionary stores data in key-value pairs.
<!-- 
employee = {
    "name": "Kajalti",
    "age": 22,
    "salary": 25000
}

print(employee) -->


* Key and Value :-
A key is used to identify data.
A value is the actual data stored with the key.
Access a Value

<!-- employee = {
    "name": "Kajalti",
    "salary": 25000
}

print(employee["name"]) -->

* keys() :- 
The keys() method returns all dictionary keys.
<!-- 
employee = {
    "name": "Kajalti",
    "age": 22,
    "salary": 25000
}
print(employee.keys()) -->

Output:

dict_keys(['name', 'age', 'salary'])


* values() :-
The values() method returns all dictionary values.

<!-- print(employee.values()) -->

Output:
dict_values(['Kajalti', 22, 25000])

* items() :-
The items() method returns keys and values together.

<!-- print(employee.items()) -->


* Add Data :-A new key-value pair can be added to a dictionary.
<!-- 
employee = {
    "name": "Kajalti",
    "salary": 25000
}
employee["city"] = "Indore" 
print(employee)
-->

* Update Data :- We can update a value using its key.

<!-- employee = {
    "name": "Kajalti",
    "salary": 25000
}
employee["salary"] = 30000
print(employee) -->

Output:

{'name': 'Kajalti', 'salary': 30000}
-------------------------------------------------------------------------------------------------------------
🔥 TOPIC 7 — FUNCTIONS IN PYTHON:-
<!-- ⭐ What is a Function? -->
A function is a block of reusable code that performs a specific task.

<!-- ⭐ Why use Functions? (Benefits) -->
* Reduce code repetition
* Increase readability
* Divide big programs into smaller parts 

<!-- ⭐ 1. Creating a Function -->

2. def :-
The def keyword is used to create or define a function.
<!--
syntax:-

def function_name():
    # code    
-->


<!-- 
def greet():
    print("Hello Python")
 -->

---------------------------------------------------------------------------------------------------------------
<!-- ⭐ 2.Parameters (arguments) -->
Parameters are variables written inside the function definition.

<!--
 def greet(name)
    print("Hello", name)

greet("kajalti")  // Hello kajalti

-->
name is a parameters.


<!-- 4. Arguments  -->
Arguments are the actual values passed to a function when calling it.

<!-- 
def greeting(name):
    print("Hello", name)

greeting("Kajalti") -->

Here:
name
is a parameter.

"Kajalti"
is an argument.
--------------------------------------------------------------------------------------------------------------
<!-- ⭐ 3. Function With Return Value -->
return function se value wapas deta hai.
<!-- 
def add(a, b):
    return a + b

result = add(5, 3)
print(result) -->
--------------------------------------------------------------------------------------------------------------

<!-- ⭐ 4. Default Parameters -->

If you don’t pass a value, default will be used.
<!-- 
def greet(name="User"):
    print("Hello", name)

greet()          # Hello User
greet("Kajal")   # Hello Kajal -->


----------------------------------------------------------------------------------------------------------
<!-- ✔ Strings (very important) -->
A string is a sequence of characters enclosed in quotes. It is an Immutable.
<!--
name = "Kajal"
city = 'Indore'
message = '''Welcome to Python'''
print(name) 
-->

<!-- 🔤 STRING METHODS (Very Important) -->
* lower()
* upper()
* title()
* strip()
* replace()
* split()
* join()
* find()

⭐ 1. lower() :- Converts string to lowercase.
<!--
str = "PYTHON"
print(str.lower())
 -->
⭐ 2. upper() :-  Converts string to uppercase
<!-- 
s = "python"
print(s.upper())
 -->
⭐ 3. title() :- First letter of each word capital(Har word ka pehla letter capital)
<!-- 
s = "python is easy"
print(s.title()) 
-->

⭐ 4. capitalize() :- First letter capital (only first word)
<!-- 
s = "python is easy"
print(s.capitalize())
 -->

⭐ 5. strip() :- Removes spaces from both sides(Aage aur piche ke spaces hata deta hai)
<!-- 
s = "  hello  "
print(s.strip())
 -->

⭐ 6. replace() :- Replace old word with new.
<!-- 
s = "I love Java"
print(s.replace("Java", "Python"))
 -->

 ⭐ 7. find() :- Finds index of character/word
Hindi: Character ya word ka index batata hai.
<!-- 
s = "Python"
print(s.find("t"))  # 2
 -->

 ⭐ 8. split() :- Converts string into list.
<!-- 
 s = "Python is easy"
print(s.split())
 -->

 ⭐ 9. join() :- Joins list items into string
<!-- 
 words = ["Python", "is", "fun"]
print(" ".join(words))
 -->

✔ split() → string → list
✔ join() → list → string

⭐ 10. count() :- Counts occurrence
Hindi: Kitni baar aaya hai.
<!-- 
s = "banana"
print(s.count("a")) 
-->

----------------------------------------------------------------------------------------------------------------
<!-- 7. File Handling in Python -->
File handling is used to read, write, and update data in files.

For a Data Analyst, file handling is useful when working with TXT and CSV files.

1. open() :-
The open() function is used to open a file in Python.

<!-- open("file_name", "mode") -->

Common file modes:-
| Mode  | Meaning           |
| ----- | ----------------- |
| `"r"` | Read file         |
| `"w"` | Write file        |
| `"a"` | Append data       |
| `"x"` | Create a new file |

<!-- 2. Read File:-  -->
Reading a file means getting data from an existing file.
The "r" mode is used to read a file.
<!-- 
file = open("data.txt", "r")
data = file.read()
print(data)
file.close() -->

<!-- 3. read() -->
The read() method is used to read the complete content of a file.
<!-- 
file = open("data.txt", "r")
data = file.read()
print(data)
file.close() -->

<!-- 4. Write File -->
Writing a file means adding new data to a file.
The "w" mode is used to write data.

Example
<!-- 
file = open("data.txt", "w")
file.write("Python for Data Analysis")
file.close() -->

<!-- 5. write() -->
The write() method is used to write text into a file.
<!-- 
file = open("sales.txt", "w")
file.write("Total Sales: 50000")
file.close() -->


<!-- 
file = open("sales.txt", "w")
file.write("Indore: 50000\n")
file.write("Bhopal: 30000\n")
file.write("Ujjain: 20000")
file.close() -->

file contains:

Indore: 50000
Bhopal: 30000
Ujjain: 20000

\n means new line


------------------------------------------------------------------------
<!-- WHAT IS AN EXCEPTION? -->
An exception is a runtime error that stops the normal flow of a program.

<!-- Exception Handling --> 
try
except
else
finally


<!--⭐ TRY – EXCEPT -->
<!-- 
try:
    # risky code
except:
    # error handling code -->


<!-- ✔ Example 1: Divide by zero -->
<!-- 
try:
    a = 10
    b = 0
    print(a / b)
except:
    print("Cannot divide by zero") -->

try   → risky code
except → error ka solution


<!-- ⭐ else block (bahut easy) -->

else tab chalta hai jab koi error nahi hota
<!-- 
try:
    x = int(input("Enter number: "))
    print(10 / x)
except:
    print("Error aaya")
else:
    print("Sab kuch sahi chala") -->
------------------------------------------------------------------------------------------------------------------

<!-- ⭐ finally block (yaad rakhna) -->
finally hamesha chalta hai(Error ho ya na ho → finally pakka chalega)

<!-- try:
    print(10 / 2)
except:
    print("Error")
finally:
    print("Program end") -->

✔ Output:
5.0
Program end

-------------------------------------------------------------------------------------------------------------------------
📦 PART : Modules & Packages -->
A module is a file that contains Python code (functions, variables, classes).


Module ek Python file hoti hai jisme functions, variables ya classes hote hain.

<!-- 
import math
print(math.sqrt(16))
 -->

⭐ WHY MODULES?

Code reuse
Better organization
Easy maintenance

---------------------------------------------------------------------------------------------------------------------------------
📦 WHAT IS A PACKAGE?

A package is a folder that contains multiple modules.

Package ek folder hota hai jisme multiple Python files (modules) hote hain.

<!--
 ⭐ REAL-LIFE ANALOGY

📦 Package = Library
📄 Module = Book
📃 Function = Chapter 
-->

---------------------------------------------------------------------------------------------------------------------------------

<!-- 🧱 OOP in Python (Very Important) -->

OOP(object-Oriented Programming) is a programming approach based on objects and classes.
It helps in writing clean, reusable and secure code.


<!-- ⭐ Why OOP? (Why we use it) -->
* Code reusability
* Better structure
* Easy maintenance
* Security

<!-- 🧱 4 Pillars of OOP -->
1️⃣ Class & Object
2️⃣ Encapsulation
3️⃣ Inheritance
4️⃣ Polymorphism
(+ Abstraction)


<!-- 🧱 1. Class & Object :-  -->

* Class :- 

A class is a blueprint or template that defines the properties (variables) and behaviors (methods/functions) of an object.
It does not occupy memory until an object is created(Jab tak object create nahi hota, class memory me jagah nahi leti.)
<!-- 
Ex:-
class Student:
    def study(self):
        print("Student is studying") -->

<!-- 
Ex:-
class Student:
    name = "Kajal"
    age = 20

 -->

* Object :- 

An object is a real instance of a class that occupies memory and can use the class’s data and methods.

Hindi:
Object class ka real example (instance) hota hai jo memory leta hai aur class ke functions aur variables use karta hai.

s1 = Student()   # object create
s1.study()      # method call

<!-- 🔹 Output: -->
Student is studying

---------------------------------------------------------------------------------------------------------------------------

3️⃣ Constructor (__init__)

Constructor is a special method that runs automatically when an object is created.

Constructor ek special function hota hai jo object bante hi automatically call hota hai.

<!-- 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Kajal", 20)
print(s1.name, s1.age)
 -->

---------------------------------------------------------------------------------------------------------------------

<!-- 🧱 2. Encapsulation :-  -->

Encapsulation is the process of wrapping data and methods into a single unit and restricting direct access to data. It improves data security and code maintainability.

<!-- Real-Life Example -->
ATM machine:

Aap directly bank ka balance change nahi kar sakte

----------------------------------------------------------------------------------------------------------------

<!-- 3.🧱 Inheritance in Python-->

👉 It helps in code reusability.

----------------------------------------------------------------------------------------------------------------------

<!-- 4. Polymorphism -->

Polymorphism means same function name, different behavior. 
Polymorphism ka matlab ek hi method ka alag-alag kaam karna.
<!-- 
class Dog:
    def sound(self): //sound is a method
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

d = Dog()
c = Cat()

d.sound()
c.sound() -->

Ek hi method sound()
lekin Dog me Bark
aur Cat me Meow