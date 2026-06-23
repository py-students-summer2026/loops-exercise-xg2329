def one(number):
    """
    Write a program that finds the prime factors of a given number using a for loop.
    """
    print("\ndifficult.one:")

    prime_factors = []

    for candidate in range(2, number + 1):
        if number % candidate == 0:
            is_prime = True
            for divisor in range(2, candidate):
                if candidate % divisor == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_factors.append(candidate)

    print('\t', f'prime factors of {number} = {prime_factors}')


def two(n):
    """
    Write a program that calculates the nth term of the Fibonacci sequence using a while loop.
    """
    print("\ndifficult.two:")

    if n == 1:
        print('\t', 'term 1 = 0')
        return
    if n == 2:
        print('\t', 'term 2 = 1')
        return

    first = 0
    second = 1
    count = 3

    while count <= n:
        next_term = first + second
        first = second
        second = next_term
        count += 1

    print('\t', f'term {n} = {second}')


def three(text1, text2):
    """
    Write a program that checks if a given string is an anagram using a for loop.
    """
    print("\ndifficult.three:")

    first_text = text1.replace(' ', '').lower()
    second_text = text2.replace(' ', '').lower()
    
    is_anagram = True

    if len(first_text) != len(second_text):
        is_anagram = False
    else:
        checked_letters = ''
        for letter in first_text:
            if letter not in checked_letters:
                count_first = 0
                count_second = 0

                for character in first_text:
                    if character == letter:
                        count_first += 1
                        
                for character in second_text:
                    if character == letter:
                        count_second += 1

                if count_first != count_second:
                    is_anagram = False
                    break

                checked_letters += letter

    if is_anagram:
        print('\t', f'"{text1}" and "{text2}" are anagrams')
    else:
        print('\t', f'"{text1}" and "{text2}" are not anagrams')


def four(n, first_term, difference):
    """
    Write a program that prints the first n terms of the arithmetic sequence using a while loop.
    """
    print("\ndifficult.four:")

    count = 0
    term = first_term

    print('\t', f'first {n} terms:', end=' ')
    while count < n:
        if count < n - 1:
            print(term, end=', ')
        else:
            print(term)
        term += difference
        count += 1


def five(numbers):
    """
    Write a program that finds the median of a given list of numbers using a for loop.
    """
    print("\ndifficult.five:")

    sorted_numbers = numbers[:]
    # Sort the list in ascending order.
    for i in range(len(sorted_numbers)):
        for j in range(i + 1, len(sorted_numbers)):
            if sorted_numbers[i] > sorted_numbers[j]:
                temp = sorted_numbers[i]
                sorted_numbers[i] = sorted_numbers[j]
                sorted_numbers[j] = temp

    middle = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 1:
        median = sorted_numbers[middle]
    else:
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

    print('\t', f'median = {median}')


def six(number):
    """
    Write a program that checks if a given number is a perfect number using a while loop.
    """
    print("\ndifficult.six:")

    divisor = 1
    total = 0

    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1

    if total == number:
        print('\t', f'{number} is a perfect number')
    else:
        print('\t', f'{number} is not a perfect number')


def seven(number):
    """
    Write a program that prints the sum of all digits in a given number using a for loop.
    """
    print("\ndifficult.seven:")

    total = 0
    for digit in str(number):
        total += int(digit)
    print('\t', f'sum of digits in {number} = {total}')


def eight(sentence):
    """
    Write a program that finds the longest word in a given sentence using a while loop.
    """
    print("\ndifficult.eight:")

    clean_sentence = sentence
    for symbol in ',.!?':
        clean_sentence = clean_sentence.replace(symbol, ' ')

    words = clean_sentence.split()
    longest_word = ''
    index = 0

    while index < len(words):
        if len(words[index]) > len(longest_word):
            longest_word = words[index]
        index += 1
    
    print('\t', f'longest word = "{longest_word}"')


def nine(sentence):
    """
    Write a program that checks if a given string is a pangram using a for loop.
    """
    print("\ndifficult.nine:")

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = sentence.lower()
    is_pangram = True

    for letter in alphabet:
        if letter not in text:
            is_pangram = False
            break

    if is_pangram:
        print('\t', 'The sentence is a pangram')
    else:
        print('\t', 'The sentence is not a pangram')


def ten():
    """
    Write a program that prints the prime numbers between 1 and 1000 using a while loop.
    """
    print("\ndifficult.ten:")

    number = 2
    prime_numbers = []

    while number <= 1000:
        is_prime = True
        divisor = 2

        while divisor < number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            prime_numbers.append(number)
        number += 1
    print('\t', prime_numbers)
