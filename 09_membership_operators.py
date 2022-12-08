fruits = ["apple", "pear", "banana"]
comodin = 0


while True:
  var = input("Enter a fruit: ").lower()
  if var.isalpha():
    if var in fruits:
      print("Finded")
    elif var not in fruits:
      print("Not finded")
  else:
    print("Enter a Fruit please")
