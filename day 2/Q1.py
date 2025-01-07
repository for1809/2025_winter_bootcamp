# # 1. Practice with the `math` Module

# ### Problem Statement

# Use the `math` module to solve the following problems.

# ### Requirements

# 1. Write a function `calculate_area_of_circle(radius)` that takes a float `radius` and returns the area of a circle with that radius. Use `math.pi` to get the value of π.
#   - The area of a circle is given by: $$ \text{Area} = \pi \cdot \text{radius}^2 $$

# 2. Write a function `calculate_hypotenuse(a, b)` that takes two floats `a` and `b` representing the lengths of the two shorter sides of a right triangle and returns the length of the hypotenuse. Use `math.sqrt` to calculate the square root.
#   - The hypotenuse of a right triangle is given by: $$ c = \sqrt{a^2 + b^2} $$


# 3. Write a function `convert_degrees_to_radians(degrees)` that takes a float `degrees` and returns the equivalent angle in radians. Use `math.radians` to convert degrees to radians.
#   - To convert degrees to radians, use the formula: $$ \text{radians} = \frac{\pi \cdot \text{degrees}}{180} $$



# 4. Write a function `calculate_factorial(n)` that takes an integer `n` and returns the factorial of `n`. Use `math.factorial` to calculate the factorial.
#   - The factorial of a number \( n \) is given by: $$ n! = n \cdot (n-1) \cdot (n-2) \cdots 3 \cdot 2 \cdot 1 $$


# 5. Write a function `calculate_logarithm(value, base)` that takes two floats `value` and `base` and returns the logarithm of `value` to the given `base`. Use `math.log` to calculate the logarithm.
#   - The logarithm of a value with a given base is: $$ \log_{\text{base}}(\text{value}) $$


import math



def calculate_area_of_circle(radius):
    # Write your code here
    return math.pi * raidus ** 2

def calculate_hypotenuse(a, b):
    # Write your code here
    return math.sqrt(a ** 2 + b ** 2)

def convert_degrees_to_radians(degrees):
    # Write your code here
    return math.radians(degrees)

def calculate_factorial(n):
    # Write your code here
    return math.factorial(n)

def calculate_logarithm(value, base):
    # Write your code here
    return math.log(value, base)
