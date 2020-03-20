def problemA():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    for i in range(0,n, 2):
        print(a[i],end=' ')
def problemB():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    for i in range(0,n):
        if a[i] % 2 == 0:
            print(a[i],end=' ')
def problemC():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    count = 0

    for i in range(0,n):
        if a[i] > 0:
            count = count+1
    print(count)

def problemD():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    prev = 0
    count = 0
    for i in range(0,n):
        if i > 0 and a[i] > prev:
            count = count+1
        prev = a[i]
    print(count)

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 1

def problemE():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    prev = 0
    count = 0

    for i in range(0, n-1):
        if (sign(a[i]) == sign(a[i+1])):
            print('YES')
            return
    print('NO')

def problemF():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    prev = 0
    count = 0

    for i in range(1, n-1):
        if a[i] > a[i-1] and a[i] > a[i+1] :
            count = count + 1
    print(count)
def problemG():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    a = list(reversed(a))
    for i in range(n):
        print(a[i], end = ' ')
problemG()

