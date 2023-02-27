
# task 1
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
