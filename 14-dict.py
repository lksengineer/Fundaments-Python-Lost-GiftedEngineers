my_dict = {}
print(type(my_dict))

my_dict = {
  'avion': "bla bla bla",
  'name': 'Nicolas',
  'last_name': 'Molina Monroy',
  'age': 87
}

# Print the dict
print(my_dict)

# Len of the dict
print(len(my_dict))

# Print value of a key
print(my_dict['age'])
print(my_dict['last_name'])

# Print value of a key with get() method (Return Null if there is not value)
print(my_dict.get('age'))


# Buscar el valor de una llave por el nombre de la llave
print('avion' in my_dict)
print('otroqueno' in my_dict)