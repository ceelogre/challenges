def check_check(index, array):
  if array[index] in 'aeiou':
    lastMatchIndex =check_check(index + 1, array)
    return lastMatchIndex
  else:
    check_check(index + 1, array)
  return index

def longest_vowels(string):
  sortedStringArray = (sorted(string))
  last = check_check(0, sortedStringArray)
  return last

print(longest_vowels('hello'))