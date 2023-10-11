import math


def gcd(x):  # 1
    y = []
    for i in range(0, x):
        print("Insert a number")
        y.append(int(input()))

    if len(y) < 2:
        print("Invalid input")
    else:
        result = y[0]
        for n in y[1:]:
            result = math.gcd(result, n)
        print(f"gcd {y}, {result}")


def count_vowels(x=''):  # 2
    vowels = "aAeEiIoOuU"
    result = 0
    for s in vowels:
        result += x.count(s)
    print(f"The number of vowels in {x} = {result}")
    return result


def count_app(x='', y=''):  # 3
    print(f"{x} appears in {y}, {y.count(x)} times")
    return y.count(x)


def convert(x=''):  # 4
    result = ''
    for c in x:
        if c.islower():
            result += c
        else:
            result += '_'
            result += c.lower()
    print(f"Initial string = {x}, converted string = {result}")


def print_spiral(x):  # 5
    result = ''
    top = 0
    bottom = len(x) - 1
    left = 0
    right = len(x[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result += x[top][i]
        top += 1

        for i in range(top, bottom + 1):
            result += x[i][right]
        right -= 1

        if top <= bottom and left <= right:
            for i in range(right, left - 1, -1):
                result += x[bottom][i]
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                result += x[i][left]
            left += 1
    print(f"#5: {result}")
    return result


def is_palindrome(x):  # 6
    if x < 0:
        return False

    if x <= 9:
        return True

    if x % 10 == 0:
        return False

    inv = 0
    y = x
    while x != 0:
        inv = inv * 10 + x % 10
        x = x // 10
    print(f"{y} is palindrome: {inv == y}")
    return y == inv


def find_number(x=''):  # 7
    number = ''
    found = False
    for c in x:
        if found and not c.isdigit():
            print(f"{x} contains as first number: {int(number)}")
            return int(number)

        if c.isdigit():
            found = True
            number += c
    print(f"{x} contains as first number: {int(number)}")
    return int(number)


def count_bits(x):  # 8
    counter = 0
    y = x
    while x != 0:
        if x % 2 == 1:
            counter += 1
        x = x // 2
    print(f"{y} contains {counter} bits with value 1")


def most_common_letter(x=''):  # 9
    x.lower()
    c = ' '
    m = 0
    for i in x:
        if m < x.count(i) and 'a' < i < 'z':
            c = i
            m = x.count(i)
    print(f"most common letter is {c} with {m} occurrences")


def number_of_letters(x=''):  # 10
    print(f'|{x}| contains {len(x.split(" "))} words')


gcd(3)
count_vowels("alfabet")
count_app("azi", "azi e bine, azi nu fac nimic, azi")
convert("bauBauBauBauBau")
print_spiral([
    "firs",
    "n_lt",
    "oba_",
    "htyp"
])
is_palindrome(121)
find_number("ws12defrgre123456789wedfrgre567")
count_bits(15)
most_common_letter("an apple is not a tomato")
number_of_letters("I have Python exam")
