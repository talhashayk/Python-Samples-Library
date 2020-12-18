digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(digits[1])
print(digits[-1])
print(len(digits))

# SLICING
# The first number is inclusive, second is exclusive
print(digits[0:3])

name = "first last"
print(name[0:5])
# Same as
print(name[:5])

print(digits[:-1])
print(digits[:-2])
print(digits[-1: 0])  # Doesn't work

print(digits[0:])

# STRIDING
print(digits[0:10:1])
print(digits[0:10:2])
print(digits[0:10:3])
print(digits[::1])
print(digits[::4])
print(digits[::-1])
print(digits[::-2])

# Direction of slicing must always be in the right order, i.e. negative or positive

for i in range(len(digits)):
    print(digits[:i+1])

for i in range(len(digits)-2):
    print(digits[i:i+3])

window_size = 3
for i in range(len(digits) - 2):
    print(digits[i:i + window_size])

for i in range(len(digits) - (window_size-1)):
    print(digits[i:i + window_size])
