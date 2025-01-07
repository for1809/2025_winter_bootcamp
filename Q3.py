def compare_numbers(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        print('Error: Both parameters should be integers.')
    elif num1 > num2:
        print(f'{num1} is greater than {num2}')
    elif num1 < num2:
        print(f'{num1} is less than {num2}')
    else:
        print(f'{num1} is equal to {num2}')


