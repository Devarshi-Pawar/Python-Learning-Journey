"""
figure out the way to store 9 and 9.0 as separate values in a set.
because you get two value in set as set={9,9.0} then it take as a same value and get only one value because set does not allow duplicate values and it will consider 9 and 9.0 as a same value .
"""

# first way to store 9 and 9.0 as separate values in a set is to convert 9.0 to a string and then add it to the set.
set_values = {9, "9.0"} 
print(set_values) # it will print {9, '9.0'} because 9 and "9.0" are considered as separate values in the set.

print("\n")

#second way to store 9 and 9.0 as a separate values in a set in the form of a tuple because tuple is an immutable data type and it can be added to the set as a separate value.
set_values1 = {(9.0,9)}
set_values2 = {("float",9.0),("int",9)}
print(set_values1) # it will print {9, (9.0,)} because
print(set_values2) # it will print {('float', 9.0), ('int', 9)} because ("float", 9.0) and ("int", 9) are considered as separate values in the set.