def readtxt(txt):
	lst = []
	file = open(txt, "r")
	for line in file:
		lst.append(line)
	return lst
