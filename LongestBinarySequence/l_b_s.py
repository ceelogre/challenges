import sys
import random

def findMaxConsecutiveOnes(nums):
  # remove 0b from the beginning of the binary string
  binary_nums = [x[2:] for x in nums]
  ones_list = ''.join(str(x) for x in binary_nums).split('0')
  longest = -1
  for consec_ones in ones_list:
      print(consec_ones)
      if len(consec_ones) > longest:
        longest = len(consec_ones)
          
  return longest

# get the length of array from the input using argv
nums = int(sys.argv[1])

# create an array of 0s and 1s
# convert to 50 to binary
a = bin
binary_array = [bin(random.randint(100000, 1000000)) for i in range(nums)]

print(findMaxConsecutiveOnes(binary_array))