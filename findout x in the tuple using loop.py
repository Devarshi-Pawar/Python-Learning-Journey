#search for the number x in the tuple using loop 

tup=(1,4,9,16,25,36,49,64,81,100)

x=eval(input("Enter the value of x which is want to findout their index:"))

if x in tup:

    index=0

    while index<len(tup):
        if (tup[index]==x):
            print(x,"Number Found at index:",index)

        index=index+1

else:
    print("you entered wrong value which not present in given tuple")