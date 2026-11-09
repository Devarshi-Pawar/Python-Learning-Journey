# Break statement 

boys_name=["deva","rohan","sahil","adved","akhilesh"]

x=input("Select one boy from given list:")

index=0

while (index<len(boys_name)):
    if (boys_name[index]==x):
        print(x,"found at index no",index)
        break # break statement stop the work of loop and exit from loop and skip all next steps 

    print(boys_name[index])
    index=index+1

print("\n")

# continue statement 

girls_name=["arpita","prajakta","prachi","tanushree","arya"]

x=input("select one favourite girl name from given girls name list:")

index=0

while index<len(girls_name):
    if (girls_name[index]==x):
        index=index+1
        continue

    print(girls_name[index])
    index=index+1

    


    

