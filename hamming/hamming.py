
def distance(strands1, strands2):
    if len(strands1) != len(strands2):
        raise ValueError
    return len(filter(lambda x: x[0] != x[1],zip(strands1, strands2)))
