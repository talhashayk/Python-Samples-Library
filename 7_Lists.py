l = ["un", "deux", "trois"]
print(l)
l2 = [1, "deux", "3", [], [1, 2, 4], True]
print(l2)
print(l2[4])
l2.append([1, 2, 4, 2, 2, 3])
print(l2)
l2.insert(2, [1, 2, 4, 2, 2, 3])
print(l2)
l3 = [13, 4, 2, 1]
l3.sort()
print(l3)
l3.sort(reverse=True)
print(l3)
l2.reverse()
print(l2)

for value in l2:
    print(value)

bmt = "   big man thing"
print(bmt)
bmt = bmt.strip(" ")
print(bmt)
bmt = bmt.replace(' ', '')
print(bmt)
l3.extend(bmt)
print(l3)

lll = ["un", "deux", "trois"]
ll = ["un", "deux", "trois"]
ll.append(lll.pop(1))
print(ll)

print("\n\n")
list_1 = [1, 2]
list_2 = [4, 3, 5, 6, 7]
print(list_1)
print(list_2)

for i in list_2:
    list_1.append(i)

list_2.clear()

# list_1.append(list_2)
print(list_1)
print(list_2)
