"""
Chloe number is a number whose three, four and five consecutive digits sum is a prime number
"""
def first_n_digit_number(digits_number):
  first_number = str(1)
  for i in range(1, digits_number):
    first_number += '0'
  return int(first_number)

def last_n_digit_number(digits_number):
  return first_n_digit_number(1+digits_number) -1


def is_prime(number):
  # starts from 2 up to the number
  if number == 2 or number == 3 or number == 5 or number == 7:
    return True
  return number %2 != 0 and number %3 != 0 and number %5 !=0 and number %7 != 0

def prime_digit_sum(digits):
  prime_count = 0
  for i in range (first_n_digit_number(digits), last_n_digit_number(digits)):
    if consecutive_digits(i, 3) :
      if consecutive_digits(i, 4):
        if consecutive_digits(i, 5):
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