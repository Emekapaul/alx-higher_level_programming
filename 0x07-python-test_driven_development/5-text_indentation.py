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

    for i, ch in enumerate(text):
        if ch in [".", "?", ":"]:
            print(ch)
            print()

        elif text[i - 1] in [".", "?", ":"] and ch == " ":
            pass

        else:
            print(ch, end="")
