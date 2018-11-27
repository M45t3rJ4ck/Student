# Print out the first n Fibonacci numbers (using the previous Fibonacci function is useful. Do this recursively, NO LOOPS)
n = int(input("Enter a number to start the fibonacci sequence: "))


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        return result


print(fib(n))
