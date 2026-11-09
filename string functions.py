name="devarshi"

print(len(name))

print("\n")

print(name.endswith("rshi")) #returns true if the string ends with the given substring
print(name.endswith("deva"))

print("\n")

print(name.startswith("deva")) #returns true if the string starts with the given substring
print(name.startswith("varshi"))    

print("\n") 

print(name.capitalize()) #capitalizes the first letter of the string but only for the first word and only for the one time change not change permanent

print("\n")

print(name.removesuffix("rshi"))

print("\n")

print(name.replace("devarshi","pawar"))

print("\n")

print(name.find("e")) #returns the index of the first occurrence of the given substring
print(name.find("s")) #returns -1 if the given substring is not found in the string

print("\n")

print(name.count("a")) #returns the number of occurrences of the given substring in the string
print(name.count("z")) #returns 0 if the given substring is not found in the string