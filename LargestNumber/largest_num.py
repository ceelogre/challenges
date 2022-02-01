import sys
from itertools import permutations
def largest_num(L):
  # convert to str
  L_ = [str(num) for num in L]

  perms = list(permutations(L_))

  #generate all permutations
  #perms = []
  #for i in range(len(L_)):
    #perms.extend(permutations(L_, i))

  highest = -1
  for perm in perms:
    num =  ''.join(perm)
    if int(num) > highest:
      highest = int(num)

#  L_str = ""
#  for item in L_:
#    L_str += item
#  
#  L_str_num = int(L_str)
  return highest

input_ = (sys.argv[1])
str_numbers = input_.strip('[]')
L = list(map(int, str_numbers.split(',')))
print(largest_num(L))