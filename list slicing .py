marks=[23,46,75,24,67,98,35,44]

print(len(marks))

print(marks[3])

print(marks[1:6])

print(marks[ :5]) #marks[0:5]
print(marks[3: ]) #marks[3:len(marks)]
print(marks[ : ]) #marks[0:len(marks)]
print(marks[-5:-2]) 

marks[2]=12 # allowed in list beacuse list is mutable
print(marks)