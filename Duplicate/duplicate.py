import sys 

def dup_count(word):
  # convert string to list
  word_list = [ letter for letter in word.casefold()]

  # return unique values
  word_list_unique = set(word_list)

  # get the count for every unique letter
  dups = 0
  for letter in word_list_unique:
    count = word_list.count(letter)

    if count > 1:
      dups +=1
  return dups

print(dup_count(sys.argv[1]))
