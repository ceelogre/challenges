def debt_evader(payments_array):
  # start at the first element
  #loop through all payments taking sum of all prev elements
  # if at any point sum is less than zero, move the element to the end
  #repeat
  # if we reach the end of the array and the sum is positive stop

  index = 0
  array_sum = 0
  relocations = 0
  while (index < len(payments_array)):
    array_sum = sum(payments_array[:index+1])
    if array_sum < 0:
      neg_sum_elt = payments_array.pop(index)
      payments_array.append(neg_sum_elt)
      relocations += 1
      index, array_sum = -1, 0
    index += 1
  return relocations

print(debt_evader([2,8,7,-5,10]))
print(debt_evader([2,8,-7,-5,10]))
print(debt_evader([10, -9, -2, -1, 3, -4, 3]))
print(debt_evader([-1, -1, -1, 1, 1, 1, 1]))
print(debt_evader([10, -10, -1, -1, 10]))