# Mutations
def mutate_string(string, position, character):
    new_string = string[:position] + character + string[position+1:]
    return new_string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end='')
# Arithmetic Operations
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

