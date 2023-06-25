# Matt Carmody
# COSC 6375
# Lab 6 Part 2

def char_count(sentence):
    """Count the occurrence of each letter in a string."""
    sentence = sentence.lower().replace(' ','')
    sentence_dictionary = dict()

    for letter in sentence:
        sentence_dictionary[letter] = 0

    for letter in sentence:
        sentence_dictionary[letter]+=1

    for letter in sorted(sentence_dictionary):
        print(f'{letter}:    {sentence_dictionary[letter]}')
    return

char_count('This is a test sentence written by Matt')

"""
INSTRUCTIONS:
Part 2. Character Counts
This is a problem in the textbook, Problem 6.7, on page 235.
Write a Python script in a file named Lab6_Part2.py.
Recall that strings are sequences of characters. Use techniques similar to Fig. 6.2 to write a script that inputs
a sentence from the user, then uses a dictionary to summarize the number of occurrences of each letter.
Ignore case, ignore blanks and assume the user does not enter any punctuation. Display a two-column table
of the letters and their counts with the letters in sorted order.
"""
