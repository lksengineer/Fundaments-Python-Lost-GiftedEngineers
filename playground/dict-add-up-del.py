person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

# Add New Key: Value to the Dict
person['twitter'] = '@nicobytes'

# Update Key 'name' by Value 'Felipe'
person['name'] = 'Felipe'

# delete key age of the dict
# del person['age']
person.pop('age')

# Print list with the keys of the dict
print(list(person.keys()))

# Print list with the values of the dict
print(list(person.values()))
