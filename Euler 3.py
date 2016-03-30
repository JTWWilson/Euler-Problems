"""
The solution to Euler Project Problem 3
https://projecteuler.net/problem=3
"""


def calculate(num):
    answer = num
    for i in range(1, num):
        if isprime(i) is True:
            if num % i == 0:
                answer /= i
    return answer


def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
        # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
                    return False
    return True


print(calculate(600851475143))
