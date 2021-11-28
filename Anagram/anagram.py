def is_anagram(string, string_):
  return sorted(string_) == sorted(string)

def anagrams(string):
  ana = []
  set_indices = []
  for index, word in enumerate(string):
    chars_list = ''.join(sorted(word))
    if chars_list  not in ana:
      ana.append(chars_list)
      set_indices.append(index)
  annie = []
  for index in set_indices:
    annie.append(string[index])
  return sorted(annie)

print(anagrams(['code','edoc', 'doce', 'framer', 'frame']))
print(anagrams(['code', 'aaagmnrs', 'anagrams', 'doce']))