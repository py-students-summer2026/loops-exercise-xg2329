def one(numbers):
    """
    Write a program that finds the largest element in a given list using a for loop.
    """
    print("\nmedium.one:")

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

    print('\t', f'largest element = {largest}')


def two(numbers):
    """
    Write a program that calculates the average of a list of numbers using a while loop.
    """
    print("\nmedium.two:")

    total = 0
    index = 0
    while index < len(numbers):
        total += numbers[index]
        index += 1

    average = total / len(numbers)
    print('\t', f'average = {average}')


def three(text):
    """
    Write a program that checks if a given string is a palindrome using a for loop.
    """
    print("\nmedium.three:")

    is_palindrome = True

    # Compare characters from both ends.
    for index in range(len(text) // 2):
        if text[index] != text[len(text) - 1 - index]:
            is_palindrome = False
            break

    if is_palindrome:
        print('\t', f'"{text}" is a palindrome')
    else:
        print('\t', f'"{text}" is not a palindrome')


def four(n, first_term, ratio):
    """
    Write a program that prints the first n terms of the geometric sequence using a while loop.
    """
    print("\nmedium.four:")

    count = 0
    term = first_term

    print('\t', f'first {n} terms:', end=' ')
    while count < n:
        if count < n - 1:
            print(term, end=', ')
        else:
            print(term)
        term *= ratio
        count += 1


def five(numbers):
    """
    Write a program that finds the second largest element in a given list using a for loop.
    """
    print("\nmedium.five:")

    largest = numbers[0]
    second_largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number

    print('\t', f'second largest element = {second_largest}')


def six(number):
    """
    Write a program that calculates the factorial of a given number using a while loop.
    """
    print("\nmedium.six:")

    factorial = 1
    current = number

    while current > 0:
        factorial *= current
        current -= 1

    print('\t', f'{number}! = {factorial}')


def seven(number):
    """
    Write a program that checks if a given number is a perfect square using a for loop.
    """
    print("\nmedium.seven:")

    is_perfect_square = False

    for value in range(number + 1):
        if value * value == number:
            is_perfect_square = True
            break

    if is_perfect_square:
        print('\t', f'{number} is a perfect square')
    else:
        print('\t', f'{number} is not a perfect square')


def eight():
    """
    Write a program that prints the sum of all prime numbers between 1 and 100 using a while loop.
    """
    print("\nmedium.eight:")
    number = 2
    total = 0

    while number <= 100:
        is_prime = True
        divisor = 2

        while divisor < number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            total += number

        number += 1

    print('\t', f'sum of prime numbers from 1 to 100 = {total}')


def nine(sentence):
    """
    Write a program that counts the number of words in a given sentence using a for loop.
    """
    print("\nmedium.nine:")

    for symbol in ',.!?':
        sentence = sentence.replace(symbol, ' ')
    words = sentence.split()
    
    count = 0
    for word in words:
        count += 1
    print('\t', f'number of words = {count}')


def ten(list1, list2):
    """
    Write a program that prints the common elements between two lists using a while loop.
    """
    print("\nmedium.ten:")

    common_elements = []
    index = 0

    while index < len(list1):
        if list1[index] in list2 and list1[index] not in common_elements:
            common_elements.append(list1[index])
        index += 1
    
    print('\t', 'common elements =', common_elements)
