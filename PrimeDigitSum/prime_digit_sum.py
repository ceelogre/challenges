"""
Chloe number is a number whose three, four and five consecutive digits sum is a prime number
"""

def is_prime(number):
  # starts from 2 up to the number
  digits_sum = 0
  while ( number != 0):
    digits_sum += number %10
    number = number // 10

  # one is not a prime number as it doesn't have two factors
  if digits_sum == 1: return False 
  if digits_sum == 2 or digits_sum == 3 or digits_sum == 5 or digits_sum == 7:
    return True
  return digits_sum %2 != 0 and digits_sum %3 != 0 and digits_sum %5 !=0 and digits_sum %7 != 0

def prime_digit_sum(digits):
  prime_count = 0
  # any number below 9999 cannot satisfy the condition as 5 digits sums are not available
  if digits < 5: return prime_count

  for i in range (10 **(digits-1), 10 **digits ):
    if consecutive_digits(i, 3) :
      if consecutive_digits(i, 4):
        if consecutive_digits(i, 5):
          print(i)
          prime_count += 1 
  return prime_count

def consecutive_digits(current_number, partitions):
  
  iterations = len(str(current_number)) - partitions 
  i, j = 0, partitions
  for k in range(iterations+1) :
    if not is_prime(int(str(current_number)[i:j])):
      return False
    i += 1
    j += 1
  return True

print(prime_digit_sum(int(input())))