import os

def readtxt(txt):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'txt')
	lst = []
	try:
		file = open(filename, "r")
		for line in file:
			lst.append(line)
		return lst
	except Exception:
		return None
