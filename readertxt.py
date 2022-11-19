def readtxt(txt):
	lst = []
	try:
		file = open(txt, "r")
		for line in file:
			lst.append(line)
		return lst
	except Exception:
		return None
