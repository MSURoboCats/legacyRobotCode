#!/usr/bin/env python3


def factorial(value):
    if value <= 1:
        return 1
    return value * factorial(value - 1)


if  __name__ == "__main__":
    print(factorial(5))

