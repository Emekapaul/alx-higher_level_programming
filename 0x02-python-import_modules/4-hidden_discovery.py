#!/usr/bin/python3
import hidden_4


def main():
    output = dir(hidden_4)
    for name in output:
        if (name[:2] == '__'):
            continue

        else:
            print(name)


if __name__ == "__main__":
    main()
