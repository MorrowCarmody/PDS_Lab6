# Matt Carmody
# COSC 6375
# Lab 6 Part 1

def word_sort(words):
    """Sort a list of words in alphabetical order and remove duplicates."""
    word_set = set()
    
    # add items to set to remove duplicates
    for word in words:
        word_set.add(word.lower())

    # return sorted list
    return list(sorted(word_set))

print(word_sort(['This','is','a','test','sentence','written','by','Matt','to','test','the','funciton']))

"""
INSTRUCTIONS:
Part 1. Duplicate Word Removal
This is a problem in the textbook, Problem 6.6, on page 235.
Write a Python script in a file named Lab6_Part1.py.
Write a function that receives a list of words, then determines and displays in alphabetical order only the
unique words. Treat uppercase and lowercase letters the same. The function should use a set to get the
unique words in the list. Test your function.
"""
