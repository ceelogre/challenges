def return_pairs_sum(collection, number):

  First_index = 0
  Last_index = len(collection) -1
  while (First_index != Last_index):
    if collection[First_index] + collection[Last_index] == number:
      return True
    if collection[First_index] + collection[Last_index] > number:
      Last_index = Last_index - 1
    else:
      First_index = First_index +1
  return False


print(return_pairs_sum([0,3,5,9,11,13,17,19], 8))