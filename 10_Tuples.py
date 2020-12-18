t = (1, 2, 3)
print(t[1])

debit_card_uno = (1234567890, "Mr T Sheikh", "08/21", 123)
debit_card_dos = (1234567890, "Mr T Sheikh", "08/21", 123)

debit_cards = [debit_card_uno, debit_card_dos]
print(debit_cards)

# UNPACKING
person_uno = ("Big T", 21, "All food")
person_dos = ("Lil T", 21, "All food")

mandem = [person_uno, person_dos]

name, age, favourite = person_uno

print(name)
print(age)
print(favourite)

for name, age, favourite in mandem:
    print(name)
    print(age)
    print(favourite)
    print()
