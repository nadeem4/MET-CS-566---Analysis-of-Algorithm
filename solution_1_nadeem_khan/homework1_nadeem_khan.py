"""
Course: MET CS 566 A2 - Analysis of Algorithm.
BU ID: U03225602
Name: Nadeem Khan
question: write 2 algo

Algo 1: x**n = x*(x**(n-1))

Algo 2:
n = 2**m
X**n = ((X**2) **2) **2…, etc.
[NOTE: the symbol of power (**) is used m times here, i.e., X**8 = ((X**2) **2) **2, because 8 = 2**3].
"""


def algo_1(x, n):
    res = 1
    for i in range(0, n):
        res *= x
    return res


def algo_2(x, m):
    for i in range(0, m):
        x = x ** 2
    return x


if __name__ == '__main__':
    res_1 = algo_1(2, 8)
    print(res_1)

    res_2 = algo_2(2, 3)
    print(res_2)

"""
Algo 2 will take lesser time, since it will perform less iteration than algo 1. 
For same power, Algo 2 will perform 3 steps whereas Algo 1 will perform 8 steps.
"""