#Slices
b = "Hello, World!"
print("\n Slices:")
print(b)
print(b[-5:-2])  #Display from -5 to -2
print(b[::-1])  #Display reversing
print(b[::2])  #display 2 in 2
print(b[5:2:-1])  #Display from 5 to 2 inversed

print("\n Strings:")
#strip()
a = " Hello world! "
print(a.strip())  # returns "Hello, World!"

#count()
print("\b")
print(f'{b} tiene {b.count("o")} \'o\'')

#upper()
print(a.upper())

#lower()
print(a.lower())

#swapcase
print(a.swapcase())

#replace()
print(a.replace("l", "r"))

#split()
a = "hello world"
print(a.split(" "))

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize())
print(text_2.title())