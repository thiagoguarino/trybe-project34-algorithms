# task 6

# INPUT:
# word = string corresponding to a word
# low_index = int value
# high_index = int value

# RETURN:
# if a word is a palindrome returns True
# if a word is NOT a palindrome returns False
# if the input word is empty return False

# STRATEGY, IMPLEMENTATION:
# - algorithm: -- = --
# - strategy: -- = --
# - implementation: Iterative
# - time complexity: O(n)

# RESTRICTIONS, REQUIREMENTS:
# the input can only by a word not a sentence or numbers

# file authorship: thiago guarino


def is_palindrome_iterative(word):
    """
    this function checks if a string (WORD) is a palindrome or not
    """
    normal_word = word.lower()
    reversed_word = word[::-1].lower()

    if (normal_word == ''):
        return False

    for letter in range(0, len(word)):
        if normal_word[letter] != reversed_word[letter]:
            return False
    return True
