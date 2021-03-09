import sys

def capitalize(word):
	return " ".join([i.capitalize() for i in word.split()])

print(capitalize(sys.argv[1]))
