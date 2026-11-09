# add() method in set

collection={1,2,3,2,"hello","deva",None, 3+8j ,"deva"} # set is a mutable but their elements are immutable and it does not allow duplicate elements and it is unordered collection of elements and it does not support indexing and slicing because it is unordered collection of elements.so that we add tuple in set but we cannot add list and dictionary in set because list and dictionary are mutable and set does not allow mutable elements in it.
collection.add(4) 
collection.add("world") 
collection.add((1,2,3)) # it will add the tuple (1,2,3) in the set because tuple is immutable and set does not allow mutable elements in it.
#collection.add([1,2,3]) # it will give an error because list is mutable and set does not allow mutable elements in it.
#collection.add({"name":"deva"}) # it will give an error because dictionary is mutable
print(collection)
print(len(collection)) # it will print the number of unique elements in the set because set does not allow duplicate elements and it will not count the duplicate elements in the set.

print("\n") 

#remove() method in set

element_remove_set=collection.remove(2) # it will remove the element 2 from the set and if the element is not present in the set then it will give an error.
print(element_remove_set) # it will print None because remove() method does not return any value and it will remove the element from the set.
collection.remove("hello") # it will remove the element "hello" from the set and if the element is not present in the set then it will give an error.
collection.remove(None) # it will remove the element None from the set and if the element is not present in the set then it will give an error.
print(collection)

print("\n")

#clear() method in set

collection.clear() # it will remove all the elements from the set and it will make the set empty and if we try to print the set after using clear() method then it will print an empty set.
print(collection)  

print("\n")

#pop() method in set 

collection={1,3,2,7,"hello","deva",78}

collection.pop() # it will remove random value or element from set and return the set after removing random element because set is unordered collection of elements and it does not support indexing and slicing because it is unordered collection of elements.so that we cannot predict which element will be removed from the set when we use pop() method.and if the set is empty then it will give an error because there is no element to remove from the set when we use pop() method on an empty set.
print(collection)

print(collection.pop()) #it will give an random value or element from set which is removed from the set

print("\n")

# union() method in set

a={1,2,3,4}
b={3,4,5,6}
c={5,6,7,8}
d={7,8,6,9}

print(a.union(b)) # it will return a new set which is the union of set a and set b and it will not modify the original sets a and b.

new_union_set=c.union(d)# it will return a new set which is the union of set c and set d and it will not modify the original sets c and d.
print(new_union_set)

print("\n")

#intersection() method in set

a={1,2,3,4}
b={3,4,5,6}
c={5,6,7,8}
d={7,8,6,9}

print(a.intersection(b)) # it will return a new set which is the intersection of set a and set b and it will not modify the original sets a and b.

new_intersection_set=c.intersection(d) # it will return a new set which is the intersection of set c and set d and it will not modify the original sets c and d.
print(new_intersection_set)