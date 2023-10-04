import math


def gcd(x): #1
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


def count_vowels(x=''): #2
    vowels = "aeiou"
    result = 0
    for s in vowels:
        result += x.count(s)
    print(f"The number of vowels in {x} = {result}")
    return result


def count_app(x='', y=''): #3
    print(f"{x} appears in {y}, {y.count(x)} times")
    return y.count(x)


def convert(x=''): #4
    result = ''
    for c in x:
        if c.islower():
            result += c
        else:
            result += '_'
            result += c.lower()
    print(f"Initial string = {x}, converted string = {result}")


def prin_spiral(x): #5
    for row in x:
        for column in row:
            print('bau')


count_vowels("alfabet")
count_app("azi", "azi e bine, azi nu fac nimic, azi")
convert("bauBauBauBauBau")
