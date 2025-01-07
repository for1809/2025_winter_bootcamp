# 3. Print Stars

# Make a function that print stars as below.

# (1) `star_flag(n)` (n is a positive number)

# (2) `star_Z(n) (n>2)`


def star_flag(n):
    # Write your code here
    count1 = 1
    while count1 <= n:
        print('*' * count1)
        count1 += 1
    count1 -= 2
    while count1 > 0:
        print('*' * count1)
        count1 -= 1


def star_Z(n):
    # Write your code here
    print('*' * n)
    for i in range(n - 2):
        space = n - 2 - i
        print(' ' * space, '*', sep = '')
    print('*' * n)
star_Z(5)