#!/usr/bin/python3
"""Will define Python class-to-JSON function."""


def class_to_json(obj):
    """Brings back dictionary represntation of a simple data structure."""
    return obj.__dict__
