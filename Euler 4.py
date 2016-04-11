"""
The solution to Euler Project Problem 4
https://projecteuler.net/problem=4
"""

def calculate():
    record = 0
    for i in range(999, 0, -1):
        for j in range(999, 0, -1):
            if ispalindrome(i * j) is True and i * j > record:
                record = i * j
    print(record)

def ispalindrome(n):
    if list(str(n))[::-1] == list(str(n)):
        return True
    else:
        return False

calculate()