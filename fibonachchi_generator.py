def generate_fibonachchi():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = generate_fibonachchi()
for _ in range(13):
    print(next(fib))


def generate_fibonachchi1(n):
    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a + b
    yield a

user_n = 13
for i in range(user_n):
    print(next(generate_fibonachchi1(i)))

