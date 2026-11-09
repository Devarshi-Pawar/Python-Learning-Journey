# Arithmetic Operators
a = 3
b = 5       
print("Addition:", a + b)          # Output: 8
print("Subtraction:", a - b)       # Output: -2
print("Multiplication:", a * b)    # Output: 15
print("Division:", a / b)          # Output: 0.6 # Division gives the quotient as a float, even if both operands are integers.
print("Floor Division:", a // b)   # Output: 0 # Floor division gives the quotient without the decimal part.
print("Modulus:", a % b)           # Output: 3 # Modulus gives the remainder of the division of a by b.
print("Exponentiation:", a ** b)    # Output: 243 # Exponentiation raises a to the power of b, which is equivalent to multiplying a by itself b times. In this case, 3 raised to the power of 5 is 243 (3 * 3 * 3 * 3 * 3).

print("\n")

#Relational Operators
x = 10
y = 20
print("Equal to:", x == y)         # Output: False
print("Not equal to:", x != y)     # Output: True
print("Greater than:", x > y)      # Output: False
print("Less than:", x < y)         # Output: True
print("Greater than or equal to:", x >= y)  # Output: False
print("Less than or equal to:", x <= y)     # Output: True  

print("\n")

# Assignment Operators  
a = 10
a += 5  # Equivalent to a = a + 5
print("After += 5:", a)  # Output: 15
a -= 3  # Equivalent to a = a - 3
print("After -= 3:", a)  # Output: 12
a *= 2  # Equivalent to a = a * 2
print("After *= 2:", a)  # Output: 24
a /= 4  # Equivalent to a = a / 4
print("After /= 4:", a)  # Output: 6.0
a //= 2 # Equivalent to a = a // 2
print("After //= 2:", a) # Output: 3.0
a %= 2  # Equivalent to a = a % 2
print("After %= 2:", a)  # Output: 1.0
a **= 3 # Equivalent to a = a ** 3  
print("After **= 3:", a) # Output: 1.0 

print("\n")

# Logical Operators     
p = True
q = False
print("Logical AND (p and q):", p and q)  # Output: False
print("Logical OR (p or q):", p or q)     # Output: True
print("Logical NOT (not p):", not p)       # Output: False      

