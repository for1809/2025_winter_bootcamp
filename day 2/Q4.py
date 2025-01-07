# 4. Nested List

# Make a function `P4` that receives a nested list as an input and returns a list that satisfies the conditions below.

# **Conditions**
# - The input list is looks like [[word, length]]
# - Words consist only of lower case letters
# - Collect words from the input list and return as a list
# - The list must be alphabetically ordered


def P4(lst):
    # Write your code here
    result = []
    for nlist in lst:
        result.append(nlist[0])
    result.sort()
    return result
test1 = P4([['apple', 5], ['banana', 3]])
print(test1)