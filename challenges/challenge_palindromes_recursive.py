# task 3
def is_palindrome_recursive(word, low_index, high_index):
    """
    this function checks if a string is a palindrome or not
    """
    normal_word = word.lower()

    if (normal_word == ''):
        return False

    if low_index >= high_index:
        return True

    if normal_word[low_index] != normal_word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index+1, high_index-1)
