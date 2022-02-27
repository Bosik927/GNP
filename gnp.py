import random


def gnp(n, p):
    "Model G(n,p)"
    a = [[0 for j in range(n)] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            ran = random.random()
            if (ran <= p):
                a[i][j] = a[j][i] = 1
    return a


def trangles(n, a):
    x = 0
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            if a[i][j]:
                for h in range(j + 1, n):
                    if (a[i][h]) and (a[j][h]):
                        x = x + 1
    return x


def rectangles(n, a):
    x = 0
    if n > 4:
        for i in range(1, n - 3):
            for j in range(i + 1, n - 1):
                if a[i][j]:
                    for k in range(j + 1, n):
                        if a[i][k]:
                            for h in range(i + 1, n):
                                if h != j and h != k:
                                    if a[j][k] and a[k][h]:
                                        x = x + 1
    return x

n = 6
p = 0.5
a = gnp(n, p)

for i in range(n):
    print(a[i])

print(trangles(n, a))
print(rectangles(n, a))
