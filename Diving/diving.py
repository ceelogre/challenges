def diving_mini(array):
  maxBreath = 10
  for item in array:
    maxBreath += 4 if item >= 0 else -2

  return True if maxBreath > 0 else False

print(diving_mini([-5, -15, -4, 0, 5]))
print(diving_mini([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # true
print(diving_mini([-3, -6, -2, -6, -2])) # false
print(diving_mini([2, 1, 2, 1, -3, -4, -5, -3, -4])) # false