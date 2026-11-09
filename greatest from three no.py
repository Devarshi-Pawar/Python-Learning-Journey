a=eval(input("enter first number: "))
b=eval(input("enter second number: "))
c=eval(input("enter third number: "))

if a>=b and a>=c:
    print(a,"is the greatest")
elif b>=a and b>=c:
    print(b,"is the greatest")
else:
    print(c,"is the greatest")