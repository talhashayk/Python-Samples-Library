l1 = [1, 2, 3, 4, 5]
l2 = ["un", "deux", "trois", "quatre", "cinq"]
zipped_duo = list(zip(l1, l2))
print(zipped_duo)

l3 = ["1", "2", "3", "4", "5"]
zipped_trio = list(zip(l1, l2, l3))
print(zipped_trio)

zip_mixed = list(zip(zipped_duo, zipped_trio))
print(zip_mixed)

unzip_mixed = list(zip(*zip_mixed))
print(unzip_mixed)

re_unzip_mixed = list(zip(*unzip_mixed))
print(re_unzip_mixed)

re_re_unzip_mixed = list(zip(*re_unzip_mixed))
print(re_re_unzip_mixed)

unzip_duo = list(zip(*zipped_duo))
print(unzip_duo)

unzip_trio = list(zip(*zipped_trio))
print(unzip_trio)

# FROM
"""
for i in range(5):
    print(l1[i])
    print(l2[i])
"""

# TO
for (list1, list2) in zip(l1, l2):
    print(list1)
    print(list2)

items = ["Apples", "Bananas", "Oranges"]
counts = [2, 3, 2]
prices = [0.99, 1.05, 0.59]

sentences = []
for (items, counts, prices) in zip(items, counts, prices):
    sentence = "I bought " + str(counts) + " " + \
        str(items) + " at £" + str(prices) + " each."
    sentences.append(sentence)

print(sentences)
