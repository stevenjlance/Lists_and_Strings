# To run your code use the command python3 assignment2.py
# To grade your code use the directions in the README.md file in the "Grading Your Code Section"

# A fairy tale has been stored in a string in the variable `fairy_tale` below. We want to use string methods to manipulate this string and to gain information about the string.

fairy_tale = "Once upon a time, in a kingdom far, far away, there lived a beautiful princess named Anya. She was kind and gentle, but she was also very lonely. Her parents had died when she was young, and she had no siblings.  One day, while walking in the garden, Anya saw a small, green frog sitting on a lily pad. She felt sorry for the frog and picked it up. As soon as she touched it, the frog turned into a handsome prince! The prince thanked Anya for freeing him from his curse and told her that he was the prince of a neighboring kingdom. He had been turned into a frog by a wicked witch as punishment for breaking his promise to her. Anya and the prince fell in love and were married. They lived happily ever after, ruling their kingdoms together and bringing peace and prosperity to their people."

## PART 1: String Information

# 1. How many characters are in fairy_tale? Store the length of this string in the variable fairy_tale_length
fairy_tale_length = len(fairy_tale)

# 2. You are in a very large room and need to yell about the fairy tale. Convert fairy_tale to all uppercase letters and store the result in the variable `shout_tale`.
shout_tale = fairy_tale.upper()

# 3. Oh no that was far too loud. Convert fairy tale to all lowercase letter and store the result in variable `whisper_tale`.
whisper_tale = fairy_tale.lower()


# 4. Extract the first charcter of the string and store it in the variable first_char.
first_char = fairy_tale[0]

# 5. Extract the 92nd charcter of the string and store it in the variable middle_char.
middle_char = fairy_tale[91]

# 6. Extract the last charcter of the string and store it in the variable last_char.
last_char = fairy_tale[len(fairy_tale) - 1]

## PART 2: String Methods

# 7. Split the string every time there is a space. Store the split string in the variable split_string.
split_string = fairy_tale.split()

# 8. The princess is actaully a queen! Search the fairy_tale and replace all instances of "princess" with "queen". Save the new string in the variable queen_tale.
queen_tale = fairy_tale.replace("princess", "queen")


## 9. I want to know when prince is first mentioned in the story. Find the index where the string "prince" is first mentioned and store it in the variable prince_index.
prince_index =  fairy_tale.index("prince")


## 10. Many fairy tale start with the phase "Once upon a time". Use a string method to check if this string starts with this phrase and store in answer in the variable is_traditional. HINT: You should use a string method that returns a boolean.

is_traditional = fairy_tale.startswith("Once upon a time")


## 11. STRETCH: Reverse the entire string and store it in the variable reversed_story. This will require a bit of research! You can check this using the bonus1 test.
reversed_story = fairy_tale[::-1]

## PART 3: String Iteration

## 12. Iterate throught he string. Count the number of sentences by counting the number of instances of end-of-sentence punctuation (. ? and !). Store the result in the variable sentence_count.
sentence_count = 0

for character in fairy_tale:
    if character == "." or character == "?" or character == "!":
        sentence_count = sentence_count + 1

print(sentence_count)

# 13. Count up all the instances of vowels (a, e, i, o, or u) in the story. Store the result in vowel_count.
vowel_count = 0

for character in fairy_tale:
    if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
        vowel_count = vowel_count + 1

print(vowel_count)

# STRETCH: How many consonants are in the string fairy_tale? Store the result in consonant_count. This will require a bit of research! You can check this using the bonus2 test.
consonant_count = 0
vowels = 'aeiou'
consonant_count = sum(char not in vowels for char in fairy_tale.lower())
print(consonant_count)