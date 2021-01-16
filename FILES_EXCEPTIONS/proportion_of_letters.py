# Exercise 162: A Book with No 'E'... (Proportion of words with letter)

from string import ascii_lowercase, punctuation

letter_freq = {letter: 0 for letter in list(ascii_lowercase)}

with open("words.txt", mode="r") as file:

    word = file.readline().strip().lower()
    count = 0
    while word != "":

        used = ""
        for char in word:
            if char not in used and char not in list(punctuation):
                letter_freq[char] += 1
                used += char

        count += 1
        word = file.readline().strip().lower()

# print(letter_freq)
# print(count)

for _ in letter_freq:
    letter_freq[_] = round(letter_freq[_]/count, 3)

# print(letter_freq)

minimum_freq = 2
minimum_letter = ""
for letter in letter_freq:
    if letter_freq[letter] < minimum_freq:
        minimum_freq = letter_freq[letter]
        minimum_letter = letter

print("Least letter used:", minimum_letter)
print("Proportion: ", minimum_freq)
