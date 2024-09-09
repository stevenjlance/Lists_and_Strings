# WRITE YOUR CODE HERE

# PART 1: CREATE, UPDATE, READ, DELETE

# 1. Initialize a variable avengers as an list. Assign the list the following values: "Iron Man", "Thor", "Captain America", "The Hulk", "Spider Man", "Ant Man", "Batman"
avengers = ["Iron Man", "Thor", "Captain America", "The Hulk", "Spider Man", "Ant Man", "Batman"]

# 2. Using index notation, store the third avenger in the avengers list in the thirdAvenger variable. Replace None with your code.

thirdAvenger = avengers[2]

# 3. Using index notation, replace "The Hulk" with "Captain Marvel" in the avengers list.

avengers[3] = "Captain Marvel"

# STOP AND CHECK: Check that your answers are correct by running test_part2 as instructed in the READ_ME. Move on only if you have passed the first set of tests.

# PART 2: Updating Lists and List Methods
fruits = ["pineapple", "apple", "grape", "refined uranium", "banana"]

'''
Using the provided fruits list, complete the following 
  Because we're mutating the list as we go, the number of elements will change as will indexes of items.
  It will help to follow the instructions sequentially.
'''

# 4. That forth element doesn't look right...update it to "strawberry"
fruits[3] = "strawberry"

# 5. The bananas are too bendy! Find 'banana' and delete it!
fruits.pop()


# 6. Add "orange" to the beginning of the list
fruits.insert(0, "orange")

# 7. Add "raspberry" to the end of the list
fruits.append("raspberry")


# 8. Insert "mango" into the fruits list as the 6th item
fruits.insert(5, "mango")

# STOP AND CHECK: Check that your answers are correct by running test_part2 as instructed in the READ_ME. Move on only if you have passed the second set of tests.

# PART 3: Larger Lists and Spicier List Methods

# A list of punny jokes have been imported using the command below
from jokes import punny_jokes 
# You can uncomment the line below to see the full list or you can view it in the jokes.py file.
# print(punny_jokes)

# For the variables already created, replace None with your code.
# 9. The list is quite large, save the number of jokes in the variable number_of_jokes. 
number_of_jokes = len(punny_jokes)


# 10. Get the last joke on the list and save it to the favorite_joke variable
favorite_joke = punny_jokes[len(punny_jokes) - 1]

# 11. Find the index of the following joke and save it to the variable golf_joke: "Why did the golfer bring two pairs of pants? In case he got a hole in one."
golf_joke = punny_jokes.index("Why did the golfer bring two pairs of pants? In case he got a hole in one.")

# 12. STRETCH: Make a copy of the punny_jokes list and save it to the variable reverse_aphabetized. Then, sort the list in REVERSE alphabetical order.
reverse_alphabetized = punny_jokes.copy()
reverse_alphabetized.sort(reverse = True)

# STOP AND CHECK: Check that your answers are correct by running test_part3 as instructed in the READ_ME.

# PART 4: ITERATE

# 13. You have a list of numbers provided below. Iterate through the list and sum up all the values. Store the final result in the variable sum that currently has the value of 0.

numbers = [73, 51, 97, 28, 64, 39, 12, 85, 46, 0, 75, 53, 98, 29, 65, 40, 13, 86, 47, 1, 76, 54, 99, 30, 66, 41, 14, 87, 48, 2, 77, 55, 0, 31, 67, 42, 15, 88, 49, 3, 78, 56, 1, 32, 68, 43, 16, 89, 50, 4, 79, 57, 2, 33, 69, 44, 17, 90, 51, 5, 80, 58, 3, 34, 70, 45, 18, 91, 52, 6, 81, 59, 4, 35, 71, 46, 19, 92, 53, 7, 82, 60, 5, 36, 72, 47, 20, 93, 54, 8, 83, 61, 6, 37, 73, 48, 21, 94, 55, 9]

sum = 0

for num in numbers:
  sum = sum + num
print(sum)
# 14. You have an list called oddNums and an empty list called evenNums. Increase each number by 1 and add it to evenNums (i.e. the new list should have the values, 2, 4, 6, 8, etc.)
oddNums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
evenNums = []
for num in oddNums:
   evenNums.append(num + 1)

# BONUS: The problems below are extra practice to help you extend your knowledge of lists! They are not required, but are very helpful as you grow in your knowledge of how to manipulte values in lists.


# 15. Find the maximium and minimum numbers in the numbers list. Save them in the max_val and min_val variables
max_val = max(numbers)
min_val = min(numbers)
print(max_val)
print(min_val)

# 16. Iterate through the all_even array, increase the value by 1 ONLY if the number is odd, and add it to the end of the all_even array. If the number is even, simply add it to the end of all_even without changing the value. Thus, your final list should be only even numbers.

all_even = []

for num in numbers:
  if(num % 2 == 1):
    all_even.append(num + 1)
  else:
    all_even.append(num)
print(all_even)


# 17. You really like jokes that start with the phrase "Why". Iterate through punny_jokes and if the joke starts with the phrase Why then add it to the end of the why_jokes list. If it doesn't start with the phrase Why, do not add it to the why_jokes list.

why_jokes = []

for joke in punny_jokes:
  if joke[0:3] == "Why":
    why_jokes.append(joke)

print(len(why_jokes))