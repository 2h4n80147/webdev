import math


def P333():

    a = int(input())
    b = int(input())
    for i in range(a, b+1):
        if i % 2 == 0:
            print(i)
def P334():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    for i in range(a,b+1):
        if (i%d == c):
            print (i, end=' ')
def P335():
    a = int(input())
    b = int(input())
    for i in range(a,b+1):
        c = int(math.sqrt(i))
        if c*c == i:
            print(i, end=' ')
def P339():
    x = int(input())
    for i in range(2, x):
        if x % i == 0:
            print(i)
            break

def problemH():
    x = int(input())
    for i in range(1, x+1):
        if x % i == 0:
            print(i, end=' ')

def problemI():
    x = int(input())
    count = 0
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            count = count+1
            if i*i != x:
                count = count+1
    print(count)
def problemJ():
    sum = 0
    for i in range(100):
        x = int(input())
        sum = sum + x
    print(sum)
def problemK():
    n = int(input())
    sum = 0
    for i in range(n):
        x = int(input())
        sum = sum + x
    print(sum)
def problemM():
    n = int(input())
    zeroes = 0
    for i in range(n):
        x = int(input())
        if x == 0:
            zeroes = zeroes+1
    print(zeroes)