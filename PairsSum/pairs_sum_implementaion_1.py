def return_pairs_sum(collection, number):
  for (i =0; i < len(collection), ++i) {
    for (j = i+1; j < len(collection); j++) {
      if (collection[i] + collection[j] == number): return True
    }
  }
  return False

print(return_pairs_sum([0,3,5,9,11,13,17,19], 8))