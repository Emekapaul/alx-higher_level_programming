#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5

    addResult = add(a, b)
    subResult = sub(a, b)
    mulResult = mul(a, b)
    divResult = div(a, b)

    print(f'{a} + {b} = {addResult}')
    print(f'{a} - {b} = {subResult}')
    print(f'{a} * {b} = {mulResult}')
    print(f'{a} / {b} = {divResult}')


if __name__ == "__main__":
    main()
