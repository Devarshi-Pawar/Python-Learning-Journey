"""
write a program to enter marks of 3 subjects from the user and store them in dictionary .
start with an empty dictionary and add one by one . use subject name as key and marks as value.
"""

subject={}

for i in range(3):
    subject_name=input("Enter the subject name:")
    marks=eval(input("Enter the marks of the subject:"))
    subject.update({subject_name:marks})
    print("\n")

print(subject)

print("\n")
print("\n")

# another way 

marks={}

x=eval(input("enter physics marks:"))
marks.update({"physics":x})

x=eval(input("enter chemistry marks:"))
marks.update({"chemistry":x})   

x=eval(input("enter mathematics marks:"))
marks.update({"mathematics":x})

print(marks)
