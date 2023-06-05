# task 4

# INPUT:
# two strings: 2 words to be compared

# RETURN:
# returns Tuple with 2 sorted str + boolean.
# true if strings are anagrams
# false if strings are empty or aren't anagrams

# STRATEGY, IMPLEMENTATION:
# - algorithm: Merge Sort
# - strategy: Divide and Conquer
# - implementation: Recursion
# - time complexity: O (n log n)

# RESTRICTIONS, REQUIREMENTS:
# python functions (sort, sorted, collections/Counter) are not allowed
# str comparison (case insentisitive)

# Ref: https://stackabuse.com/merge-sort-in-python/

# file authorship: thiago guarino


def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return
    middle = (left_index + right_index) // 2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)


def merge(array, left_index, right_index, middle):
    l_array = array[left_index:middle + 1]
    r_array = array[middle+1:right_index+1]

    left_copy_index = 0
    right_copy_index = 0

    sorted_index = left_index

    while left_copy_index < len(l_array) and right_copy_index < len(r_array):

        if l_array[left_copy_index] <= r_array[right_copy_index]:
            array[sorted_index] = l_array[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            array[sorted_index] = r_array[right_copy_index]
            right_copy_index = right_copy_index + 1

        sorted_index = sorted_index + 1

    while left_copy_index < len(l_array):
        array[sorted_index] = l_array[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(r_array):
        array[sorted_index] = r_array[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def is_anagram(first_string, second_string):
    """
    this function checks if a string is another string's anagram.
    """
    first_word = list(first_string.lower())
    second_word = list(second_string.lower())

    merge_sort(first_word, 0, len(first_word) - 1)
    merge_sort(second_word, 0, len(second_word) - 1)

    first_word_sorted = ''.join(first_word)
    second_word_sorted = ''.join(second_word)

    if first_string == '' or second_string == '':
        return (first_word_sorted, second_word_sorted, False)

    if first_word != second_word:
        return (first_word_sorted, second_word_sorted, False)

    return (first_word_sorted, second_word_sorted, True)
