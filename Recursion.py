# Now that you have read and understood example.py, write recursive functions for the following tasks. Write all of the recursive functions in a file
# called “recursion.py”:

# 1.)Reverse a string
print("1.) Reverse...")
esrever = str(input("Enter your string: "))


def reverse(esrever):
    reverse = esrever[::-1]
    return reverse


print(reverse(esrever))

# 2.)Find the factorial of an integer (factorial (5) = 5 x 4 x 3 x 2 x 1)
print("2.) Factorial...")
n = int(input("Enter a number to start Factorial Calculations: "))


def factorial(n):
    if n <= 1:
        return 1
    else:
        calc = n * factorial(n - 1)
        print("Calculating factorial ", n, " of ", (n - 1), " : ", calc)
        return calc


print(factorial(n))

# 3.)Calculate the nth Fibonacci number (Fibonacci numbers are a sequence where each number is the sum of the previous two - 0 1 1 2 3 5 8 etc.)
print("3.) Fibonacci... ")
n = int(input("Enter a number to start Fibonacci sequence: "))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        return result


print(fibonacci(n))
