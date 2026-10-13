Sentence = input()
vowels = "aeiou"
count = 0
for char in Sentence.lower():
    if char in vowels:
        count += 1
print("Number of vowels:", count)