def search_insert_pos(nums, target):
  try:
    pos = nums.index(target)
    return pos
  except ValueError:
    start_pos = 0
    end_pos = len(nums) -1
    while start_pos <= end_pos:
      mid_pos = (start_pos + end_pos) // 2
      if target > nums[mid_pos]:
        start_pos = mid_pos + 1
      else:
        end_pos = mid_pos - 1
    return start_pos

print(search_insert_pos([1,3,5,7], 4))