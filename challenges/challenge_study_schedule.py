# task 1

# INPUT:
# permanance_period = array of tuples with login time and logout time (int)
# target_time = int value that corresponds to the time searched

# RETURN:
# return int value that is the amount of students logged at that time
# return None if target value is empty of wrong data type is provided

# STRATEGY, IMPLEMENTATION:
# - algorithm: -- = --
# - strategy: Brute Force
# - implementation: Iterative
# - time complexity: O(n)

# RESTRICTIONS, REQUIREMENTS:
# -- = --

def study_schedule(permanence_period, target_time):
    """
    returns the count of students logged in the platform given a target time.
    """
    try:
        n = len(permanence_period)
        student_counter = 0
        for index in range(0, n):
            login_time, logout_time = permanence_period[index]
            if login_time <= target_time <= logout_time:
                student_counter += 1
    except (TypeError):
        return None

    return student_counter
