student={
    "name":"deva",
    "cgpa":9.5,
    "marks":[23,56,34]
    }

print(student["cgpa"])
print(student["name"])
print(student["marks"])

print("\n")
student["cgpa"]=9.8 # allowed in dictionary beacuse dictionary is mutable
print(student["cgpa"])

student["name"]="devarshi" # allowed in dictionary beacuse dictionary is mutable
print(student["name"])

print("\n")

#Nested dictionary

student={
    "name":"deva",
    "cgpa":9.5 ,
    "score":{
        "maths":23,
        "science":56,
        "english":34
    }
}
 
print(student)
print(student["score"]["maths"])

print(student["score"]["science"])

student["score"]["maths"]=78 # allowed in dictionary beacuse dictionary is mutable
print(student)

print("\n")

# null or empty dictionary
student={}
print(student)
