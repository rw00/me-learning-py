str1 = "Python"
str2 = "Python"
print(id(str1) == id(str2)) # same id because strings are interned and immutable
print(str1 is str2) # reference equality
print(str1 == str2) # object equality
