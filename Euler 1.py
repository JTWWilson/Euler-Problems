"""
The solution to Euler Project Problem 1
https://projecteuler.net/problem=1
"""


def calculate():
    """
    Calculates the sum of all of the positive multiples of 3 and 5 that are less tha 1000
    :returns: sum of all of the values
    """
    l = []
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            l.append(i)
    return sum(l)

print(calculate())


def listcomprehension():
    """
    Wondered hoe small I could crush the function after reading about one line list comprehensions
    (http://blog.teamtreehouse.com/python-single-line-loops)
    ...it works!
    """
    return sum([i for i in range(0, 1000) if i % 3 == 0 or i % 5 == 0])

print(listcomprehension())
