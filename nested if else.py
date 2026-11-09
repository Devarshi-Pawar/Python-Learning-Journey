age=eval(input("enter your age: "))

if age>=18:
    if age>=18 and age<75:
        print("You are eligible to vote,and apply for driving license")
    else:
        print("You are eligible to vote but not eligible to apply for driving license")

else:
    print("You are not eligible to vote and apply for driving license")