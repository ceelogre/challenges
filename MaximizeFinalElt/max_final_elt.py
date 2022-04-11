def get_max_value(arr):
  a = sorted(arr)
  a[0] = 1
  for index, elt in enumerate(a):
    if len(a) > index+1:
      if a[index+1] - a[index] > 1:
        a[index+1] -= 1
  return a[-1]
print(get_max_value([3,2,3,5]))