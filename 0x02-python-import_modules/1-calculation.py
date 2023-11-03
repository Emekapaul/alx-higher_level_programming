#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5

    addResult = add(a, b)
    subResult = sub(a, b)
    mulResult = mul(a, b)
    divResult = div(a, b)

    print('{} + {} = {}'.format(a, b, addResult))
    print('{} - {} = {}'.format(a, b, subResult))
    print('{} * {} = {}'.format(a, b, mulResult))
    print('{} / {} = {}'.format(a, b, divResult))


if __name__ == "__main__":
    main()
