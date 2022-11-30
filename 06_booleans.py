# Evaluate True values
print("\n*****True values*****")
print(10 <= 16)
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = '15'

print(bool(x))
print(bool(y))

# Evaluate False values
print("\n*****False values*****")
print(10 >= 16)
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Evaluate a booleans with functions
print("\nEvaluate booleanda with isinstance() functions")
print(isinstance(14, str))

print("\nEvaluate booleanda with isalnum() functions")
x = "ghg5448"
print(x.isalnum())

print("\nEvaluate booleanda with isnumeric() functions")
x = "gghg5874"
print(x.isnumeric())

