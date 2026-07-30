
# String Methods in Python
# Uppercase: Converts all characters in the string to uppercase.
# String ko uppercase me convert karta hai.
name = "kajalti sirame"
print(name.upper())  # Output: KAJALTI SIRAME

# Lowercase: Converts all characters in the string to lowercase.
# String ko lowercase me convert karta hai.
name = "KAJALTI SIRAME"
print(name.lower())  # Output: kajalti sirame

# title() :- Har word ka first letter capital kar deta hai.
name = "kajalti sirame"
print(name.title())  # Output: Kajalti Sirame

# capitalize() :- Sirf first letter capital banata hai.
name = "kajalti sirame"
print(name.capitalize())  # Output: Kajalti sirame

# strip() :- String ke starting & ending se extra spaces hata deta hai.
msg = "   Hello, World!   "
print(msg.strip())  # Output: Hello, World!

# replace() :- String ke andar ek character ya substring ko doosre character ya substring se replace kar deta hai.
msg = "Hello, World!"
print(msg.replace("World", "Python"))  # Output: Hello, Python!

# split() :- String ko ek list me convert kar deta hai based on a specified delimiter (default space).
msg = "Hello, World! Welcome to Python."
print(msg.split())  # Output: ['Hello,', 'World!', 'Welcome', 'to', 'Python.']

# join() :- Ek list ke elements ko ek string me join kar deta hai with a specified separator.
words = ['Hello', 'World', 'from', 'Python']
print(' '.join(words))  # Output: Hello World from Python

# find() :- String me kisi substring ka index return karta hai. Agar substring nahi milta to -1 return karta hai.
msg = "Hello, World!"
print(msg.find("World"))  # Output: 7
print(msg.find("Python"))  # Output: -1

# index() :- String me kisi substring ka index return karta hai. Agar substring nahi milta to error raise karta hai.
msg = "Hello, World!"
print(msg.index("World"))  # Output: 7
# print(msg.index("Python"))  # This will raise a ValueError

# startswith() :- Check karta hai string kis se start hoti hai.
msg = "Hello, World!"
print(msg.startswith("Hello"))  # Output: True
print(msg.startswith("World"))  # Output: False

# endswith() :- Check karta hai string kis se end hoti hai.
msg = "Hello, World!"
print(msg.endswith("World!"))  # Output: True
print(msg.endswith("Hello"))  # Output: False

# count():- Substring kitni baar aaya hai.
msg = "Hello, World! Welcome to the World of Python."
print(msg.count("World"))  # Output: 2

# isdigit():- Check karta hai string sirf digits hai ya nahi.
num_str = "12345"
print(num_str.isdigit())  # Output: True
alpha_str = "Hello123"
print(alpha_str.isdigit())  # Output: False

# isalpha():- Check karta hai string sirf alphabets hai ya nahi.
alpha_str = "Hello" 
print(alpha_str.isalpha())  # Output: True
alnum_str = "Hello123"
print(alnum_str.isalpha())  # Output: False

# center():- String ko center me align karta hai with specified width.
msg = "Hello"
print(msg.center(20, '-'))  # Output: -------Hello--------
