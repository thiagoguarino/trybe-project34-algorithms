# task 3
def is_palindrome_recursive(word, low_index, high_index):
    """
    this function checks if a string is a palindrome or not
    """
    normal_word = word.lower()

    # Take two pointer L & R.
    # L point to the first character of the string and R point to the last character of the String.
    # if L >= R then returns True (means it is a palindrome)
    # if S[L] != S[R] then returns False ( means it is not palindrome).
    # otherwise return recursive functionis_palindrome(L+1, R+1,S) .

    if (normal_word == ''):
        return False

    if low_index >= high_index:
        return True

    if normal_word[low_index] != normal_word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index+1, high_index-1)
