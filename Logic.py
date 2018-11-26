# Collecting user input
U_prime = int(input("Please enter a number to check if it is prime: "))
is_prime = str(U_prime) + " is a prime number."
isn_prime = str(U_prime) + " isn't a prime number."
for num in range(2, U_prime):
    if (U_prime % num) != 0:
        print(isn_prime)
    else:
        print(is_prime)
        

