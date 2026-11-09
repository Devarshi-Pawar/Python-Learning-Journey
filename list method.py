list=[23,54,12]

list.append(55)
print(list)

print("\n")

list.sort() # sort the list in ascending order
print(list)

print("\n")

list.sort(reverse=True) # sort the list in descending order
print(list)

print("\n")

list.reverse() # reverse the order of the list
print(list) 

print("\n") 

list.insert(2, 100) # insert 100 at index 2
print(list)

print("\n")

list.remove(54) # remove the first occurrence of 54 from the list
print(list) 

print("\n") 

list.pop() # remove the last element from the list
print(list)

list.pop(1) # remove the element at index 1
print(list)