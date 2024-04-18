def is_array_monotonic(array):
    increasing = False
    decreasing = False

    if len(array) == 1:
        return True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:

            decreasing = True

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:

            increasing = True

    if increasing and decreasing:
        return False
    return True
