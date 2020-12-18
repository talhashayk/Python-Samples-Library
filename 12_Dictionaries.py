groceries = {"milk": 6, "choco": 2, 3: "lol"}
print(groceries.get("milk"))
print(groceries.get("choco"))
print(groceries.get(3))

id = {
    "talha": 123567,
    "bigman": 234568
}

print(id.get("bigman"))
print(id)

# Dictionary with lists
contacts = {
    "uno": ["123-456", "uno@lol.com", "address", 21],
    "dos": ["456-789", "dos@lol.moc", "location", 12]
}

print(contacts)
print(contacts.get("dos"))

# Dictionary with dictionaries
contacts = {
    "uno": {
        "phone number": "123-456",
        "email": "uno@lol.com",
        "address": "somewhere",
        "age": 21
    },
    "dos": {
        "phone number": "456-789",
        "email": "dos@lol.moc",
        "address": "someplace",
        "age": 12
    }
}

print(contacts)
print(contacts.get("dos"))
print(contacts.get("dos").get("email"))

contacts.pop("uno")
# "pop" removes the selected item whereas, "popitem" removes the last item from the dictionary (Both methods can be printed)
print(contacts)

print()

word_count = {}

sentence = "I like the name talha because the name talha means tree"
split_sentence = sentence.split(" ")
for word in split_sentence:
    if word_count.get(word) is None:
        i = {word: 1}
        word_count.update(i)
    else:
        count = word_count.get(word)
        count = count + 1
        i = {word: count}
        word_count.update(i)
        # Could also be word_count[word] = count (Arguably a better way)

print(word_count)

print()

print(word_count.items())
print(word_count.keys())
print(word_count.values())

print()

print(list(word_count.items()))
print(list(word_count.keys()))
print(list(word_count.values()))

total_word_count = 0

for value in list(word_count.values()):
    total_word_count = total_word_count + value

print(total_word_count)

word_count.clear()
print(word_count)

board_dictionary = {
    1: 5,
    2: 5,
    3: 5,
    4: 5,
    5: 5,
    6: 5,
    7: 5,
}

board_dictionary[2] -= 1
print(board_dictionary)
