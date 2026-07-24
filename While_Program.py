#write a program to print natural numbers upto n read the n value from user
num=int(input("Enter Number of Natural numbers:"))
i=1
while i<=num:
    print(i,"is a Natural number")
    i+=1

#write a program to print even and odd numbers accept from user
n=int(input("Enter a number: "))
i=1
print("Even numbers:")
while i<=n:
    if i%2==0:
        print(i)
    i=i+1
i=1
print("Odd numbers:")
while i<=n:
    if i%2!=0:
        print(i)
    i=i+1 

#write a program to print sum of odd numbers upto n
n=int(input("Enter the value of n: "))
i=1
sum=0
while i<=n:
    if i%2!=0:
        sum=sum+i
    i=i+1
print("Sum of odd numbers =", sum)

#write a program to print sum of even numbers upto n
n=int(input("Enter the value of n: "))
i=1
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
    i=i+1
print("Sum of odd numbers =", sum)

#write a program to print sum of all naturals numbers upto n
n=int(input("Enter the value of n: "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print("Sum of natural numbers =", sum)

#write a program to print natural numbers upto n in reverse order
n=int(input("Enter the value of n: "))
while n>=1:
    print(n)
    n=n-1

#write a program to print fibonnacii series upto n
n=int(input("Enter the number of terms: "))
a=0
b=1
i=1
while i<=n:
    print(a)
    c=a+b
    a=b
    b=c
    i=i+1 

#write a program to check entered number is prime or not  
n=int(input("Enter a number: "))
i=2
while i<n:
    if n%i==0:
        print(n,"Not a Prime Number")
        break
    i=i+1
else:
    print(n,"Prime Number")

#write a program to find sum of digits of entered number
n=int(input("Enter a number: "))
sum=0
while n>0:
    digit=n%10
    sum= sum+digit
    n=n//10
print("Sum of digits =", sum)

#write a program to check entered number is palindrome or not
n=int(input("Enter a number: "))
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if temp==rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

#write a program to print a multiplication table
n=int(input("Enter a number: "))
i=1
while i<=10:
    print(n, "x", i, "=", n * i)
    i=i+1

#write a program to print largest and smallest number from n numbers
n=int(input("Enter how many numbers: "))
num=int(input("Enter number: "))
largest=num
smallest=num
i=1
while i<n:
    num=int(input("Enter number: "))
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
    i=i+1
print("Largest number=",largest)
print("Smallest number=",smallest)