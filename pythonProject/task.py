def fibonacci_generator(limit=None):

    a, b = 0, 1
    count = 0
    while True:
        if limit and count >= limit:
            break
        yield a
        a, b = b, a + b
        count += 1

    fibonacci_sequence = fibonacci_generator(10)
    print(list(fibonacci_sequence))
