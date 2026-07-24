#Check wheather number is zero or not
n=int(input("Enter an number:"))
if n==0:
    print("Number is zero")
else:
    print("Number is not zero0")    

#Find largest of two numbers
num1=int(input("Enter an first Number:"))
num2=int(input("Enter an second number:"))
if(num1>num2):
    print(num1,"is greater")
else:
    print(num2,"is greater")   

#Check number is positive or negative
num=int(input("Enter an Number:"))
if n>0:
    print(num,"Number is postive")
else:
    print(num,"Number is negative") 

#check vowel or constant
ch=input("Enter character:")
if(ch=="A" or ch=="a" or ch=="E" or ch=="e" or ch=="I" or ch=="i" or ch=="O" or ch=="o" or ch=="U" or ch=="u"):
    print("Character is vowel")
else:
    print("Character is constant")

#Evaluate student performance
m=int(input("Enter Percentage of Student:"))
if(m>=90):
    print("Excellent Performance")
elif(m>=80):
    print("Very Good Performance")
elif(m>=70):
    print("Good Performance")
elif(m>=60):
    print("Average Performance")
else:
    print("Fail")

#Find Greatest Number
n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Third Number:"))
if(n1>n2 and n1>n3):
    print(n1," is greatest number")
elif(n2>n1 and n2>n3):
    print(n2," is greatest number")  
else:
    print(n3," is greatest number")  

#Find Smallest Number
nb1=int(input("Enter First Number:"))
nb2=int(input("Enter Second Number:"))
nb3=int(input("Enter Third Number:"))
if(nb1<nb2 and nb1<nb3):
    print(nb1," is Smallest number")
elif(nb2<nb1 and nb2<nb3):
    print(nb2," is Smallest number")  
else:
    print(nb3," is Smallest number")

#Check number is even or odd
number=int(input("Enter an Number:"))
if(number%2==0):
    print("Number is even")
else:
    print("Number is odd")

#Check year is leap year or not
Year=int(input("Enter an Year:"))
if(Year%4==0 and Year%400==0 and Year%100==0):
    print(Year,"Year is leap year")
else:
    print(Year,"Year is not leap year")

married = input("Married? (yes/no): ")
gender = input("Gender (male/female): ")
age = int(input("Enter age: "))

if married == "yes":
    print("Driver is insured")
elif gender == "male" and age > 30:
    print("Driver is insured")
elif gender == "female" and age > 25:
    print("Driver is insured")
else:
    print("Driver is not insured")   

