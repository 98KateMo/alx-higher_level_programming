# 8-multiple_returns.py
#!/usr/bin/python3


def multiple_returns(sentence):
    """Returns length of a string & its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
