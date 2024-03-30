#find bigest among them in 3 values
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b and a>c:
    print("{} it is big".format(a))
elif b>a and b>c:
    print("{} it is big".format(b))
else:
    print("{} it is big".format(c))