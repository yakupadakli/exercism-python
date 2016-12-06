
def to_rna(data):
	nucleotides = {
		"G": "C",
		"C": "G",
		"T": "A",
		"A": "U"
	}
	result = map(lambda x: nucleotides.get(x), data)
	return "".join(result) if None not in result  else ""
