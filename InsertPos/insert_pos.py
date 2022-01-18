def search_insert_pos(nums, target):
  try:
    pos = nums.index(target)
  except ValueError:
    for index, num in enumerate(nums):
      if num+1 == target:
        pos = index+1 
  return pos

def sip_log(nums, target):
  try:
    pos = nums.index(target)
  except ValueError:
    mid = len(nums)//2
    if nums[mid] > target:
     pass 
    else:
      pass

print(search_insert_pos([1,3,5,6], 0))