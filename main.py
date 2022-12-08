fruits = ["apple", "pear", "banana"]

while True:
  var = input("Enter a fruit: ").lower()
  if var in fruits:
    print("Finded")
  elif var not in fruits:
    print("Not finded")

