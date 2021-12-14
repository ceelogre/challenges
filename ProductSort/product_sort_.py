def occurrence_dict(L):
  occurrences = {}
  for key in L:
    if key in occurrences:
      occurrences[key] += 1
    else:
      occurrences[key] = 1
  return occurrences

def merge_sort(L):
  if len(L) == 1:
    return L
  middle = len(L) // 2
  left = L[0:middle]
  right = L[middle:]
  return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
  results = []

  while (len(left) > 0 and len(right) > 0):
    if left[0] > right[0]:
      results.append(right.pop(0))
    else:
      results.append(left.pop(0))
  while(len(left) > 0):
    results.append(left.pop(0))
  while(len(right) > 0):
    results.append(right.pop(0))
  return results

def sort_products(L):
  o = occurrence_dict(L)

  freq_list = []
  for key in o:
    freq_list.append((o[key], key))

  freq_ = merge_sort(freq_list)

  sorted_list = []
  for i in freq_:
    sorted_list.extend([i[1]] * i[0])
  return sorted_list

print(sort_products([4,5,6,5,4,3]))
print(sort_products([8,5,5,5,5,1,1,1,4,4]))