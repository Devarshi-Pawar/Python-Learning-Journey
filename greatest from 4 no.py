a=eval(input("enter first number: "))
b=eval(input("enter second number: "))
c=eval(input("enter third number: "))
d=eval(input("enter fourth number: "))  

if a>=b and a>=c and a>=d:
    print(a,"is the greatest")
elif b>=c and b>=d:
    print(b,"is the greatest")
elif c>=a and c>=d:
    print(c,"is the greatest")
else:       
    print(d,"is the greatest")