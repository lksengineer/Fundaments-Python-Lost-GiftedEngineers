'''
while True:
  print('se ejecuto')


counter = 0

while counter < 10:
  counter += 1
  print(counter)


counter = 0

while counter < 20:
  counter += 1
  if counter == 15:
    break
  print(counter)
'''

counter = 0

while counter < 20:
  counter += 1
  if counter < 15:
    continue
  print(counter)


"""The else Statement
With the else statement we can run a block of code once when the condition no longer is true:"""

# Example
# Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")