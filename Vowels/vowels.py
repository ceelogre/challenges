# Return the number (count) of vowels in the given string
# "aerial" => "2"
# "yield fire" => "2"
# "Abracadabra" => "1

def vowelsCount(str):
  count = 0
  vowels = ['a', 'e', 'i', 'u', 'o'] 
  for letter in str:
    if letter in vowels:
        count += 1
  return count

print(vowelsCount("aerial"))
print(vowelsCount('abbracadabra'))
print(vowelsCount('yield fire'))