"""
Docstring for functions_module module
"""


def filter_longer_words(*words, n=0):
    filtered = []
    for word in words:
        if len(word) > n:
            filtered.append(word)
    return filtered
