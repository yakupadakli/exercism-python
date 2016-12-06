import string


def is_pangram(data):
    data = filter(lambda x: x.isalpha(), list(set(data.lower())))
    return string.ascii_lowercase == "".join(sorted(data))
