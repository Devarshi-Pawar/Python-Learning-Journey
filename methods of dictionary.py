student={
    "name":"deva",
    "age": 20,
    "courses": ["Math", "Science", "English"],
    "cgpa":8.4
}

#keys() method in dictionary
keys=student.keys() 
print(keys) # it will print all the keys in the dictionary
print(list(keys)) # it will print all the keys in the dictionary in list format

print("\n")

#values() method in dictionary
values=student.values() 
print(values)# it will print all the values in the dictionary
print(list(values)) # it will print all the values in the dictionary in list format

print("\n")

#items() method in dictionary
items=((student.items()))#return all (key, value) pairs in the dictionary as a tuples.
print(items)

items=(list(student.items()))
print(items) # it will print all the (key, value) pairs in the dictionary as a list of tuples. Each tuple contains a key and its corresponding value from the dictionary.
print(items[1]) # it will print the second item in the list of tuples which is ('age', 20
print(len(list(student.items()))) # it will print the number of items in the dictionary

print("\n") 

#get() method in dictionary
print(student["name"]) # it will print the value of the key "name" which is "deva"
print(student.get("name")) # it will print the value of the key "name" which is "deva" 

"""
both the above code will give the same output but the difference is that if we try to access a key that does not exist in the dictionary using the first method it will give an error but using the get() method it will return None instead of giving an error.
and second get() method used as a pro coder because by mistake we take some value which does not exist in the dictionary then it will return None instead of giving an error and our program will not crash.
"""
print("\n")

# update() method in dictionary

student.update({"city":"Amravati"}) # it will add a new key "city" with value "Amravati" in the dictionary
print(student)

new_dict={"country":"India"}
student.update(new_dict) # it will add a new key "country" with value "India" in the dictionary
print(student)
student.update({"age":21}) # it will update the value of the key "age" to 21 in the dictionary and if the key is not present in the dictionary then it will add the key with the value in the dictionary otherwise it will update the value of the key in the dictionary and not add again duplicate key in the dictionary.
student.update({"name":"devarshi"}) # it will update the value of the key "name" to "devarshi" in the dictionary and if the key is not present in the dictionary then it will add the key with the value in the dictionary otherwise it will update the value of the key in the dictionary and not add again duplicate key in the dictionary.
print(student)