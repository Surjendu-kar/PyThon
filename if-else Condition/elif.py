x = int(input("Enter 1 number :-> "))
y = int(input("Enter 2 number :-> "))
z = int(input("Enter 3 number :-> "))

if x>y and x>z :
    print("max = ",x)
elif y>x and y>z :
    print("max = ",y)
else:
    print("max = ",z)