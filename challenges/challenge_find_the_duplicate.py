# task 5

# INPUT:
# nums = array of N numbers

# RETURN:
# if the array contains duplicate numbers return the duplicate;
# if function receives empty array return False;
# if function receives an array with strings return False;
# if function receives an array without duplicate numbers return False;
# if function receives an array with just one int return False;
# if function receives an array with negative numbers return False;

# STRATEGY, IMPLEMENTATION:
# - algorithms: -- = --
# - strategy: -- = --
# - implementation: Iterative
# - time complexity: O (n)

# RESTRICTIONS, REQUIREMENTS:
# tip: sort the array - sort() or sorted() are allowed


def find_duplicate(nums):
    """
    this function finds the first duplicate number on an array.
    """
    numbers_arr, number = nums, 0
    if len(numbers_arr) <= 1:
        return False
    numbers_arr.sort()
    for index in range(1, len(numbers_arr)):
        if numbers_arr[index] == numbers_arr[index-1]:
            number = numbers_arr[index]
    if number < 1:
        return False
    return number
