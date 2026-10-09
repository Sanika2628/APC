text = input("Enter a paragraph: ")
words = text.lower().split()
print("Total words:", len(words))
frequency = {}
for word in words:
    word = word.strip(".,!?;:")
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("Word Frequency:")
for word in frequency:
    print(word, ":", frequency[word])
print("Top 3 Most Frequent Words:")
sorted_words = sorted(frequency, key=frequency.get, reverse=True)
for word in sorted_words[:3]:
    print(word, ":", frequency[word])
vowels = "aeiou"
count = 0
for ch in text.lower():
    if ch in vowels:
        count += 1
print("Total vowels:", count)

