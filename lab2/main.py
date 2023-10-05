def fibo(n):
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


print(fibo(3))
