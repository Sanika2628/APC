#Arithmetic Operators
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
print("Addition of a and b is:",a+b)
print("Substraction of a and b is:",a-b)
print("Multiplication of a and b is:",a*b)
print("Division of a and b is:",a/b)
print("Modulus of a and b is:",a%b)
print("Floor Division of a and b is:",a//b)
print("Exponential of a and b is:",a**b)

#Comparision Opearators
n1=int(input("Enter First number:"))
n2=int(input("Enter Second number:"))
print("n1==n2 :",n1==n2)
print("n1!=n2 :",n1!=n2)
print("n1<n2 :",n1<n2)
print("n1>n2 :",n1>n2)
print("n1<=n2 :",n1<=n2)
print("n1>=n2 :",n1>=n2)

#Logical Operators
x=10
y=15
if(x>5 and y>=15):
    print("Both Conditions are True")
if(x<15 or y>15):
    print("Atleast one condition is True")
if not(x<5):
    print("Condition is false so not make it True")   

#Assignment Operators
c=5
print("After= :",c)    
c+=5
print("After+= :",c)
c-=5
print("After-= :",c)
c*=5
print("After*= :",c)
c/=5
print("After/= :",c)
c%=5
print("After%= :",c)
c//=5
print("After//= :",c)
c**=5
print("After**= :",c)

#Bitwise Operators
d=10
e=6
print("d & e =",d&e)
print("d | e =",d|e)
print("d ^ e =",d^e)
print("-d =",-d)
print("d << 2 =",d<<2)
print("d >> 2 =",d>>2)

#Membership Operator
colors=["Red","Purple","Black"]
print("Red"in colors)
print("Pink"in colors)
print("Purple" not in colors)

#Identity Operators
a=[10,20,30]
b=a
c=[10,20,30]
print("a is b:",a is b)
print("a is c:",a is c)
print("a is not c:",a is not c)
