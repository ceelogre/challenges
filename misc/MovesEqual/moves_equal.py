def count_moves(n):
  # find the largest
  moves = 0
  increment(n)
  moves += 1

  # check if all equal
  n = sorted(n)
  while (n[0] != n[len(n) -1]): 
    moves += 1
    increment(n)
    n = sorted(n)
  return moves

def increment(n):
  largest = max(n)
  seen_max_already = False
  for index, elt in enumerate(n):
    if elt == largest and seen_max_already == False:
      seen_max_already = True
    else: n[index] = elt + 1

print(count_moves([3,2,2,2]))