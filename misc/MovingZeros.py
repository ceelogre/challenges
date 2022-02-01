#Given a list of integers, move all zeros to the end of the list preserving the order of the other elements.
def moveZeros(l):
  for num in l:
    if num == 0:
      l.remove(num)
      l.append(num)
  return l

print(moveZeros([1, 2, 0, 3, 0, 4, 5, 0]))
print(moveZeros([1,0,1,2,0,1,3]))