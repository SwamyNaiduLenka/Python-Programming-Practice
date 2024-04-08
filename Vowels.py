# Count the number of vowels in a given string using a "for" loop
sentence = "India is developing country"
count = 0

for i in range(len(sentence)):
    if sentence[i] == 'a' or sentence[i] == 'e' or sentence[i] == 'i' or sentence[i] == 'o' or sentence[i] == 'u':
        count = count + 1

print(f"The number of vowels in the sentence is: {count}")
