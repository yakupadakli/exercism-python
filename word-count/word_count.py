def decode_if_needed(string):
    try:
        return string.decode('utf-8')
    except AttributeError:
        return string


def word_count(data):
    result = {}
    data = decode_if_needed(data)
    data = "".join([x.lower() if x.isalnum() else " " for x in data]).split()
    for word in data:
        if result.get(word):
            result[word] += 1
        else:
            result[word] = 1
    return result
