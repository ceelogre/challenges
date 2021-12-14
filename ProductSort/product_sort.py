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

  ones = [number for number in o if o[number] == 1 ]
  ones_ = merge_sort(ones)

  more = [number for number in L if number not in ones]
  more_than_one_freq = occurrence_dict(more)
  freqs = []
  for key in more_than_one_freq:
    #key, value is reversed so merge_sort picks the correct sorting key
    freqs.append((more_than_one_freq[key],key))

  freqs_ = merge_sort(freqs)
  results = []
  for item in freqs_:
    results.extend([item[1]] * item[0])
  return ones_+ results

print(sort_products([8,5,5,5,5,1,1,1,4,4]))