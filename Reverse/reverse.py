#Complete the solution so that it reverses all of the words within the string passed in.
def reverse_string(string):
      return ' '.join(string.split()[::-1])


print(reverse_string("Hello greatest victory is that which requires no battle"))