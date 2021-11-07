def add_arrays(arr1, arr2):
  arr3 = [a+b for a,b in zip(arr1, arr2)]
  return arr3
print(add_arrays([7, 8, 2], [1, 3, 8]))
print(add_arrays([3, 5, -2], [9, 1, 0]))