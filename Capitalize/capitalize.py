import sys

def capitalize(word):
  word_in_list = word.split()

  for index, item in enumerate(word_in_list):
    word_in_list[index] = item.capitalize()

  return " ".join(word_in_list)

print(capitalize(sys.argv[1]))