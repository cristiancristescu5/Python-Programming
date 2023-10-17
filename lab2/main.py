import math
import string


def fibo(n):  # 1
    fibo_list = []
    if n <= 0:
        print("Incorrect input")
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    x = 1
    y = 1
    n = n - 2
    fibo_list.append(x)
    fibo_list.append(y)
    while n > 0:
        z = x + y
        fibo_list.append(z)
        x = y
        y = z
        n -= 1

    return fibo_list


def is_prime(x):
    if x == 1:
        return False
    if x == 2 or x == 3 or x == 7:
        return True
    for d in range(2, int(math.sqrt(x)) + 1):
        if x % d == 0:
            return False

    return True


def prime_list(x):  # 2
    result_list = []
    for i in x:
        if is_prime(i):
            result_list.append(i)
            print(i)
    return result_list


def process_lists(a: list, b: list):  # 3
    intersected = []
    union = []
    dif1 = []
    dif2 = []
    for i in a:
        if b.count(i) != 0:
            intersected.append(i)
    for i in a:
        if union.count(i) == 0:
            union.append(i)
    for i in b:
        if union.count(i) == 0:
            union.append(i)

    for i in a:
        if b.count(i) == 0:
            dif1.append(i)

    for i in b:
        if a.count(i) == 0:
            dif2.append(i)

    return [intersected, union, dif1, dif2]


def create_song(i, notes: list, moves: list):  # 4
    song = [notes[i]]
    position = i
    for j in moves:
        position += j
        while position > len(notes) - 1:
            position = position - len(notes)
        song.append(notes[position])
    return song


def replace_diagonal(matrix):  # 5
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix[0])):
            if i > j:
                matrix[i][j] = 0
    return matrix


def process_lists_var(*lists, x):
    result_list = []
    el = []
    l: list
    for l in lists:
        result_list = list(set(result_list) | set(l))
    for i in result_list:
        count = 0
        for h in lists:
            count += h.count(i)
        if count == x:
            el.append(i)
    return el


def isPalindrome(x):
    inv = 0
    y = x
    while x != 0:
        inv = inv * 10 + x % 10
        x = x // 10
    if inv == y:
        return True
    return False


def palindrome_tuple(x: list):
    max_ = 0
    count = 0
    for i in x:
        if isPalindrome(i):
            count += 1
            if i > max_:
                max_ = i
    return count, max_


def ascii_list(string_list: list[string], flag, x=1):
    result_chars = []
    for s in string_list:
        chars = []
        for c in s:
            if flag and ord(c) % x == 0:
                chars.append(c)
            if not flag and ord(c) % x != 0:
                chars.append(c)
        result_chars.append(chars)
    return result_chars


def spectators(seats):
    rows = len(seats)
    cols = len(seats[0])
    pos = []
    for j in range(cols):
        for i in range(1, rows):
            el = seats[i][j]
            for m in range(i - 1, 0, -1):
                if seats[m][j] >= el:
                    pos.append((i, j))
                    break

    return pos


def lists_to_tuples(*lists: list):  # 10
    tuples = []
    max_length = 0
    for l in lists:
        if len(l) > max_length:
            max_length = len(l)

    for i in range(max_length):
        single_tuple: tuple = ()
        for j in lists:
            if len(j) <= i:
                single_tuple = single_tuple + (None,)
            else:
                single_tuple = single_tuple + (j[i],)
        tuples.append(single_tuple)
    return tuples


def sort_list_tuples(tuples: list[tuple]):
    tuples.sort(key=lambda i: i[1][2])
    return tuples


# print(fibo(3))
# print(prime_list([1, 2, 3, 4, 5, 6, 7, 12, 17, 11, 13, 14, 25, 23, 78, 31, 41, 51]))
# print(process_lists([1, 2, 3], [1, 3, 4, 5]))
# print(create_song(2, ["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2]))
# print(replace_diagonal([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
# print(process_lists_var([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=1))
# print(palindrome_tuple([121, 131, 141, 151, 161, 171, 100001]))
# print(ascii_list(["test", "hello", "lab002"], False, 2))
# print(spectators([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]))
print(lists_to_tuples([1, 2, 3, 4, 9, 10], [5, 6, 7, 8], ["a", "b", "c"]))
print(sort_list_tuples([("abc", "bcd"), ("abc", "zza")]))
