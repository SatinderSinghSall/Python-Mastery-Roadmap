# Sets in Python:

s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = set()

print(s)
print(type(s))
print(len(s))

s.add(11)
print(s)

print(s2)
print(type(s2))
print(len(s2))

# Set Methods:
print(s.add(11))
print(s)

print(s.remove(11))
print(s.clear())
# print(s.pop())
print(s.union(s2))
print(s.intersection(s2))
print(s.difference(s2))
