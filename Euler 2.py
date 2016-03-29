"""
The solution to Euler Project Problem 2
https://projecteuler.net/problem=2
"""

def calculate():
    """
    Calculates the sum of all even Fibonacci numbers < 4 000 000
    """
    x=1
    y=2
    seq=[]
    while x<4000000 and y<4000000:
        seq.append(x)
        seq.append(y)
        x=x+y
        y=y+x
    return sum([i for i in seq if i % 2 == 0])

print(calculate())