#!/usr/bin/python3
"""Willl define text file-reading function."""


def read_file(filename=""):
    """Will print contents of UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
