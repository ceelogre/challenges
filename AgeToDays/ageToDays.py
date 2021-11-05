# return ages in days
def ageToDays(age):
    return  age * 365 if age >= 0 else 'Can\'t be negative'
print(ageToDays(65))
print(ageToDays(0))
print(ageToDays(20))
print(ageToDays(-1))