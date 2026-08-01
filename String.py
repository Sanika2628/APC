#String Length
#Write a program to input a string and display its length without using the len() function
string=input("Enter a string: ")
count=0
for ch in string:
    count=count+1
print("Length of the string is:",count)

#Character Count
#Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 
string=input("Enter a string: ")
vowels=consonants=digits=spaces=special=0
for ch in string:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1
print("Vowels:",vowels)
print("Consonants:",consonants)
print("Digits:",digits)
print("Spaces:",spaces)
print("Special Characters:",special)

#Reverse String
#Reverse the given string without using built-in reverse functions
string=input("Enter a string: ")
reverse=""
for ch in string:
    reverse=ch+reverse
print("Reversed string is:",reverse)

#Palindrome Check
#Check whether the entered string is a palindrome. 
string=input("Enter a string: ")
reverse=""
for ch in string:
    reverse=ch+reverse
if string==reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#Uppercase and Lowercase Count 
#Count the number of uppercase and lowercase letters in a string    
string=input("Enter a string: ")
uppercase=0
lowercase=0
for ch in string:
    if ch.isupper():
        uppercase+=1
    elif ch.islower():
        lowercase+=1
print("Uppercase letters:",uppercase)
print("Lowercase letters:",lowercase)

#Replace Characters
#Replace all occurrences of a given character with another character
string=input("Enter a string: ")
old=input("Enter the character to replace: ")
new=input("Enter the new character: ")
result=""
for ch in string:
    if ch==old:
        result=result+new
    else:
        result=result+ch
print("Updated string:",result)

#Remove Spaces
#Remove all spaces from the input string
string = input("Enter a string: ")
result = ""
for ch in string:
    if ch != " ":
        result = result + ch
print("String after removing spaces:", result)

#Frequency of Character
#Find the number of times a specified character appears in a string. 
string = input("Enter a string: ")
char = input("Enter the character to search: ")
count = 0
for ch in string:
    if ch == char:
        count += 1
print("Number of occurrences of", char, "is:", count)

#First and Last Character
#Print the first and last character of a string. 
string = input("Enter a string: ")
if string:
    print("First character:", string[0])
    print("Last character:", string[-1])
else:
    print("The string is empty.")

#Ascii Values
#Display each character of a string along with its ASCII value.
string = input("Enter a string: ")
for ch in string:
    print(ch, ":", ord(ch))   

#Word Count
#Count the total number of words in a sentence. 
sentence = input("Enter a sentence: ")
words = sentence.split()
count = 0
for word in words:
    count += 1
print("Total number of words:", count) 

#Longest Word
#Find the longest word in a given sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
longest = ""
for word in words:
    if len(word) > len(longest):
       longest = word
print("Longest word:", longest)
print("Length:", len(longest))

#Shortest Word
#Find the shortest word in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
shortest = words[0]
for word in words:
    if len(word) < len(shortest):
        shortest = word
print("Shortest word:", shortest)
print("Length:", len(shortest))

#Title Case
#Convert the first letter of every word to uppercase
sentence = input("Enter a sentence: ")
words = sentence.split()
result = ""
for word in words:
    result = result + word.capitalize() + " "
print("Updated sentence:", result)

#Duplicate Characters
#Print all duplicate characters in a string
string = input("Enter a string: ")
printed = ""
for i in range(len(string)):
    count = 0
    for j in range(len(string)):
        if string[i] == string[j]:
            count += 1
    if count > 1 and string[i] not in printed:
        print(string[i])
        printed += string[i]

#Character Frequency
#Display the frequency of every character in a string
string = input("Enter a string: ")
checked = ""
for ch in string:
    if ch not in checked:
        count = 0
        for c in string:
            if ch == c:
                count += 1
        print(ch, ":", count)
        checked += ch

#Anagram Check
#Check whether two strings are anagrams.   
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
s1 = sorted(str1.lower())
s2 = sorted(str2.lower())
if s1 == s2:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")  

#Remove Duplicate Characters
#Remove duplicate characters while maintaining the original order
string = input("Enter a string: ")
result = ""
for ch in string:
    if ch not in result:
        result += ch
print("String after removing duplicates:", result)     

#Substring Search
#Check whether a given substring exists in the main string
main_string = input("Enter the main string: ")
substring = input("Enter the substring: ")
if substring in main_string:
    print("Substring found.")
else:
    print("Substring not found.")

#Count Occurences of Words
#Count how many times a specific word appears in a sentence.   
sentence = input("Enter a sentence: ")
word = input("Enter the word to search: ")
words = sentence.split()
count = 0
for w in words:
    if w == word:
        count += 1
print("The word", word, "appears", count, "time(s).")  

#Password Validator
password = input("Enter a password: ")
upper = lower = digit = special = 0
for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1
if len(password) >= 8 and upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
    print("Password is valid.")
else:
    print("Password is invalid.")

#Run-Length Encoding 
# Program to compress a string using Run-Length Encoding
string = input("Enter a string: ")
result = ""
count = 1
for i in range(len(string)):
    if i < len(string) - 1 and string[i] == string[i + 1]:
        count += 1
    else:
        result = result + string[i] + str(count)
        count = 1
print("Compressed string:", result)  

#String Compression
#Compress repeated characters and return the original string if compression does not reduce the length
string = input("Enter a string: ")
compressed = ""
count = 1
for i in range(len(string)):
    if i < len(string) - 1 and string[i] == string[i + 1]:
        count += 1
    else:
        compressed = compressed + string[i] + str(count)
        count = 1
if len(compressed) < len(string):
    print("Compressed string:", compressed)
else:
    print("Original string:", string) 

#Most Frequent Character
#Find the character with the highest frequency     
string = input("Enter a string: ")
max_char = ""
max_count = 0
for ch in string:
    count = 0
    for c in string:
        if ch == c:
            count += 1
    if count > max_count:
        max_count = count
        max_char = ch
print("Character with highest frequency:", max_char)
print("Frequency:", max_count)

#Second Most Frequent Character
#Find the second most frequently occurring character. 
string = input("Enter a string: ")
freq = {}
for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
first_char = ""
second_char = ""
first_count = 0
second_count = 0
for ch in freq:
    if freq[ch] > first_count:
        second_count = first_count
        second_char = first_char
        first_count = freq[ch]
        first_char = ch
    elif freq[ch] > second_count and freq[ch] != first_count:
        second_count = freq[ch]
        second_char = ch
if second_char != "":
    print("Second most frequent character:", second_char)
    print("Frequency:", second_count)
else:
    print("No second most frequent character found.")

#Encrypt and decrypt a message using the Caesar Cipher algorithm. 
text = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
encrypted = ""
decrypted = ""
for ch in text:
    if ch.isalpha():
        if ch.isupper():
            encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        encrypted += ch
print("Encrypted message:", encrypted)
for ch in encrypted:
    if ch.isalpha():
        if ch.isupper():
            decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
        else:
            decrypted += chr((ord(ch) - 97 - shift) % 26 + 97)
    else:
        decrypted += ch
print("Decrypted message:", decrypted) 

#Email Validator
#Validate whether a given email address follows a valid format. 
email = input("Enter an email address: ")
if ("@" in email and
    "." in email and
    email.index("@") > 0 and
    email.rindex(".") > email.index("@") + 1 and
    email.rindex(".") < len(email) - 1):
    print("Valid email address.")
else:
    print("Invalid email address.")

#Word Frequency Dictionary
#Count the frequency of every word in a paragraph.  
paragraph = input("Enter a paragraph: ")
words = paragraph.lower().split()
frequency = {}
for word in words:
    word = word.strip(".,!?;:'\"()[]{}")
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("\nWord Frequencies:")
for word in frequency:
    print(word, ":", frequency[word])  

#Sentence Reversal 
#Reverse the order of words in a sentence without changing the words themselves. 
sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_sentence = ""
for i in range(len(words) - 1, -1, -1):
    reversed_sentence += words[i] + " "
print("Reversed sentence:", reversed_sentence.strip())

#String Rotation
# Program to check whether one string is a rotation of another
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if len(str1) == len(str2) and str2 in (str1 + str1):
    print("Yes, the second string is a rotation of the first string.")
else:
    print("No, the second string is not a rotation of the first string.") 