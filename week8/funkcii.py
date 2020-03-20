def min(a, b, c, d):
    mn = a
    if mn > b:
        mn = b
    if mn > c:
        mn = c
    if mn > d:
        mn = d
    return mn

def problemA():
    a, b, c, d = map(int, input().split())
    print(min(a,b,c,d))
def power(a, n):
    b = 1.0
    for i in range(n):
        b = b * a
    return b

def problemB():
    a, n = map (float, input().split())

    print(power(a, n))
def XOR(a, b):
    if a == b:
        return 0
    else:
        return 1
def problemC():
    a, n = map(int,input().split())
    print(XOR(a,n))
problemC()