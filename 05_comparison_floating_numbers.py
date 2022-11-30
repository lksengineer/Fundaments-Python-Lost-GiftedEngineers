x = 3.3
y = 1.1 + 2.2
tolerance = 0.00001

print(f'x = {x}')
print(f'y = {y}')
print(f'(x - y): {x-y}')
print(f'abs(x - y): {abs(x-y)}')
print(abs(x-y) < tolerance)
