# pass statement 
#example 1
for i in range(1,11):
    pass 

print("\n")

#example 2
i=5

if i==5:
    pass

else:
   pass 

#pass statement generally used for skip some part for after used and skip if we does not want to write anything there 

#Q1) write a program to find sum of first n number using while loop only 

sum=0
n=eval(input("enter the value of n:"))
i=1 

while i<=n:
    sum=sum+i
    i+=1
print("sum:",sum)

print("\n")

#Q2) write a program to find the factorial of first n numbers using for loop only

n=eval(input("enter the value of n:"))
fact=1

for i in range (1,n+1):
    fact=fact*i

print("factorial of",n,"is:",fact)