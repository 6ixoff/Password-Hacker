def fibonacci(n):
    first = 0
    second = 1
    for i in range(n):
        if i == 1:
            yield 1
        elif i == 0:
            yield 0
        else:
            result = first + second
            first = second
            second = result
            yield result
