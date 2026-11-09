a="6"
b=7
c=9.8

a=int(a)     #Convert string to integer but it will only possible when the string contains a valid integer and float value but character string will not be converted to integer
print(type(a))   
b=float(b)   #Convert integer to float
print(type(b))
c=str(c)     #Convert float to string
print(type(c))
c=float(c)
print(type(c))#converting string to float is possible but string to integer is not possible if the string contain the float value.it required to convert the string to float first and then to integer.means string 9.8 to int 9.8 is not possible but 9 or 11 is possible to string to integer 
c=int(c)
print(type(c))