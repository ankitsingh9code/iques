def fibonacci_series(n):
    fib_series = [0,1]
    for i in range(0,n-2):
        fib_series.append(fib_series[-1]+fib_series[-2])
    return fib_series

print(fibonacci_series(8))
    