list=["mic","speaker","mobile","camera"]

print("earbuds" in list)

print("mobile" in list)

print()
print()

marks=[70,80,95,98]

for i in marks:
    print(i/2)

print()
# but by using if is long method we just use below method 

print([i/2 for i in marks])