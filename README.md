# Lists_and_Strings

Lists are one of the most integral parts of any programming language. They ensure that we can efficiently store similar data (e.g. a list of names) rather than creating endless amount of variables that will be difficult to remmeber and even harder to query for information. Strings, like lists, also have index values, methods, and can be iterated upon. Thus, many of the actions we perform on a list can also be done on string

**TASK**: This assignment consists of two distinct parts that you will complete in the files `assignment #1.py` and `assignment2.py`.

- **[Assignment #1: Python Lists and List Methods](#assignment-1-python-lists)**: Using your knowledge of lists, list methods, and iteration, complete all of the problems that are written out in the `assignment1.py` file. At the end of each part, grade your code using the directions outlined in the [Grading Your Code](#grading-your-code) section of this page.
- **[Assignment #2: String Methods and Iteration](#assignment-2-string-indexes-and-methods)**: Using your knowledge of strings, string methods, and iteration, complete all of the problems that are written out in the `assignment2.py` file. At the end of each part, grade your code using the directions outlined in the [Grading Your Code](#grading-your-code) section of this page.
- **BONUS PROBLEMS**: Each assignment has bonus problems that are designed to help you extend your knowledge of lists and strings **They are not required**, but are very helpful as you grow in your knowledge of how to manipulte values in lists and strings.

> 💡 Programmers do not memorize many, if any, of the methods you will be using in these assignments. Therfore, be sure to consult the documentation that we have used during the lesson when you are stuck.
>
> - **W3Schools**: [Python Lists](https://www.w3schools.com/python/python_lists.asp)
> - **W3Schools**: [Python List Methods](https://www.w3schools.com/python/python_ref_list.asp)
> - **W3Schools**: [Python String Methods](https://www.w3schools.com/python/python_strings_methods.asp)

## Cloning This Repository

To start the assignment, open up your terminal on your machine and type `git clone https://github.com/stevenjlance/Lists_and_Strings.git`. You can get the URL in this command by pressing the green Code button and then coppying the URL that appears.

![git clone URL](./images/gitClone.png)

## Running Your Code

1. To run your code use the command

```bash
python3 NAME_OF_FILE
```

For example, for the first first assignment you will use the command

```bash
python3 assignment1.py
```

Anything you are outputting to the console with a `print()` statement will appear in your terminal when you run this command.

## Grading Your Code

Your code is setup so that it can grade itself using Python tests. To run the tests do the following:

1. After you have cloned the repository down, click the flask icon in the left tool bar.

![Step 1](./images/Step1.jpg)

2. Next, click "Configure Python Tests".

![Step 2](./images/Step2.jpg)

3. You'll havae two options to select. Select Pytest.

![Step 3](./images/Step3.jpg)

4. Select the folder that contains the tests. In this case you should select **tests**.

![Step 4](./images/Step4.jpg)

5. Finally, you'll see a play icon that you can press to run each of the test. All of the tests in `test_assignment1.py` will grade your code for each part in assignment #1 and all code in `test_assignment2.py` will grade your code for each part in assignment #2.

![Step 5](./images/Step5.png)

6. Click the play button next to `test_part1` and you'll see that it turns red. That's okay! You haven't done any code yet. Start Assignment #1 and press the play button after part 1 to check your work.

## Assignment #1: Python Lists

> All of this work should be done in the [assignment1.py](assignment1.py) file.

### PART 1: CREATE, UPDATE, READ, DELETE

> **NOTE**: In order for the tests to work, some variables have been created with the value of `None`. You should delete `None` and update it with your code.

1. Initialize a variable avengers as an list. Assign the list the following values: `"Iron Man", "Thor", "Captain America", "The Hulk", "Spider Man", "Ant Man", "Batman"`
2. Using index notation, store the third avenger in the avengers list in the `thirdAvenger` variable. Replace `None` with your code.
3. Using index notation, replace `"The Hulk"` with `"Captain Marvel"` in the avengers list.

🛑 **STOP AND CHECK**: Check that your answers are correct by running test_part1 as instructed in the [Grading Your Code](#grading-your-code) section above. Move on **only** if you have passed the first set of tests.

### PART 2: Updating Lists and List Methods

Using the provided `fruits` list, complete the following

4. That forth element doesn't look right...update it to `"strawberry"`.
5. The bananas are too bendy! Find `"banana"` and delete it!
6. Add `"orange"` to the beginning of the list
7. Add `"raspberry"` to the end of the list
8. Insert `"mango"` into the fruits list as the 6th item

🛑 **STOP AND CHECK**: Check that your answers are correct by running test_part2 as instructed in the [Grading Your Code](#grading-your-code) section above. Move on **only** if you have passed the first set of tests.

### PART 3: Larger Lists and Spicier List Methods

A list of punny jokes have been imported into the file and saved the variable `punny_jokes`.

9. The list is quite large, save the number of jokes in the variable number_of_jokes.
10. Get the last joke on the list and save it to the favorite_joke variable
11. Find the index of the following joke and save it to the variable golf_joke: "Why did the golfer bring two pairs of pants? In case he got a hole in one."
12. STRETCH: Make a copy of the punny_jokes list and save it to the variable reverse_aphabetized. Then, sort the list in REVERSE alphabetical order.

🛑 **STOP AND CHECK**: Check that your answers are correct by running test_part3 as instructed in the [Grading Your Code](#grading-your-code) section above.

### PART 4: ITERATE

13. You have a list of numbers provided. Iterate through the list and sum up all the values. Store the final result in the variable `sum` that currently has the value of 0.
14. You have an list called `oddNums` and an empty list called `evenNums`. Increase each number by 1 and add it to evenNums (i.e. the new list should have the values, 2, 4, 6, 8, etc.)

🛑 **STOP AND CHECK**: Check that your answers are correct by running test_part3 as instructed in the [Grading Your Code](#grading-your-code) section above.

### BONUS

The problems below are extra practice to help you extend your knowledge of lists! They are not required, but are very helpful as you grow in your knowledge of how to manipulte values in lists.

15. Find the maximium and minimum numbers in the numbers list. Save them in the max_val and min_val variables
16. Iterate through the all_even array, increase the value by 1 ONLY if the number is odd, and add it to the end of the all_even array. If the number is even, simply add it to the end of all_even without changing the value. Thus, your final list should be only even numbers.
17. You really like jokes that start with the phrase "Why". Iterate through punny_jokes and if the joke starts with the phrase Why then add it to the end of the why_jokes list. If it doesn't start with the phrase Why, do not add it to the why_jokes list.

## Assignment #2: String Indexes and Methods

> All of this work should be done in the [assignment2.py](assignment2.py) file.

**TASK**: A fairy tale has been stored in a string in the variable `fairy_tale`. We want to use string methods to manipulate this string and to gain information about the string.

### PART 1: String Information

> **NOTE**: In order for the tests to work, some variables have been created with the value of `None`. You should delete `None` and update it with your code.

1. How many characters are in fairy_tale? Store the length of this string in the variable `fairy_tale_length`.
2. You are in a very large room and need to yell about the fairy tale. Convert fairy_tale to all uppercase letters and store the result in the variable `shout_tale`.
3. Oh no that was far too loud. Convert fairy tale to all lowercase letter and store the result in variable `whisper_tale`.
4. Extract the first charcter of the string and store it in the variable `first_char`.
5. Extract the 92nd charcter of the string and store it in the variable `middle_char`.
6. Extract the last charcter of the string and store it in the variable `last_char`.

🛑 **STOP AND CHECK**: Check that your answers are correct by running test_part1 as instructed in the [Grading Your Code](#grading-your-code) section above.

## PART 2: String Methods

7. Split the string every time there is a space. Store the split string in the variable `split_string`.
8. The princess is actaully a queen! Search the `fairy_tale` and replace all instances of `"princess"` with `"queen"`. Save the new string in the variable `queen_tale`.
9. I want to know when prince is first mentioned in the story. Find the index where the string `"prince"` is first mentioned and store it in the variable `prince_index`.
10. Many fairy tales start with the phase `"Once upon a time"`. Use a string method to check if this string starts with this phrase and store in answer in the variable is_traditional. **HINT**: You should use a string method that returns a boolean.

🛑 **STOP AND CHECK**: Check that your answers are correct by running `test_part2` as instructed in the [Grading Your Code](#grading-your-code) section above.

11. **BONUS**: Reverse the entire string and store it in the variable `reversed_story`. This will require a bit of research! You can check this using the `test_bonus1` test.

### PART 3: String Iteration

12. Iterate throught he string. Count the number of sentences by counting the number of instances of end-of-sentence punctuation (`.` `?` and `!`). Store the result in the variable `sentence_count`.
13. Count up all the instances of vowels (`a`, `e`, `i`, `o`, or `u`) in the story. Store the result in `vowel_count`.

🛑 **STOP AND CHECK**: Check that your answers are correct by running `test_part3` as instructed in the [Grading Your Code](#grading-your-code) section above.

14. **BONUS**: How many consonants are in the string `fairy_tale`? Store the result in `consonant_count`. This will require a bit of research! You can check this using the `test_bonus2` test.

consonant_count = 0
vowels = 'aeiou'
consonant_count = sum(char not in vowels for char in fairy_tale.lower())
print(consonant_count)
