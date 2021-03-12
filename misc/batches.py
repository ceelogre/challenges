
def return_in_threes (number):
  iterations = len(str(number)) - 4
  i, j = 0, 4
  threes = []
  for k in range(iterations+1) :
    threes.append(str(number)[i:j])
    i += 1
    j += 1
  return threes

print(return_in_threes(int(input())))