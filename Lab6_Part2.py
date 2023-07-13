# Matt Carmody
# COSC 6375
# Lab 6 Part 2

def char_count(sentence):
    """Count the occurrence of each letter in a string."""
    sentence = sentence.lower().replace(' ','')
    sentence_dict = dict()

    # Add letter to dictionary or iterate count if it exists
    for letter in sentence:
        sentence_dict[letter] = sentence_dict.get(letter, 0)+1

    # Print sorted letters and their counts in two-column table
    for letter in sorted(sentence_dict):
        print(f'{letter}:    {sentence_dict[letter]}')
    return

char_count('This is a test sentence written by Matt')
