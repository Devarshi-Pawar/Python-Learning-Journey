# Q1) print the element of the following list using a for loop

list=[1,4,9,16,25,36,49,64,81,100]

for i in list :
    print(i)

print("\n")

# Q2) search for number x in a tuple using for loop

list=(1,4,9,16,25,36,49,64,81,100)

x=eval(input("enter the number which you want to findout in tuple:"))

index=0

for i in list:
    if (i==x):
        print(x,"number found at number:",index)
    else:
        print(i)
    
    index+=1
    