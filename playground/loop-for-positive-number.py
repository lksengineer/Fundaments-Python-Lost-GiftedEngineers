my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

# For loop
for num in my_list:
  if num > 0:
    new_list.append(num)
print(new_list)

# lambda function with filter
new_list = list(filter(lambda num: num > 0, my_list))
print(new_list)

# Comprehension List
new = [num for num in my_list if num > 0]
print(new)