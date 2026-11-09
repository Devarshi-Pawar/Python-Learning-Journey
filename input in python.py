a=input("enter the value of a: ")
b=input("enter the value of b: ")   
print("Addition:", a + b)   # here the output will be 23 because the input function takes the input as a string and when we add two strings it concatenates them instead of performing arithmetic addition. To perform arithmetic addition, we need to convert the input values to integers or floats before adding them. For example:
a = eval(input("enter the value of a: "))
b = eval(input("enter the value of b: "))
print("Addition:", a + b)   