list1=[1,2,3,2,1]

list1_copy=list1.copy() # create a copy of the original list
list1_copy.reverse()

if list1==list1_copy:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")


print("\n")
print("\n")

list2=[1,2,3,4]

list2_copy=list2.copy()
list2_copy.reverse()

if list2==list2_copy:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")


