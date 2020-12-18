# Lists use []
# Tuples (Arrays) use ()
# Sets use {}

s = {"coco", "shea", "nut"}
print(s)


s.add("olive")
print(s)

s.add(4)
print(s)

# Will NOT allow duplication
s.add(4)
print(s)

l = [1, 2, 3, 4, 4, 4, 5, 5, 4, 5, 6, 6, 7, "1", "1"]
duplicates_removed_set = set(l)
print(duplicates_removed_set)
duplicates_removed_list = list(duplicates_removed_set)
l = duplicates_removed_list
print(l)
print()

library_1 = {"Harry Potter", "Romeo and Juliet", "LOTR"}
library_2 = {"Harry Potter", "Of Mice and Men", "ASOIAF"}

lib_all = library_1.union(library_2)
print(lib_all)

shared = library_1.intersection(library_2)
print(shared)

unique = library_1.symmetric_difference(library_2)
print(unique)
