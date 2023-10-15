import datetime


def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_with_time(n: int) -> str:
    print(f'Started fibonnacci for = {n}, start time = {datetime.datetime.now()}')
    result = fibonacci(n)
    print(f'Finished fibonnacci for = {n}, end time = {datetime.datetime.now()}')
    return f'fib({n}) = {result}'
