def first_unique(array):
  for index, element in enumerate(array):
    # remove the elt
    array.pop(index)
    if element not in array:
      return element
  return 'No unique element'

print(first_unique([3, 9, 19, 9, 34, 1, 3]))
print(first_unique([6, 2, 60, 49, 2, 4, 10, 3]))
print(first_unique([2, 2]))
print(first_unique([]))