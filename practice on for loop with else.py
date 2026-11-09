# using break
list=[2,4,6,7,3,77,25,5,32,6]

x=eval(input("enter the any number from give list :"))

for i in list :
    if i==x:
        break # exit and stop the work of loop 

    print(i)

else:
    print("THE END LOOP")

print("\n")


# using continue

list=[34,6,3,26,3,68,33,77,32,9]

x=eval(input('enter any number from given list:'))

for i in list:
    if i==x:
        continue
    print(i)

else:
    print("THE END")