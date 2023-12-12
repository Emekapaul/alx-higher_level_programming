#!/usr/bin/python3

"""The 5-text_indentation modul defines the func: text_indentation(text)"""


def text_indentation(text):
    """function that prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        text (string): The string to print
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    b = True
    for i, ch in enumerate(text):
        if b and text[0] == " ":
            b = False
            pass
        elif ch in [".", "?", ":"]:
            print(ch)
            print()

        elif i > 0 and text[i - 1] in [".", "?", ":", " "] and ch == " ":
            pass

        else:
            print(ch, end="")
