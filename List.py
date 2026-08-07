#Create a list of five fruits and display the lists
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("List of Fruits:")
print(fruits)

#Display first, last and third element
numbers = [10, 20, 30, 40, 50]
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("Third Element:", numbers[2])

#Replace the third color
colors = ["Red", "Blue", "Green", "Yellow", "Black"]
colors[2] = "Purple"
print("Updated List:")
print(colors)

#Add elements at end, beginning and specified position
numbers = [10, 20, 30, 40]
numbers.append(50)
numbers.insert(0, 5)
numbers.insert(3, 25)
print("Updated List:")
print(numbers)

#Remove first, last and specific student
students = ["Amit", "Rahul", "Sneha", "Priya", "Neha"]
students.pop(0)
students.pop()
students.remove("Sneha")
print("Remaining Students:")
print(students)

#Largest and smallest without max() and min()
numbers = [45, 12, 89, 23, 67, 5]
largest = numbers[0]
smallest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print("Largest =", largest)
print("Smallest =", smallest)

#Accept 10 numbers and find sum and average
numbers = []
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)
total = sum(numbers)
average = total / len(numbers)
print("Sum =", total)
print("Average =", average)

#Count even and odd numbers
numbers = []
for i in range(15):
    num = int(input("Enter number: "))
    numbers.append(num)
even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even Numbers =", even)
print("Odd Numbers =", odd)

#Search city in list
cities = ["Pune", "Mumbai", "Delhi", "Kolhapur", "Nagpur"]
city = input("Enter city name: ")
if city in cities:
    print("City Found")
else:
    print("City Not Found")

#Reverse list without reverse()
numbers = [10, 20, 30, 40, 50]
rev = []
for i in range(len(numbers)-1, -1, -1):
    rev.append(numbers[i])
print("Original List:", numbers)
print("Reversed List:", rev) 

#Display different parts using slicing
numbers = [1,2,3,4,5,6,7,8,9,10]
print("First 5 Elements:", numbers[:5])
print("Last 5 Elements:", numbers[-5:])
print("Middle 4 Elements:", numbers[3:7])
print("Alternate Elements:", numbers[::2])
print("Reverse List:", numbers[::-1])

#Display elements at even index positions
numbers = [10,20,30,40,50,60,70]
print("Elements at Even Index:")
for i in range(0, len(numbers), 2):
    print(numbers[i])

#Sort ascending and descending
numbers = []
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)
numbers.sort()
print("Ascending:", numbers)
numbers.sort(reverse=True)
print("Descending:", numbers)

#Display unique elements
numbers = [10,20,10,30,40,20,50,30]
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
print("Unique Elements:")
print(unique)

#Find second largest element
numbers = [25, 40, 80, 65, 90, 75]
largest = second = -999999
for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
print("Second Largest =", second)

#Nested list of students
students = [
    ["Amit", 1, 85],
    ["Sneha", 2, 90],
    ["Rahul", 3, 78]
]
print("Student Details")
for student in students:
    print("Name:", student[0])
    print("Roll No:", student[1])
    print("Marks:", student[2])
    print()

#Matrix Addition
A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
B = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]
C = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print("Result Matrix:")
for row in C:
    print(row)   

#Shopping Cart
cart = ["Milk", "Bread", "Rice"]
cart.append("Sugar")
cart.remove("Bread")
item = input("Enter item to search: ")
if item in cart:
    print("Item Found")
else:
    print("Item Not Found")
print("Shopping Cart:", cart)
print("Total Items:", len(cart)) 

#Student Attendance List
students = ["Amit", "Rahul", "Sneha", "Neha"]
print("Total Students:", len(students))
name = input("Enter student name to search: ")
if name in students:
    print("Present")
else:
    print("Absent")
new_student = input("Enter new student: ")
students.append(new_student)
remove_student = input("Enter absent student to remove: ")
if remove_student in students:
    students.remove(remove_student)
print("Updated Student List:")
print(students)

#Book List Management
books = ["Python", "Java", "C++"]
new_book = input("Enter new book: ")
books.append(new_book)
search_book = input("Enter book to search: ")
if search_book in books:
    print("Book Found")
else:
    print("Book Not Found")
remove_book = input("Enter book to remove: ")
if remove_book in books:
    books.remove(remove_book)
print("Book List:")
print(books)
print("Total Books:", len(books))

#Accept two lists and merge them into a single list
list1 = []
list2 = []
print("Enter 5 elements for List 1")
for i in range(5):
    list1.append(int(input()))
print("Enter 5 elements for List 2")
for i in range(5):
    list2.append(int(input()))
merged = list1 + list2
print("Merged List:")
print(merged)

#Find common elements between two lists
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70, 20]
common = []
for i in list1:
    if i in list2 and i not in common:
        common.append(i)
print("Common Elements:")
print(common)

#Count the frequency of each element in a list
numbers = [10, 20, 10, 30, 20, 10, 40]
checked = []
for i in numbers:
    if i not in checked:
        count = 0
        for j in numbers:
            if i == j:
                count += 1
        print(i, "appears", count, "times")
        checked.append(i)

#Rotate a list left and right by one position
numbers = [10, 20, 30, 40, 50]
left = numbers[1:] + [numbers[0]]
right = [numbers[-1]] + numbers[:-1]
print("Original List:", numbers)
print("Left Rotation:", left)
print("Right Rotation:", right)

#Remove duplicate elements while preserving order
numbers = [10, 20, 10, 30, 40, 20, 50, 30]
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
print("List without Duplicates:")
print(unique)

#Students Marks Analysis
marks = []
print("Enter marks of 20 students")
for i in range(20):
    marks.append(int(input()))
highest = marks[0]
lowest = marks[0]
total = 0
for i in marks:
    total += i
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
average = total / len(marks)
above = 0
below = 0
for i in marks:
    if i > average:
        above += 1
    elif i < average:
        below += 1
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Students Above Average:", above)
print("Students Below Average:", below)

#Employee salary analysis
salary = []
n = int(input("Enter number of employees: "))
for i in range(n):
    salary.append(int(input("Enter Salary: ")))
highest = salary[0]
lowest = salary[0]
total = 0
for i in salary:
    total += i
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
average = total / n
above50000 = 0
below30000 = 0
for i in salary:
    if i > 50000:
        above50000 += 1
    if i < 30000:
        below30000 += 1
print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Employees Above ₹50000:", above50000)
print("Employees Below ₹30000:", below30000)

#Batsman Score Analysis
scores = []
print("Enter scores of 10 matches")
for i in range(10):
    scores.append(int(input()))
highest = scores[0]
lowest = scores[0]
total = 0
century = 0
half = 0
for i in scores:
    total += i
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
    if i >= 100:
        century += 1
    elif i >= 50:
        half += 1
average = total / len(scores)
print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Total Runs:", total)
print("Average Runs:", average)
print("Centuries:", century)
print("Half-Centuries:", half)

#Temperature Analysis
temperature = []
print("Enter temperature of 30 days")
for i in range(30):
    temperature.append(float(input()))
highest = temperature[0]
lowest = temperature[0]
total = 0
for i in temperature:
    total += i
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
average = total / len(temperature)
above = 0
below = 0
for i in temperature:
    if i > average:
        above += 1
    elif i < average:
        below += 1
print("Hottest Day Temperature:", highest)
print("Coldest Day Temperature:", lowest)
print("Average Temperature:", average)
print("Days Above Average:", above)
print("Days Below Average:", below)

#Patient Management System
names = ["Amit", "Rahul", "Sneha"]
ages = [25, 30, 22]
name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
names.append(name)
ages.append(age)
delete = input("Enter Patient Name to Delete: ")
if delete in names:
    index = names.index(delete)
    names.pop(index)
    ages.pop(index)
    print("Patient Deleted")
else:
    print("Patient Not Found")
search = input("Enter Patient Name to Search: ")
if search in names:
    index = names.index(search)
    print("Patient Found")
    print("Name:", names[index])
    print("Age:", ages[index])
else:
    print("Patient Not Found")
print("\nPatient Details")
for i in range(len(names)):
    print("Name:", names[i], "Age:", ages[i])
print("Total Patients:", len(names))
