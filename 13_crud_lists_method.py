# CRUD WITH LISTS METHOD

# 1. Create
numbers = [1, 2, 5, 4, 6, 1, 6, 6, 6, 7, 5]

# 2. Read
print(numbers)
print(numbers[1])
print(numbers[0:4:2])
print(numbers[-1])
print(f'Count(7): {numbers.count(7)}')

# 3. Update
strings = ['hello', 'please', 'you are welcome']

numbers[1] = 0
print(numbers)

# insert
numbers.insert(1, 2)
print(f'\b insert {numbers}')

# index
index = numbers.index(0)
print(f'\n index(0): {index}')
numbers[index] = 3
print(f'\n replace index {numbers}')

# append
numbers.append(10)
print(numbers)

# sort
names = ["Luis", "Daniel", "Carlos", "Juana", "Esmelda", "Pedro", "Juan", "Carlota", "Daniela"]

numbers.sort()
print(numbers)

names.sort()
print(names)

# reverse
numbers.reverse()
print(f'\n Reverse {numbers}')

# concatenar lists
numbers = numbers + strings
print(numbers)


# Delete

# remove() Remove elements
numbers.remove("hello")
print(f'\n remove("hello"): {numbers}')

# pop() Remove indexes
numbers.pop()
print(f'\n pop(): {numbers}')

numbers.pop(0)
print(f'\n pop(0): {numbers}')

