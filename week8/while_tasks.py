import math


def problemA():
    n = int(input())
    i = 0
    while (i <= n):
        c = int(math.sqrt(i))
        if (c * c == i):
            print(i)
        i = i+1

def problemB():
    n = int(input())

    i = 2
    while (i <= n):
        if (n % i == 0):
            print(i)
            break
        i = i+1
def problemC():
    n = int(input())

    i = 1
    while (i <= n):
        print(i, end=' ')
        i = i * 2
def problemD():
    n = int(input())
    x = (n & (n - 1))
    if x == 0:
        print('YES')
    else:
        print('NO')
def problemE():
    n = int(input())
    k = 0
    while (2**k < n):
        k=k+1
    print(k)
problemE()

