#
# schneller weg um fibonacci mit matrizen zu berechnen
#


def mul(A, B):
    a, b, c = A
    d, e, f = B
    return a * d + b * e, a * e + b * f, b * e + c * f


def pow(A, n):
    if n == 1:
        return A
    if n & 1 == 0:
        return pow(mul(A, A), n >> 1)
    else:
        return mul(A, pow(mul(A, A), (n - 1) >> 1))


def fib(n):
    if n < 2:
        return n
    return pow((1, 1, 0), n - 1)[0]


for i in range(50):
    print(fib(i))