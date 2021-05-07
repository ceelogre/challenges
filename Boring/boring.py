def filter_x(predicate, digits):
  return [x for x in digits if  x[1] == predicate]

def is_boring(left_edge, right_edge):
  boring_numbers = 0
  for number in range(left_edge, right_edge +1):
    digits_list = [ (int(j), 1 if (i+1) % 2 == 1 else 2) for i,j in enumerate(str(number))]
    ones = filter_x(1, digits_list)
    twos = filter_x(2, digits_list)
    even_in_ones = [x for x in ones if x[0]%2 == 0]
    odd_in_twos= [x for x in twos if x[0] %2 != 0]
    
    if(even_in_ones == [] and odd_in_twos == []): 
      print(number)
      boring_numbers += 1

  return boring_numbers

print(is_boring(20, 30))