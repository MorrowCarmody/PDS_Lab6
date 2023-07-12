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
