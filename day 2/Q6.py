# 6. Sum Values Until Threshold is Reached

# Write a function to sum values in a list until the sum reaches or exceeds a given threshold `K`.

# ### Requirements
# * Write a function `sum_until_threshold(lst, K)` that takes a list `lst` and a float `K`.
#     - The list `lst` contains integers, floats, and strings representing numbers.
#     - The function should convert all values to floats, if possible.
#     - If a value cannot be converted to a float, it should be ignored.
#     - If the sum of all valid values in the list is still less than `K`, the function should return `-1` and `None`.
#     - The function should return the sum of the values and the index if the threshold is reached or exceeded.
# * Ensure that the function produces the expected output for the given test cases.

# ### Constraints
# * The threshold `K` will be a positive float.
# * The function should not use any external libraries except for the built-in functions.


def allfloat(x):
    try:
        x = float(x)
    except ValueError:
        pass
    return x

def sum_until_threshold(lst, K):
    # Write your code here
    flst = list(map(allfloat, lst))
    index = 0
    result = 0
    while index < len(flst):
        if isinstance(flst[index], float):
            result += flst[index]
        if result > K:
            return f'{result}, {index}'

        index += 1
    return '-1, None'
print(sum_until_threshold([1, 9, -12, 7, 5], 15))

