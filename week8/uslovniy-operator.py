def p292():
    a = int(input())
    b = int(input())
    print(max(a, b))


def p253():
    year = int(input())
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print('YES')
            else:
                print('NO')
        else:
            print('YES')
    else:
        print('NO')


def p2960():
    a = int(input())
    b = int(input())
    x, y, z, w = [a % 10, a // 10 % 10, a // 100 % 10, a // 1000 % 10]

    c = 0

    if (x == w and y == z):
        c = 1
    else:
        c = 0

    if (c == 1 and b == 1) or (c != 1 and b != 1):
        print('YES')
    else:
        print('NO')

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
def p2959():
    x = int(input())
    print(sign(x))

def P293():
    a = int(input())
    b = int(input())
    if a > b:
        print(1)
    elif  a < b:
        print(2)
    else:
        print(0)
