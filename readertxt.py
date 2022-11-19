def readtxt(txt):
	lst = []
	file = open(txt, "r", encoding="utf-8")
	for line in file:
		lst.append(line)
    file.close()
	return lst
