#Create and Display Array
from array import *
a=array('i', [10, 20, 30, 40, 50])
print("Array:", a)

#Access Array Elements
from array import *
a = array('i', [10, 20, 30, 40, 50])
print("First element:", a[0])
print("Third element:", a[2])

#Add Element Using append()
from array import *
a = array('i', [10, 20, 30])
a.append(40)
print("Array:", a)

#Insert Element Using insert()
from array import *
a = array('i', [10, 20, 30])
a.insert(1, 15)
print("Array:", a)

#Remove Element Using remove()
from array import *
a = array('i', [10, 20, 30, 40])
a.remove(20)
print("Array:", a)

#Find Index Using index()
from array import *
a = array('i', [10, 20, 30, 40])
print("Index of 30:", a.index(30))

#Reverse an Array
from array import *
a = array('i', [10, 20, 30, 40])
a.reverse()
print("Reversed array:", a)

#Find Length of Array
from array import *
a = array('i', [10, 20, 30, 40, 50])
print("Length of array:", len(a))

#Extend Array
from array import *
a = array('i', [10, 20, 30])
b = array('i', [40, 50, 60])
a.extend(b)
print("Array:", a)

#Convert Array to List
from array import *
a = array('i', [10, 20, 30, 40])
b = a.tolist()
print("Array:", a)
print("List:", b)

#Find Sum of Array Elements
from array import *
a = array('i', [10, 20, 30, 40, 50])
sum = 0
for i in a:
    sum = sum + i
print("Sum =", sum)