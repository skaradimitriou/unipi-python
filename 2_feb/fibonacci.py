## recursive method

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


# alternative method. Much faster
def fibo1(n):
    if n == 1 or n == 2:
        return 1

    a = 1
    b = 1

    for i in range(n - 2):
        tmp = a + b
        a = b
        b = tmp
    return b


print(fibo1(50))
