#!/usr/bin/python3
"""Will define JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Sribe object to a text file utilizing JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
