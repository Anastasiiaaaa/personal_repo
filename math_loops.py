def my_times(a, b):
    result = 0
    sign = 1
    if b < 0 and a < 0:
        b = abs(b)
        a = abs(a)
    elif b < 0 and a > 0:
        sign = -1
        b = abs(b)
    for i in range(b):
        result = result + a
    return result


print(my_times(3, -6) == -18)
print(my_times(3, 6) == 18)
print(my_times(-3, -6) == 18)
print(my_times(-3, 6) == -18)


def my_power(x, p):
    result = 1
    sign = 1
    if x == 0 and p != 0:
        return 0
    if x == 0 and p == 0:
        return 1
    if p < 0:
        for i in range(abs(p)):
            result = result * x
        result = 1 / result
    else:
        for i in range(abs(p)):
            result = result * x
    return result


print(my_power(10, 3) == 1000)
print(my_power(10, -3) == 0.001)
print(my_power(-10, 3) == -1000)
print(my_power(-10, -3) == -0.001)
print(my_power(0, 3) == 0)
print(my_power(0, 0) == 1)
print(my_power(10, 0) == 1)
print(my_power(-10, 0) == 1)


def my_factorial(x):
    result = 1
    assert x >= 0
    if x == 0:
        result = 0
    else:
        for i in range(1, x + 1):
            result = result * i
    return result


print(my_factorial(3) == 6)


def my_geometric(x):
    result = 0
    for i in range(1, 10000):
        result = result + x ** i
    return result


print(my_geometric(9))


def my_factorial(x):
    result = 1
    assert x >= 0
    if x == 0:
        result = 1
    else:
        for i in range(1, x + 1):
            result = result * i
    return result


def my_exp(y):
    result = 0
    for i in range(0, 1000):
        b = my_factorial(i)
        assert b > 0
        result += y ** i / b
    return result


print(my_exp(3))


def my_ln_mini(x):
    assert x > -1 and x <= 1
    result = 0
    for i in range(1, 1000):
        b = i + 1
        q = -(1 ** b) / i
        result = q * x ** i
    return result


print(my_ln_mini(0.5))

from math import pi
import math


def my_factorial(x):
    result = 1
    assert x >= 0
    if x == 0:
        result = 1
    else:
        for i in range(1, x + 1):
            result = result * i
    return result


def my_sin(x):
    result = 0
    n = 0
    last = -1
    while True:
        h = 2 * n + 1
        b = my_factorial(h)
        o = (-1) ** n / b
        result += o * x ** h
        if result == last:
            break
        last = result
        n = n + 1
    return result


num = math.pi
print(my_sin(num), math.sin(num))
