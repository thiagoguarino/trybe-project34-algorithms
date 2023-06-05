# task 3

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
# - implementation: Recursive
# - time complexity: O(n)

# RESTRICTIONS, REQUIREMENTS:
# the input can only by a word not a sentence or numbers

# file authorship: thiago guarino


def is_palindrome_recursive(word, low_index, high_index):
    """
    this function checks if a string (WORD) is a palindrome or not
    """
    normal_word = word.lower()

    if (normal_word == ''):
        return False

    if low_index >= high_index:
        return True

    if normal_word[low_index] != normal_word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index+1, high_index-1)
