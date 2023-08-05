person = {
  'name': 'nico',
  'last_name': 'molina',
  'langs': ['python', 'javascript'],
  'age': 99
}

print(person)

# Update the dict
person['name'] = 'santi'
person['age'] -= 50
person['langs'].append('rust')
print(person)

# Delete a key  of the dict
del person['last_name']
person.pop('age')

print(person)

# Return Keys: Values
print('items')
print(person.items())

# Return Keys
print('keys')
print(person.keys())

# Return Values
print('values')
print(person.values())