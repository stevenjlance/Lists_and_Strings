import pytest
from assignment1 import fruits, avengers, thirdAvenger, number_of_jokes, favorite_joke, golf_joke, reverse_alphabetized, sum, evenNums, all_even, max_val, min_val, why_jokes
from jokes import punny_jokes

def test_part1():
    expected = ['Iron Man', 'Thor', 'Captain America', 'Captain Marvel', 'Spider Man', 'Ant Man', 'Batman']
    assert avengers == expected
    assert thirdAvenger == expected[2]

def test_part2():
    expected = ['orange', 'pineapple', 'apple', 'grape', 'strawberry', 'mango', 'raspberry']
    assert fruits == expected

def test_part3():
    assert number_of_jokes == 50
    assert favorite_joke == "Why did the computer go to the doctor? Because it had a virus!"
    assert golf_joke == 30
    newList = punny_jokes.copy()
    newList.sort(reverse = True)
    assert reverse_alphabetized == newList

def test_part4():
    assert sum == 4718
    assert evenNums == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]


def test_bonus():
    assert max_val == 99
    assert min_val == 0
    assert all_even == [74, 52, 98, 28, 64, 40, 12, 86, 46, 0, 76, 54, 98, 30, 66, 40, 14, 86, 48, 2, 76, 54, 100, 30, 66, 42, 14, 88, 48, 2, 78, 56, 0, 32, 68, 42, 16, 88, 50, 4, 78, 56, 2, 32, 68, 44, 16, 90, 50, 4, 80, 58, 2, 34, 70, 44, 18, 90, 52, 6, 80, 58, 4, 34, 70, 46, 18, 92, 52, 6, 82, 60, 4, 36, 72, 46, 20, 92, 54, 8, 82, 60, 6, 36, 72, 48, 20, 94, 54, 8, 84, 62, 6, 38, 74, 48, 22, 94, 56, 10]
    assert len(why_jokes) == 15