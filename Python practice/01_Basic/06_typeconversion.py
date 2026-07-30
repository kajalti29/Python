# Type Conversion in Python ?
# Type conversion ka matlab hai — data ko ek type se doosre type me badal dena.
# Python me do tarah ke type conversion hote hain:
# 1. Implicit Type Conversion: Jab Python khud se ek data type ko doosre data type me convert kar deta hai bina kisi explicit instruction ke.
# 2. Explicit Type Conversion: Jab hum khud se ek data type ko doosre data type me convert karte hain using built-in functions jaise int(), float(), str(), etc.    
# Implicit Type Conversion Example
a = 5          # Integer
b = 2.5        # Float
result = a + b # Implicitly converts 'a' to float and then adds 
print(result)  # Output: 7.5

# Explicit Type Conversion Example
x = 10         # Integer
y = "20"       # String
y_int = int(y)
sum_result = x + y_int
print("Explicit Type Conversion Result:", sum_result)  # Output: 30
