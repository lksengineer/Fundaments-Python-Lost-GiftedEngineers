'''
for element in range(1, 21):
  print(element)

'''

my_list = [23, 45, 67, 89 ,43]
for element in my_list:
  print(element)

my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
  print(element)


product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 89
}

for key in product:
  print(key, '=>', product[key])

for key, value in product.items():
  print(key, '=>', value)

people = [
  {
    'name': 'nico',
    'age': 34
  },
  {
    'name': 'zule',
    'age': 45
  },
  {
    'name': 'santi',
    'age': 4
  }
]

for person in people:
  print(person)
  print('name =>', person['name'])
  for x, y in person.items():
    print(x, y)


zoo = {
    'Leon': 8,
    'Jirafa': 5,
    'Hipo': 4,
}

for animal, cantidad in zoo.items():
    print(f'En el zoo tenemos el/la {animal} con una poblacion de {cantidad}')