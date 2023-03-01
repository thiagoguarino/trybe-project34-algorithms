# task 6
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
