

"""
List method:
Python tiene un conjunto de métodos integrados que puede usar en las listas.

Method	Description:
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value

extend()	Add the elements of a list (or any iterable), to the end of the current list

index()	Returns the index of the first element with the specified value

insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""


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


# IN: Check if "apple" is present in the list:
print("n\IN: Check if 'apple' is present in the list:")
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")