# Immutable
"""
- Tuples
- Ints
- Floats
- Booleans
"""

# Mutable
"""
- Lists
- Dictionaries
- Sets
"""

tup = (1, 2, 3, [1, 2, 3])
# Can't change any element within tuple but can change elements within the list in the tuple
print(tup)
tup[3][1] = 8
print(tup)

tup = (1, 2, 3, (1, 2, 3))
# Can't change any element within tuple or tuple within the tuple
